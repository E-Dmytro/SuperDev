# -*- coding: utf-8 -*-

__title__ = "GroupSave"
__author__ = "Erik Frits"
__doc__ = """Version = 1.2
This script was create for grouping elements that ungrouped
_____________________________________________________________________
"""


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ==================================================
import os
import json
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Group

doc = __revit__.ActiveUIDocument.Document
groups = FilteredElementCollector(doc).OfClass(Group).ToElements()
gr_dict = {}
for group in groups:
    gr_name = group.Name
    gr_id = str(group.Id)
    # print("Group ID: ", gr_name )
    # print("Element IDs in the group:")
    gr_dict[gr_name] = {gr_id: []}
    for elementId in group.GetMemberIds():
        gr_dict[gr_name][gr_id].append(str(elementId))

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file_data = os.path.realpath(os.path.join(location + '/data_list.json'))
# Save data_list to a JSON file
with open(file_data, 'w') as f:
    json.dump(gr_dict, f)
