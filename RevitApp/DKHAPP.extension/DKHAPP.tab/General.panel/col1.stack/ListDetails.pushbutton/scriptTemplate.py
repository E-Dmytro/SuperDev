# -*-coding: utf-8 -*-

__title__ = "Furniture Room" #Name of the button displayed in Revit UI
__doc__   ="""This is simple tool to Copy Elemement With Revit API """ #Button Description shown in Revit UI
__version__ = "Version = 1.0"
__doc__ = """ Version = 1.0
Date    = 02.09.2023
_____________________________________________________________________
Description:

Test code about Get all Furniture and Plumbing elements and write Room's name
if available to a comment Parameter.
______________________________________
Author: Dmytro Khom"""
__author__ = "Dmytro Khom"




# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================

# Regular + Autodesk
from Autodesk.Revit.DB import *    #Import everything from DB (Very good for beginners and development)
from Autodesk.Revit.UI import UIDocument, UIApplication

# .NET IMPORT
import clr
clr.AddReference('System')


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ===========================================================================
# from pyrevit.revit import uidoc, doc, app #Alternative
doc    = __revit__.ActiveUIDocument.Document   #type: UIDocument
uidoc  = __revit__.ActiveUIDocument            #type: Document
app    = __revit__.Application                 #type: UIApplication



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
# ===========================================================================



# 🔓 Start Transaction
t = Transaction(doc, __title__)
t.Start()













# 🔒 End Transaction
t.Commit()

