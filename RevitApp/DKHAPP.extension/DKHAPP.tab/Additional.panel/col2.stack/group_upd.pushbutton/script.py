# -*- coding: utf-8 -*-

__title__ = "GroupUpd"
__author__ = "Erik Frits"
__doc__ = """Version = 1.2
This script was create for grouping elements that ungrouped
_____________________________________________________________________
"""

# Function

# from Autodesk.Revit.DB import Transaction, GroupType, FilteredElementCollector,Group, BuiltInCategory
# import json
# import os
#
# def add_to_group(doc, gr_name, gr_id, element):
#     # Start a new transaction
#     t = Transaction(doc, 'Add to group')
#     t.Start()
#
#     try:
#         # Find the group type
#         group_type = doc.GetElement(gr_id)
#
#         if group_type is None:
#             # The group type does not exist, create a new one
#             group_type = GroupType.Create(doc, gr_name)
#
#         # Find the group
#         group = None
#         for g in FilteredElementCollector(doc).OfClass(Group).ToElements():
#             if g.GroupType.Id == group_type.Id:
#                 group = g
#                 break
#
#         if group is None:
#             # The group does not exist, create a new one
#             group = doc.Create.NewGroup([element.Id])
#             group.GroupType = group_type
#         else:
#             # The group exists, add the element to it
#             group.InsertMember(element)
#
#         # Commit the transaction
#         t.Commit()
#     except Exception as e:
#         # Something went wrong, roll back the transaction
#         t.RollBack()
#         print('Failed to add element to group:', e)
#
#
# # ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# # ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# # ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# # ==================================================
# doc = __revit__.ActiveUIDocument.Document
#
# location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# file_data = os.path.realpath(os.path.join(location + '/data_list.json'))
#
# def get_ungrouped_elements(doc):
#     # Get all elements
#     all_elements =FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()
#
#     # Filter out the elements that are in a group
#     ungrouped_elements = [e for e in all_elements if e.GroupId.IntegerValue == -1]
#
#     return ungrouped_elements
#
#
# # Load group data from JSON file
# with open(file_data, 'r') as f:
#     group_data = json.load(f)
#
# # Get ungrouped elements
# ungrouped_elements = get_ungrouped_elements(doc)
#
# # Group ungrouped elements based on the JSON file
# for element in ungrouped_elements:
#     element_id = str(element.Id)
#     for gr_name in group_data:
#         for gr_id in group_data[gr_name]:
#             if element_id in group_data[gr_name][gr_id]:
#                 # The element should be in this group, add it
#                 add_to_group(doc, gr_name, gr_id, element)
#


from Autodesk.Revit.DB import Transaction, ElementId
doc = __revit__.ActiveUIDocument.Document
# Start a new transaction
t = Transaction(doc, 'Create group')
t.Start()

try:
    # List of element IDs
    element_ids = ["433392", "433393", "433394", "437369", "437370"]

    # Create a new group with these elements
    group = doc.Create.NewGroup(element_ids)

    # Commit the transaction
    t.Commit()
except Exception as e:
    # Something went wrong, roll back the transaction
    t.RollBack()
    print('Failed to create group:', e)