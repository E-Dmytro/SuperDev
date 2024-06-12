# -*-coding: utf-8 -*-

__title__ = "Copy View Filter" #Name of the button displayed in Revit UI
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
# __highlight__ = "new"
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


#🟢COPY WITH VECTOR
#🟢
#🟢
# 👉 Step 1: Get Views/ViewTemplates with Filters
all_views = (FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Views)\
    .WhereElementIsNotElementType()\
    .ToElements())

#🔎 Views with Filters
# views_with_filters          = [v for v in all_views if v.GetFilters()]
# only_views_with_filters     = [v for v in all_views if v.GetFilters() and not v.IsTemplate]
# only_templates_with_filters = [v for v in all_views if v.GetFilters() and v.IsTemplate      ]
# print ('All Views and ViewTemplates: {}'.format(len(views_with_filters)))
# print ('All Views with filters: {}'.format(len(only_templates_with_filters)))
# print ('All ViewsTemplates with filters: {}'.format(len(only_templates_with_filters)))
views_with_filters          = [v for v in all_views if v.GetFilters()]

# ✔ Ensure there are views with Filters in the project!
if not views_with_filters:
    forms.alert('There are no Views/ViewTemplates with Filters applied to them! Please Try Again', exitscript=True)

# 📃 Create Dict of Views
dict_views_with_filters = {v.Name:v for v in views_with_filters}



# 👉 Step 2: Select Source View/ViewTemplate

# select_src_views = forms.SelectFromList.show(dict_views_with_filters.keys(),
select_src_views = forms.SelectFromList.show(sorted(dict_views_with_filters),
                                title='Select Source View/ViewTemplate',
                                multiselect=False,
                                button_name='Select Source View/ViewTemplate')
# ✔ Ensure src_view is selected
if not select_src_views:
    forms.alert('No Source View/ViewTemplate was selected.Please Try Again', exitscript=True)

src_view = dict_views_with_filters[select_src_views]


# 👉 Step 3: Select Filters To Copy

filter_ids = src_view.GetFilters()
filters    = [doc.GetElement(f_id) for f_id in filter_ids]
dict_filters = {f.Name:f for f in filters}


selected_filters= forms.SelectFromList.show(sorted(dict_filters),
                                title='Select Filters to Copy',
                                multiselect=True,
                                button_name='Select Filters to Copy')

# ✔ Ensure src_view is selected
if not selected_filters:
    forms.alert('No Filters were Selected. Please Try Again.', exitscript=True)

filters_to_copy = [dict_filters[f_name] for f_name in selected_filters ]


# The same as on upper, but without List Comprehension
# filters = []
# for f_id in filter_ids:
#     f = doc.GetElement(f_id)
#     filters.append(f)

# 👉 Step 4: Select Destination Views
dict_all_views = {v.Name:v for v in all_views}
selected_dest_views = forms.SelectFromList.show(sorted(dict_all_views),
                                title='Select Destination Views/ViewTemplates',
                                multiselect=True,
                                button_name='Select Destination Views/ViewTemplates')
# ✔ Ensure src_view is selected
if not selected_dest_views:
    forms.alert('No Destination View/ViewTemplate was selected.Please Try Again', exitscript=True)

src_view = dict_views_with_filters[select_src_views]

dest_views = [dict_all_views[v_name] for v_name in selected_dest_views]

# 👉 Step 5: Copy View Filters
# # 🔓 Start Transaction
with Transaction(doc, __title__) as t:

    t.Start()
    for view_filter in filters_to_copy:
        filter_overrides = src_view.GetFilterOverrides(view_filter.Id)

        for view in dest_views:
            view.SetFilterOverrides(view_filter.Id,filter_overrides)
# # # 🔒 End Transaction
    t.Commit()


# Filter Overrides
# Apply Filter

# override toggle








