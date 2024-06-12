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
def get_window_parameters(doc):
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


    for window in windows:
        # if window.Symbol.Family.Name == 'U':
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
                            if value=="":
                                value = None
                    except:
                        # print("%s: Parameter not found" % param)
                        param_values[param] = "Parameter not found"
                        continue
                # print("%s: %s" % (param, value))
                param_values[param] = value
    return param_values





# Assuming 'doc' is your Document object
window_parameters = get_window_parameters(doc)

def get_type_glass(glass_type):
    if glass_type=="Glass_Black":
        glass_type_symbol = "B"
    elif glass_type == "Glass_Wavy":
        glass_type_symbol = "P"
    elif glass_type == "Glass_Clear_PP":
        glass_type_symbol = "VP"
    elif glass_type == "Glass_Clear":
        glass_type_symbol = "V"
    return  glass_type_symbol

glass_type_total = get_type_glass(window_parameters.get("Construction Type"))
# print (glass_type_total)
name_family = window_parameters.get("NameFamily")


if name_family == "U":
    # Get the value of Parameters
    height = float(window_parameters.get("Height")) / 10
    width = float(window_parameters.get("Width")) / 10

    # Convert to int if the float value is an integer
    height = int(height) if height.is_integer() else height
    width = int(width) if width.is_integer() else width
    combine = "U-" + str(width) + "-" + str(height) + "-" + glass_type_total



# 👉 Step
# # 🔓 Start Transaction
with Transaction(doc, __title__) as t:
    t.Start()
    for window in windows:
        supercomponent = window.SuperComponent
        if supercomponent is not None:
            glass_details_name = supercomponent.LookupParameter("Glass Details Name").Set(combine)
            # print(glass_details_name)
    # 🔒 End Transaction
    t.Commit()











