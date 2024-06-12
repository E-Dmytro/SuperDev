# -*-coding: utf-8 -*-

__title__ = "AddLevelHoles" #Name of the button displayed in Revit UI
# __doc__   ="""This tool will add/update your level name to have its elevation.""" #Button Description shown in Revit UI

__doc__ = """ Version = 1.0
Date    = 07.08.2023
_____________________________________________________________________
Description:
Function to add holes into wall parameters as Level Label

There is an option to Add/Update or Remove them.
_____________________________________________________________________
How-to:

-> Click on the Button 

_____________________________________________________________________
Last update:
- [07.08.2023] - 1.0 RELEASE
_____________________________________________________________________
Author: Dmytro Khom"""

__author__ = "Dmytro Khom"
# __helpurl__ = "www.youtube.com" #TO DO: Update URL
# __highlight__ = "new"
# __min_revit_ver__  = 2019
# __max_revit_ver__  = 2022
# __context__ = ['Walls', 'Floors', 'Roofs'] # Make your button available only when certain categories are selected 


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================

# Regular + Autodesk
import os, sys, math, datetime, time
# from Autodesk.Revit.DB import * #Import everything from DB (Very good for beginners and development)
from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector, Level, BuiltInCategory, TextNoteType, XYZ, UnitUtils, ForgeTypeId, TextNote

# pyRevit
from pyrevit import revit, forms

# Custom Imports
from Snippets._selection import get_selected_elements
from Snippets._convert import convert_internal_to_m


# .NET Import
import clr 
clr.AddReference("System")
from System.Collections.Generic import List  #List<ElementType>() <- it's special type of kist that RevitAPI often requires.

# list_elements_ids = [ElementId(546771), ElementId(546771)] # Let's imagine these are real element Ids...
# List_element_ids= List[ElementId](list_elements_ids)
#
# uidoc.Selection.SetElementIds(List_element_ids)

# for e_id in list_elements_ids:
#     List_element_ids.Add(e_id)


# from System.Collections.Generic import List #List<Element() <- it's special type of list that RevitAPI often requires.

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ===========================================================================
# from pyrevit.revit import uidoc, doc, app #Alternative
doc    = __revit__.ActiveUIDocument.Document
uidoc  = __revit__.ActiveUIDocument
app    = __revit__.Application
PATHSCRIPT = os.path.dirname(__file__)

# Symbols

symbol_start = "."
symbol_end   = "."


# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ===========================================================================

# IMPORTS
# from Autodesk.Revit.DB import *
#
#
#
# all_openings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
# host_walls = [opening.Host for opening in all_openings]
#
# # Get the transformation from the internal coordinate system to the shared coordinate system
# transform = doc.ActiveProjectLocation.GetTransform()
#
# t = Transaction(doc, 'Set Option1 parameter')
# t.Start()
# for opening, wall in zip(all_openings, host_walls):
#     bb = opening.get_BoundingBox(None)
#     max_point = bb.Max.Z
#     max_pointX = bb.Max.X
#     min_pointX = bb.Min.X
#     max_pointY = bb.Max.Y
#     min_pointY = bb.Min.Y
#     mid_pointY = (max_pointY + min_pointY) / 2
#     mid_pointX = (max_pointX + min_pointX) / 2
#     print("X= " + str(mid_pointX))
#     textNoteType = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElement()
#     location = XYZ(mid_pointX, mid_pointY, 0)
#     textNote = TextNote.Create(doc, doc.ActiveView.Id, location, "Wall Annotation", textNoteType.Id)
#
#     # Transform the maximum Z value from the Revit model coordinate system to the Dynamo coordinate system
#     # max_point_transformed = transform.OfPoint(XYZ(0, 0, max_point)).Z
#     z_display_units = UnitUtils.ConvertFromInternalUnits(max_point, DisplayUnitType.DUT_METERS)
#     print (z_display_units)
#     rounded_min_value = round(z_display_units, 2)
#     project_base_point_value = rounded_min_value
#     print(project_base_point_value)
#     option1_param = wall.LookupParameter('Option1')
#     if option1_param:
#         wall_openings = [opening for opening in all_openings if opening.Host.Id == wall.Id]
#         if len(wall_openings) > 1:
#             z_display_units_values = [round(UnitUtils.ConvertFromInternalUnits(opening.get_BoundingBox(None).Max.Z, DisplayUnitType.DUT_METERS), 2) for opening in wall_openings]
#             if len(set(z_display_units_values)) > 1:
#                 option1_param.Set(', '.join(map(str, z_display_units_values)))
#             else:
#                 option1_param.Set(str(project_base_point_value))
#         else:
#             option1_param.Set(str(project_base_point_value))
# t.Commit()

