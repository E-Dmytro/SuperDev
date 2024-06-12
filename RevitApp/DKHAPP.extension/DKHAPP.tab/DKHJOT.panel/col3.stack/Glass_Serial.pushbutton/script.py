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
# __highlight__ = "new"
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

    def set_parameter(self, param_name, value):
        # Call LookupParameter on the window_element
        param = self.window_element.LookupParameter(param_name)
        if param:
            param.Set(value)
        else:
            print("Parameter not found")



class GlassType:
    def __init__(self, window):
        self.window = window

    def get_type_symbol(self,glass_type):
        # window_parameters = self.window.get_window_parameters()
        # glass_type = window_parameters.get("Construction Type")
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


class ChangeSize:
    def __init__(self, window):
        self.window = window

    def get_transformed_dimensions(self, parameter):
        # Check if the parameter is a string that can be converted to a float
        try:
            upd_parameter = float(parameter) / 10
            upd_parameter = int(upd_parameter) if upd_parameter.is_integer() else upd_parameter
        except ValueError:
            # If not, get the parameter from the window parameters
            window_parameters = self.window.get_window_parameters()
            upd_parameter = float(window_parameters.get(parameter)) / 10
            upd_parameter = int(upd_parameter) if upd_parameter.is_integer() else upd_parameter
        return upd_parameter



class Sizes:
    def __init__(self, window):
        self.window = window
        self.size = ChangeSize(window)
        self.type = GlassType(window)
    def get_sizes_parmeters(self):
        supercomponent = self.window.SuperComponent
        window_parameters = self.window.get_window_parameters()
        glass_position = window_parameters.get("Glass Height Position")

        height = self.size.get_transformed_dimensions("Height")
        width = self.size.get_transformed_dimensions("Width")

        width_parent = supercomponent.LookupParameter("Width").AsValueString()
        width_parent = self.size.get_transformed_dimensions(width_parent)
        # width_parent = supercomponent.size.get_transformed_dimensions("Width")
        # print (width_parent)
        try:
            type_top_element_full = supercomponent.Symbol.LookupParameter("Glass Type B").AsValueString()
            # print (type_top_element_full)
            type_top_element_short = self.type.get_type_symbol(type_top_element_full)
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

class WindowParameterTransformer:
    def __init__(self, window):
        self.window = window

    def get_transformed_parameters(self):
        window_parameters = self.window.get_window_parameters()
        glass_type = window_parameters.get("Construction Type")

        # Create an instance of GlassType and call get_type_symbol
        glass_type_instance = GlassType(self.window)
        type_symbol = glass_type_instance.get_type_symbol(glass_type)

        def get_parameter_value(param_name, default_value=""):
            param_value = window_parameters.get(param_name)
            if param_value in ["Left", "Right"]:
                return "%s" % param_value[0]
            elif param_value == "Yes":
                return "%s" % param_name.split()[1][0]
            else:
                return default_value

        glass_bld_output_side = get_parameter_value("BLD_Output Side")
        glass_orientation_side = get_parameter_value("Glass Corner Orientation")
        glass_symbol = window_parameters.get("Glass Family Symbol", "U")
        angle_type = get_parameter_value("Angle Left") or get_parameter_value("Angle Right")

        return {
            "glass_types": type_symbol,
            "glass_bld_output_side": glass_bld_output_side,
            "glass_orientation_side": glass_orientation_side,
            "glass_symbol": glass_symbol,
            "angle_type": angle_type,
        }



class WindowCombiner:
    def __init__(self,  window, transformer):
        self.window =  window
        self.transformer = transformer

    def combine(self, symbol, values):
        # Get transformed parameters
        return symbol.join(str(value) for value in values if value)

    def assign_to_parameter(self, param_name, value):  # Add 'value' as a parameter
        self.window.window_element.LookupParameter(param_name).Set(value)


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
window_filter = WindowFilter(doc)
windows = window_filter.filter_windows('Glass')



# 🔓 Start Transaction
with Transaction(doc, __title__) as t:
    t.Start()
    for window in windows:
        window = Window(window)

        transformer = WindowParameterTransformer(window)
        combiner = WindowCombiner(window, transformer)  # Create a WindowCombiner instance

        sizes = Sizes(window)

        # Get the parent parameters
        window_parameters = window.get_window_parameters()

        # Get the transformed parameters
        transformed_parameters = transformer.get_transformed_parameters()

        # Get the parent parameters
        sizes_parameters = sizes.get_sizes_parmeters()

        # Get the glass type
        name_family = window_parameters['NameFamily']
        glass_details_name = window_parameters['Glass Details Name']

        glass_symbol = transformed_parameters['glass_symbol']
        glass_type = transformed_parameters['glass_types']
        glass_bld_output_side = transformed_parameters['glass_bld_output_side']
        glass_orientation_side = transformed_parameters["glass_orientation_side"]
        angle_type = transformed_parameters["angle_type"]

        width_parent = sizes_parameters["Width_parent"]
        height = sizes_parameters["Height"]

        # Assign the combined string to the "Glass Details Name" parameter
        if name_family == "UV":
            combine = glass_symbol, width_parent, glass_bld_output_side
        else:
            combine = glass_symbol, glass_orientation_side,width_parent, height, glass_type, angle_type

        # glass_details_name = window.LookupParameter("Glass Details Name").Set(combine)
        # Use the WindowCombiner instance to combine the values and assign them to the parameter
        combined_value = combiner.combine("-", combine)  # Combine the values
        combiner.assign_to_parameter("Glass Details Name", combined_value)  # Assign the combined value to the parameter
    # 🔒 End Transaction
    t.Commit()












