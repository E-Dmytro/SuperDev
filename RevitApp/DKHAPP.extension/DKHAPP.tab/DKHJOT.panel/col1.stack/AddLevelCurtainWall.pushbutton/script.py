# -*-coding: utf-8 -*-
import math
__title__ = "AddLevelCurtainWall"
# __doc__ = """This is a simple tool for
__version__ = "Version = 1.0"
__doc__ = """ Glass TYPE SORT param"""
__author__ = "Dmytro"
__highlight__ = "new"
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








# Get the current document


# Get all curtain panels in the document
collector = FilteredElementCollector(doc)
curtain_panels = collector.OfClass(FamilyInstance).OfCategory(BuiltInCategory.OST_CurtainWallPanels).ToElements()

# Start a transaction
t = Transaction(doc, 'Set Curt_Level Parameter')
t.Start()

# Iterate over the curtain panels
for panel in curtain_panels:
    # Get the LevelId
    level_id = panel.LevelId

    # Get the level name
    level = doc.GetElement(level_id)
    level_name = level.Name

    # Set the Curt_Level parameter
    panel.LookupParameter('Level_Curt').Set(level_name)

# Commit the transaction
t.Commit()

print('Curt_Level parameter set for all Curtain Panel family instances.')



