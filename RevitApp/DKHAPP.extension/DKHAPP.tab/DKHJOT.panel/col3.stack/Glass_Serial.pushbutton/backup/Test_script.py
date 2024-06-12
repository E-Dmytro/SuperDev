# -*-coding: utf-8 -*-

__title__ = "Glass Serial" #Name of the button displayed in Revit UI
__version__ = "Version = 1.0"
__doc__ = """ Version = 1.0
Date    = 26.08.2022
_____________________________________________________________________
Description:

Test code about Copying Elements 
using Revit API
______________________________________
Author: Dmytro Khom"""
__author__ = "Dmytro Khom"
__highlight__ = "new"
# bundle help url
__helpurl__ = "https://www.youtube.com/watch?v=H7b8hjHbauE&t=8s&list=PLc_1PNcpnV57FWI6G8Cd09umHpSOzvamf"

# help url can also be in various locales
# pyRevit pulls the correct help url based on Revit langauge
__helpurl__  = {
  "en_us": "https://www.youtube.com/watch?v=H7b8hjHbauE&t=8s&list=PLc_1PNcpnV57FWI6G8Cd09umHpSOzvamf",
  "chinese_s": "https://www.youtube.com/watch?v=H7b8hjHbauE&t=8s&list=PLc_1PNcpnV57FWI6G8Cd09umHpSOzvamf"}




# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================
# Regular + Autodesk
from Autodesk.Revit.DB import *    #Import everything from DB (Very good for beginners and development)
from Autodesk.Revit.DB.Structure import StructuralType
# .NET IMPORT
import clr
clr.AddReference('System')

# # pyRevit
from pyrevit import revit, forms
from pyrevit.forms import select_views

from System.Collections.Generic import List
# # from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector, Level, BuiltInCategory

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ===========================================================================
# from pyrevit.revit import uidoc, doc, app #Alternative
doc    = __revit__.ActiveUIDocument.Document
uidoc  = __revit__.ActiveUIDocument
app    = __revit__.Application


# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ===========================================================================


# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ===========================================================================

class WindowFilter:
    def __init__(self, doc):
        self.doc = doc

    def filter_windows(self, startswith):
        collector = FilteredElementCollector(self.doc)
        windows = collector.OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()

        # Filter windows starting with 'startswith'
        filtered_windows = [window for window in windows if window.Name.startswith(startswith)]

        return filtered_windows



class Window:
    def __init__(self, window_element):
        self.window_element = window_element
        self.SuperComponent = window_element.SuperComponent

    def get_name(self):
        return self.window_element.Name

    def get_window_parameters(self):
        window_element = self.window_element
        parameters = [
            "Height",
            "Width",
            "Construction Type",
            "Angle Left",
            "Angle Right",
            "BLD_Output Side",
            "Step Left",
            "Step Right",
            "Glass Corner Orientation",
            "Glass Height Position",
            "NameFamily",
            "Glass Family Symbol",
            "Glass Details Name"
        ]
        param_values = {}
        for param in parameters:
            try:
                # Try to get the parameter from the instance
                value = window_element.LookupParameter(param).AsValueString()
                if value == None:
                    value = window_element.LookupParameter(param).AsString()
                    if value == "":
                        value = None
            except:
                try:
                    # If not found, try to get it from the type
                    value = window_element.Symbol.LookupParameter(param).AsValueString()
                    if value == None:
                        value = window_element.Symbol.LookupParameter(param).AsString()
                        if value == "":
                            value = None
                except:
                    param_values[param] = "Parameter not found"
                    continue
            param_values[param] = value
        return param_values

class GlassType:
    def __init__(self, window):
        self.window = window

    def get_type_symbol(self):
        window_parameters = self.window.get_window_parameters()
        glass_type = window_parameters.get("Construction Type")
        if glass_type == "Glass_Black":
            return "B"
        elif glass_type == "Glass_Wavy":
            return "P"
        elif glass_type == "Glass_Clear_PP":
            return "VP"
        elif glass_type == "Glass_Clear":
            return "V"
        elif glass_type.startswith("Glass_Window"):
            return "V"
        else:
            return "None"

class Size:
    def __init__(self, window):
        self.window = window

    def get_transformed_dimensions(self, parameter):
        window_parameters = self.window.get_window_parameters()

        upd_parameter = float(window_parameters.get(parameter)) / 10
        upd_parameter = int(upd_parameter) if upd_parameter.is_integer() else upd_parameter
        return window_parameters


class Sizes:
    def __init__(self, window):
        self.window = window
        self.size = Size(window)
    def get_sizes_parmeters(self):
        supercomponent = self.window.SuperComponent
        window_parameters = self.window.get_window_parameters()
        glass_position = window_parameters.get("Glass Height Position")

        height = self.size.get_transformed_dimensions("Height")
        width = self.size.get_transformed_dimensions("Width")

        width_parent = supercomponent.Symbol.LookupParameter("Width")
        try:
            type_top_element_full = supercomponent.Symbol.LookupParameter("Glass Type B").AsValueString()
            type_top_element_short = self.window.get_type_symbol(type_top_element_full)
        except:
            type_top_element_short = ""


        if glass_position == "Bottom" and (type_top_element_short == "B" or type_top_element_short == "P"):
            height = str(height) + "X"
        else:
            height = str(height)

        return {
            "Width":  width,
            "Width_parent": width_parent,
            "Height": height,
        }



# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN

window_filter = WindowFilter(doc)
filtered_windows = window_filter.filter_windows('Glass')

for window_element in filtered_windows:

    window = Window(window_element)
    # Get the parent parameters
    window_parameters = window.get_window_parameters()

    sizes = Sizes(window)





    # Get the parent parameters
    sizes_parameters = sizes.get_sizes_parmeters()

    # Get the glass type
    name_family = window_parameters['NameFamily']
    width_parent = sizes_parameters ["Width_parent"]
    height = sizes_parameters ["Height"]



# 🔓 Start Transaction
with Transaction(doc, __title__) as t:
    t.Start()

    # 🔒 End Transaction
    t.Commit()












