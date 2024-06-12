# -*- coding: utf-8 -*-

__title__ = "ScheduleFTR Change"
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


# from pyrevit import revit, DB
#
# # Get the current document
# doc = revit.doc
#
# # Get the selected schedules
# selected_schedules = revit.get_selection()
#
# # Start a transaction
# with DB.Transaction(doc, "Update Filter") as t:
#     t.Start()
#
#     # Iterate over each selected schedule
#     for selected_schedule in selected_schedules:
#         # Get the existing filters
#         filters = selected_schedule.Definition.GetFilters()
#         print(filters)
#
#         # # Find the filter for the field named 'Mark'
#         # for i, filter in enumerate(filters):
#         #     fieldId = filter.GetFieldId()
#         #     fieldName = selected_schedule.Definition.GetField(fieldId).GetName()
#         #     if fieldName == 'Mark':
#         #         # Update the filter value
#         #         filter.SetValue('1')
#         #
#         #         # Update the filter in the schedule
#         #         selected_schedule.Definition.SetFilter(i, filter)
#         #         break
#
#     t.Commit()

# from pyrevit import revit, DB
#
# # Get the current document
# doc = revit.doc
#
# # Get the selected schedules
# selected_schedules = revit.get_selection()
#
# # Iterate over each selected schedule
# for selected_schedule in selected_schedules:
#     # Get the existing filters
#     filters = selected_schedule.Definition.GetFilters()
#
#     # Print the name of each filter
#     for filter in filters:
#         fieldId = filter.FieldId
#         fieldName = selected_schedule.Definition.GetField(fieldId).GetName()
#         print(fieldName)


from pyrevit import revit, DB

# Get the current document
doc = revit.doc

# Get the selected schedules
selected_schedules = revit.get_selection()

# Start a transaction
with DB.Transaction(doc, "Update Filter") as t:
    t.Start()

    # Iterate over each selected schedule
    for selected_schedule in selected_schedules:
        # Get the existing filters
        filters = selected_schedule.Definition.GetFilters()

        # Find the filter for the field named 'Batch'
        for i, filter in enumerate(filters):
            fieldId = filter.FieldId
            fieldName = selected_schedule.Definition.GetField(fieldId).GetName()
            if fieldName == 'Batch':
                # Update the filter value
                filter.SetValue('1')

                # Update the filter in the schedule
                selected_schedule.Definition.SetFilter(i, filter)
                break

    t.Commit()
