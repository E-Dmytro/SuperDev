# -*-coding: utf-8 -*-
import math
__title__ = "Glass Type"
# __doc__ = """This is a simple tool for
__version__ = "Version = 1.0"
__doc__ = """ Glass TYPE SORT param"""
__author__ = "Dmytro"
# __highlight__ = "new"
# bundle help url
__helpurl__ = "https://www.autodesk.com"


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================

# Regular + Autodesk
from Autodesk.Revit.DB import *  # Import everything from DB (Very good for beginners and development)
from Autodesk.Revit.DB.Structure import StructuralType
# .NET IMPORT
import clr
from pyrevit import revit, forms
clr.AddReference('System')
# # pyRevit
from pyrevit import revit, forms
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, FamilyInstance
from collections import defaultdict

doc = __revit__.ActiveUIDocument.Document

from System.Collections.Generic import List

# # from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector, Level, BuiltInCategory


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ===========================================================================
# from pyrevit.revit import uidoc, doc, app #Alternative
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application

active_view = doc.ActiveView
active_level = doc.ActiveView.GenLevel








# # Start a new transaction
# t = Transaction(doc, "Update Glass Type S")
# t.Start()
#
# collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType()
#
# for window in collector:
#     # Get the FamilyType of the window
#     family_type = doc.GetElement(window.GetTypeId())
#     # Try to get the "Glass type" parameter
#     glass_type_param = family_type.LookupParameter('Glass Type')
#     # Check if the parameter is not None
#     if glass_type_param is not None and glass_type_param.HasValue:
#         # Get the value of the 'Glass Type' parameter
#         glass_type_value = glass_type_param.AsValueString()
#         # Try to get the 'Glass Type S' project parameter
#         glass_type_s_param = window.LookupParameter('Glass Type S')
#         # Check if the 'Glass Type S' parameter exists and set its value
#         if glass_type_s_param is not None:
#             glass_type_s_param.Set(glass_type_value)
#
# # Commit the transaction
# t.Commit()

# Function

def update_glass_type(window, glass_type_name, gtx_name):
    # Get the FamilyType of the window
    family_type = doc.GetElement(window.GetTypeId())
    # Try to get the "Glass type" parameter
    glass_type_param = family_type.LookupParameter(glass_type_name)
    # Check if the parameter is not None
    if glass_type_param is not None and glass_type_param.HasValue:
        # Get the value of the 'Glass Type' parameter
        glass_type_value = glass_type_param.AsValueString()
        # Try to get the 'Glass Type S' project parameter
        glass_type_s_param = window.LookupParameter(gtx_name)
        # Check if the 'Glass Type S' parameter exists and set its value
        if glass_type_s_param is not None:
            glass_type_s_param.Set(glass_type_value)





# Start a new transaction
t = Transaction(doc, "Update Glass Type S")
t.Start()

collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType()

for window in collector:
    update_glass_type(window, 'Glass Type', 'GTX')
    update_glass_type(window, 'Glass Type Right', 'GTX_R')
    update_glass_type(window, 'Glass Type Left', 'GTX_L')
    update_glass_type(window, 'Glass Type Left B', 'GTX_L_B')
    update_glass_type(window, 'Glass Type Right B', 'GTX_R_B')
    update_glass_type(window, 'Glass Type Step', 'GTX_S')
    update_glass_type(window, 'Glass Type B', 'GTX_B')
    update_glass_type(window, 'Glass Type Step B', 'GTX_S_B')
    update_glass_type(window, 'Glass Type A', 'GTX_A')
    update_glass_type(window, 'Glass Type Window', 'GTX_W')




# Commit the transaction
t.Commit()