# from Autodesk.Revit.DB import *

# # Add annotations for all Openings that is on the MODEL
# all_openings = FilteredElementCollector(doc).OfCategory(
#     BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()

# # Add annotations for all Openings that is on the ACTIVE VIEW
all_openings = FilteredElementCollector(doc, doc.ActiveView.Id).OfCategory(
    BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
host_walls = [opening.Host for opening in all_openings]

# Get the transformation from the internal coordinate system to the shared coordinate system
transform = doc.ActiveProjectLocation.GetTransform()

t = Transaction(doc, 'Set Option1 parameter')
t.Start()
for opening, wall in zip(all_openings, host_walls):
    bb = opening.get_BoundingBox(None)
    max_point = bb.Max.Z
    max_pointX = bb.Max.X
    min_pointX = bb.Min.X
    max_pointY = bb.Max.Y
    min_pointY = bb.Min.Y
    mid_pointY = (max_pointY + min_pointY) / 2
    mid_pointX = (max_pointX + min_pointX) / 2
    print("X= " + str(mid_pointX))
    textNoteType = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElement()
    location = XYZ(mid_pointX, mid_pointY, 0)

    # # Transform the maximum Z value from the Revit model coordinate system to the Dynamo coordinate system
    # # max_point_transformed = transform.OfPoint(XYZ(0, 0, max_point)).Z
    # z_display_units = UnitUtils.ConvertFromInternalUnits(max_point, DisplayUnitType.DUT_METERS)
    # print(z_display_units)
    # rounded_min_value = round(z_display_units, 2)
    # project_base_point_value = rounded_min_value
    # print(project_base_point_value)
    # Instead of using DisplayUnitType.DUT_METERS, use ForgeTypeId
    z_display_units = UnitUtils.ConvertFromInternalUnits(max_point, ForgeTypeId('autodesk.unit.unit:meters-1.0.2'))
    print(z_display_units)
    rounded_min_value = round(z_display_units, 2)
    project_base_point_value = rounded_min_value
    print(project_base_point_value)


    # Insert the relevant z_display_units_value into the text note
    textNote = TextNote.Create(doc, doc.ActiveView.Id, location, str(project_base_point_value), textNoteType.Id)

    option1_param = wall.LookupParameter('Option1')
    if option1_param:
        wall_openings = [opening for opening in all_openings if opening.Host.Id == wall.Id]
        if len(wall_openings) > 1:
            z_display_units_values = [round(UnitUtils.ConvertFromInternalUnits(opening.get_BoundingBox(None).Max.Z, ForgeTypeId('autodesk.unit.unit:meters-1.0.2')), 2) for opening in wall_openings]
            # z_display_units_values = [round(
            #     UnitUtils.ConvertFromInternalUnits(opening.get_BoundingBox(None).Max.Z, DisplayUnitType.DUT_METERS), 2)
            #                           for opening in wall_openings]
            if len(set(z_display_units_values)) > 1:
                option1_param.Set(', '.join(map(str, z_display_units_values)))
            else:
                option1_param.Set(str(project_base_point_value))
        else:
            option1_param.Set(str(project_base_point_value))
t.Commit()



# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ===========================================================================


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN


# GET all Levels



    # if lvl.Elevation > 0:
    #     var = '+' + str(lvl_elevation_m)
    # else:
    #     var = str(lvl_elevation_m)


