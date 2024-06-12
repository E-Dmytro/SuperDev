# -*- coding: utf-8 -*-

__title__ = "Schedule Filter Change"
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
#
#         # Find the filter for the field named 'Batch'
#         for i, filter in enumerate(filters):
#             fieldId = filter.FieldId
#             fieldName = selected_schedule.Definition.GetField(fieldId).GetName()
#             if fieldName == 'Batch':
#                 # Update the filter value
#                 filter.SetValue('1')
#
#                 # Update the filter in the schedule
#                 selected_schedule.Definition.SetFilter(i, filter)
#                 break
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
# # Start a transaction
# with DB.Transaction(doc, "Add Filter") as t:
#     t.Start()
#
#     # Iterate over each selected schedule
#     for selected_schedule in selected_schedules:
#         # Get all available fields in the schedule
#         fields = selected_schedule.Definition.GetFields()
#
#         # Find the field named 'Batch'
#         for field in fields:
#             if field.GetName() == 'Batch':
#                 # Create a new filter for this field
#                 new_filter = DB.ScheduleFilter()
#
#                 # Set the filter field and value
#                 new_filter.FieldId = field.FieldId
#                 new_filter.SetValue('1')
#
#                 # Add the new filter to the schedule
#                 selected_schedule.Definition.AddFilter(new_filter)
#                 break
#
#     t.Commit()



from pyrevit import revit, DB

# Get the current document
doc = revit.doc

# Get the selected schedules
selected_schedules = revit.get_selection()

# Start a transaction
with DB.Transaction(doc, "Add Filter") as t:
    t.Start()

    # Iterate over each selected schedule
    for selected_schedule in selected_schedules:
        # Get the ScheduleDefinition
        definition = selected_schedule.Definition

        # Get the IDs of all fields in the schedule
        field_ids = definition.GetFieldOrder()

        # Initialize a variable to track if the 'Batch' filter is found
        batch_filter_found = False

        # Find the field named 'Batch'
        for field_id in field_ids:
            field = definition.GetField(field_id)
            if field.GetName() == 'Batch':
                # Create a new filter for this field
                new_filter = DB.ScheduleFilter()

                # Set the filter field and value
                new_filter.FieldId = field.FieldId
                new_filter.SetValue('1')

                # Add the new filter to the schedule
                definition.AddFilter(new_filter)

                # Set the tracking variable to True
                batch_filter_found = True
                break

    t.Commit()

