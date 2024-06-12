# -*- coding: utf-8 -*-

__title__ = "Append To ViewName"
__author__ = "Dmytro Kh"
__doc__ = """Version = 1.2
Date    = 12.01.2024
_____________________________________________________________________
_____________________________________________________________________
"""


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ==================================================
from Autodesk.Revit.DB import (View,
                               ViewPlan,
                               ViewSection,
                               View3D,
                               ViewSchedule,
                               ViewDuplicateOption,
                               Transaction,
                               ViewType,
                               ViewSheet,
                               FilteredElementCollector,
                               FamilySymbol,
                    BuiltInParameter,
                    ParameterValueProvider,
                    FilterStringEquals,
                    FilterStringRule,
                    ViewScheduleExportOptions,
                    ElementParameterFilter,
                    SectionType,
                    ViewDrafting,
                               ElementId)
# pyRevit
from pyrevit.forms import WPFWindow, alert

# Custom imports
# from Snippets._selection import get_selected_views


# .NET Imports
from clr import AddReference
AddReference("System")
from System.Collections.Generic import List
from System.Diagnostics.Process import Start
from System.Windows.Window      import DragMove
from System.Windows.Input       import MouseButtonState

from pyrevit import revit, DB
# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ==================================================


from pyrevit import revit, DB

# Get the current selection
selection = revit.get_selection()

# Iterate over each selected element
for element in selection:
    # Check if the element is a view
    if isinstance(element, DB.View):
        # Skip view templates
        if not element.IsTemplate:
            # Append "Batch 1" to the view name
            view_name = element.Name + " Batch 1"

            # Start a transaction to modify the document
            with DB.Transaction(revit.doc, "Update View Names") as t:
                t.Start()
                # Update the view name
                element.Name = view_name
                t.Commit()

