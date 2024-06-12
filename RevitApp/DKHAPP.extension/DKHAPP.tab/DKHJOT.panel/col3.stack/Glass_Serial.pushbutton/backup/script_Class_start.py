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
    def filter_windows(self):
        collector = FilteredElementCollector(self.doc)
        windows = collector.OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()

        # Filter windows starting with 'Glass'
        glass_windows = [Window(window) for window in windows if window.Name.startswith('Glass')]

        return glass_windows


class Window:
    def __init__(self, window_element):
        self.window_element = window_element

    def get_name(self):
        return self.window_element.Name

    def get_window_parameters(window_element):
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
    def __init__(self, glass_type):
        self.glass_type = glass_type

    def get_type_symbol(self):
        if self.glass_type == "Glass_Black":
            return "B"
        elif self.glass_type == "Glass_Wavy":
            return "P"
        elif self.glass_type == "Glass_Clear_PP":
            return "VP"
        elif self.glass_type == "Glass_Clear":
            return "V"
        else:
            return "None"



class WindowParameterTransformer:
    def __init__(self, window):
        self.window = window

    def get_transformed_parameters(self):
        window_parameters = self.window.get_window_parameters()
        name_family = window_parameters.get("NameFamily")
        glass_type = GlassType(window_parameters.get("Construction Type"))
        glass_type_total = glass_type.get_type_symbol()
        glass_position = window_parameters.get("Glass Height Position")

        # Initialize glass_bld_output_side with a default value
        glass_bld_output_side = ""
        if window_parameters.get("BLD_Output Side") == "Left":
            glass_bld_output_side = "-L"
        elif window_parameters.get("BLD_Output Side") == "Right":
            glass_bld_output_side = "-R"

        # Initialize glass_orientation_side with a default value
        glass_orientation_side = ""
        if window_parameters.get("Glass Corner Orientation") == "Left":
            glass_orientation_side = "-L"
        elif window_parameters.get("Glass Corner Orientation") == "Right":
            glass_orientation_side = "-R"

        if window_parameters.get("Glass Family Symbol"):
            glass_symbol = window_parameters.get("Glass Family Symbol")
        else:
            glass_symbol = "U"

        if window_parameters.get("Angle Left") == "Yes":
            angle_type = "-L"
        elif window_parameters.get("Angle Right") == "Yes":
            angle_type = "-R"
        else:
            angle_type = ""

        height = float(window_parameters.get("Height")) / 10
        width = float(window_parameters.get("Width")) / 10

        height = int(height) if height.is_integer() else height
        width = int(width) if width.is_integer() else width

        return {
            "name_family": name_family,
            "glass_type_total": glass_type_total,
            "glass_position": glass_position,
            "glass_bld_output_side": glass_bld_output_side,
            "glass_orientation_side": glass_orientation_side,
            "glass_symbol": glass_symbol,
            "angle_type": angle_type,
            "height": height,
            "width": width
        }


class WindowCombiner:
    def __init__(self,  window_element, transformer):
        self.window =  window
        self.transformer = transformer

    def combine(self):
        # Get transformed parameters
        params = self.transformer.get_transformed_parameters()

        # Initialize combine
        combine = ""
        param_s =  params["glass_symbol"]
        # Define Family
        if params["name_family"] == "U":
            combine = param_s + "-" + str(params["width"]) + "-" + str(params["height"]) + "-" + params["glass_type_total"] + params["angle_type"]

        elif params["name_family"] == "UTL":
            type_top_element_full = self.window_element.window_element.Symbol.LookupParameter("Glass Type B").AsValueString()
            type_top_element_short = GlassType(type_top_element_full).get_type_symbol()

            if params["glass_position"] == "Bottom" and (type_top_element_short == "B" or type_top_element_short == "P"):
                params["height"] = str(params["height"]) + "X"
            combine = params["glass_symbol"] + "-" + str(params["width"]) + "-" + str(params["height"]) + "-" + params["glass_type_total"] + params["angle_type"]

        elif params["name_family"] == "UW" or params["name_family"] == "UWB":
            if params["glass_symbol"]=="W":
                combine = params["glass_symbol"] + "-" + str(params["width"]) + "-" + str(params["height"]) + "-V"
            else:
                combine = params["glass_symbol"] + "-" + str(params["width"]) + "-" + str(params["height"]) + "-" + params["glass_type_total"]

        elif params["name_family"] == "UV":
            combine = params["glass_symbol"] + "-" + str(params["width"])  + params["glass_bld_output_side"]

        elif params["name_family"] == "UCEXT":
            if params["glass_symbol"] == "EXS":
                combine = params["glass_symbol"] + params["glass_orientation_side"] + "-" + str(params["width"]) + "-" + str(params["height"]) + "-" + params["glass_type_total"] + params["angle_type"]
            else:
                combine = params["glass_symbol"] + "-" + str(params["width"]) + "-" + str(params["height"]) + "-" + params["glass_type_total"] + params["angle_type"]

        return combine

    def assign_to_parameter(self, param_name):
        combine = self.combine()
        self.window.window_element.LookupParameter(param_name).Set(combine)





# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN

# 🔓 Start Transaction
with Transaction(doc, __title__) as t:
    t.Start()
    window_filter = WindowFilter(doc)
    glass_windows = window_filter.filter_windows()
    for window_element in glass_windows:
        window = Window(window_element)  # Create a Window object
        transformer = WindowParameterTransformer(window)
        combiner = WindowCombiner(window, transformer)
        combiner.assign_to_parameter("Glass Details Name")
        # Assign the combined string to the "Glass Details Name" parameter
        glass_details_name = window.LookupParameter("Glass Details Name").Set(combiner)

    # 🔒 End Transaction
    t.Commit()












