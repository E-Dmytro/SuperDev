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


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN


#🟢COPY WITH VECTOR

# Filter for windows of family 'U'
collector = FilteredElementCollector(doc)
windows = collector.OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()
def get_window_parameters(window):
    parameters = [
        "Height",
        "Width",
        "Construction Type",
        "Angle Left",
        "Angle Right",
        # "Glass Family Symbol",
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
    if window.Symbol.Family.Name.startswith('Glass'):
        for param in parameters:
            try:
                # Try to get the parameter from the instance
                value = window.LookupParameter(param).AsValueString()
                if value == None:
                    value = window.LookupParameter(param).AsString()
                    if value == "":
                        value = None
            except:
                try:
                    # If not found, try to get it from the type
                    value = window.Symbol.LookupParameter(param).AsValueString()
                    if value == None:
                        value = window.Symbol.LookupParameter(param).AsString()
                        if value == "":
                            value = None
                except:
                    param_values[param] = "Parameter not found"
                    continue
            param_values[param] = value
    return param_values


# # Assuming 'doc' is your Document object
# window_parameters = get_window_parameters(doc)

def get_type_glass(glass_type):
    if glass_type=="Glass_Black":
        glass_type_symbol = "B"
    elif glass_type == "Glass_Wavy":
        glass_type_symbol = "P"
    elif glass_type == "Glass_Clear_PP":
        glass_type_symbol = "VP"
    elif glass_type == "Glass_Clear":
        glass_type_symbol = "V"
    else:
        glass_type_symbol = "None"
    return  glass_type_symbol


# print (glass_type_total)
# 👉 Step
# 🔓 Start Transaction
with Transaction(doc, __title__) as t:
    t.Start()
    for window in windows:

        supercomponent = window.SuperComponent
        if supercomponent is not None:

            # Get window parameters for each window
            window_parameters = get_window_parameters(window)
            name_family = window_parameters.get("NameFamily")
            glass_type_total = get_type_glass(window_parameters.get("Construction Type"))
            glass_position = window_parameters.get("Glass Height Position")

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
            # Get the value of Parameters
            height = float(window_parameters.get("Height")) / 10
            width = float(window_parameters.get("Width")) / 10

            # Convert to int if the float value is an integer
            height = int(height) if height.is_integer() else height
            width = int(width) if width.is_integer() else width


            # Define Family
            if name_family == "U":
                # glass_type_total = get_type_glass(window_parameters.get("Construction Type"))
                combine = glass_symbol + "-" + str(width) + "-" + str(height) + "-" + glass_type_total + "-" + angle_type
                glass_details_name = window.LookupParameter("Glass Details Name").Set(combine)
            elif name_family == "UTL":
                type_top_element_full = supercomponent.Symbol.LookupParameter("Glass Type B").AsValueString()
                type_top_element_short = get_type_glass(type_top_element_full)

                if glass_position == "Bottom" and (type_top_element_short == "B" or type_top_element_short == "P"):
                    height = str(height) + "X"
                combine = glass_symbol + "-" + str(width) + "-" + str(height) + "-" + glass_type_total + angle_type

                #     Result
                glass_details_name = window.LookupParameter("Glass Details Name").Set(combine)
    # 🔒 End Transaction
    t.Commit()












