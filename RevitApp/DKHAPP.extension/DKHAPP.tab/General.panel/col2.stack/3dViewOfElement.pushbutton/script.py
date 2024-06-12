# -*-coding: utf-8 -*-

__title__ = "Element 3Dview " #Name of the button displayed in Revit UI
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


# from Autodesk.Revit.DB import View3D, ViewFamily, BoundingBoxIntersectsFilter, FilteredElementCollector, Transaction, XYZ
# from Autodesk.Revit.UI.Selection import ObjectType
#
# # Get the current document and UI document
# doc = __revit__.ActiveUIDocument.Document
# uidoc = __revit__.ActiveUIDocument
#
# # Pick an object in the Revit UI
# picked = uidoc.Selection.PickObject(ObjectType.Element)
#
# # Get the element from the picked object using its ElementId
# element = doc.GetElement(picked.ElementId)
#
# # Get the bounding box of the element
# bbox = element.get_BoundingBox(doc.ActiveView)
#
# # Create a new 3D view
# viewFamilyType = FilteredElementCollector(doc).OfClass(ViewFamilyType).ToElements()
# for i in viewFamilyType:
#     if i.ViewFamily == ViewFamily.ThreeDimensional:
#         viewFamilyType = i
#         break
#
# transaction = Transaction(doc, "Create 3D view")
# transaction.Start()
# view3D = View3D.CreateIsometric(doc, viewFamilyType.Id)
# view3D.Name = "3D View - " + element.Name
#
# # Set the section box of the 3D view to the bounding box of the element
# view3D.SetSectionBox(bbox)
# transaction.Commit()


from Autodesk.Revit.DB import View3D, ViewFamily, BoundingBoxIntersectsFilter, FilteredElementCollector, Transaction, XYZ, ElementId
from Autodesk.Revit.UI.Selection import ObjectType

# Get the current document and UI document
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# Pick an object in the Revit UI
picked = uidoc.Selection.PickObject(ObjectType.Element)

# Get the element from the picked object using its ElementId
element = doc.GetElement(picked.ElementId)

# Get the bounding box of the element
bbox = element.get_BoundingBox(doc.ActiveView)

# Create a new 3D view
viewFamilyType = FilteredElementCollector(doc).OfClass(ViewFamilyType).ToElements()
for i in viewFamilyType:
    if i.ViewFamily == ViewFamily.ThreeDimensional:
        viewFamilyType = i
        break

transaction = Transaction(doc, "Create 3D view")
transaction.Start()
view3D = View3D.CreateIsometric(doc, viewFamilyType.Id)
view3D.Name = "3D View - " + element.Name

# Set the section box of the 3D view to the bounding box of the element
view3D.SetSectionBox(bbox)

# Hide all elements in the view except for the selected one
collector = FilteredElementCollector(doc, view3D.Id)
for el in collector:
    if el.Id != element.Id:
        view3D.HideElementTemporary(el.Id)

transaction.Commit()





