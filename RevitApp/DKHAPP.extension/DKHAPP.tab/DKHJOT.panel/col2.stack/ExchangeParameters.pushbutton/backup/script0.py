# -*-coding: utf-8 -*-

__title__ = "Exchange Parameters" #Name of the button displayed in Revit UI
__version__ = "Version = 1.0"
__doc__ = """ Version = 1.0
Date    = 26.08.2022
_____________________________________________________________________
Description:

A script that exchanges parameters between another or new
______________________________________
Author: Dmytro Khom"""
__author__ = "Dmytro Khom"
__highlight__ = "new"
# bundle help url
__helpurl__ = "https://www.youtube.com/watch?v=H7b8hjHbauE&t=8s&list=PLc_1PNcpnV57FWI6G8Cd09umHpSOzvamf"

# help url can also be in various locales
# pyRevit pulls the correct help url based on Revit langauge





# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# =======================================================================
# Regular + Autodesk
from Autodesk.Revit.DB import ElementId,BuiltInParameter,ParameterValueProvider,FilterStringEquals,\
                                FilterStringRule,ElementParameterFilter,FilteredElementCollector,\
                                Transaction,UnitUtils,BuiltInCategory
#Import everything from DB (Very good for beginners and development)
from Autodesk.Revit.UI import UIDocument, UIApplication
# .NET IMPORT
import clr
clr.AddReference('System')
from System import Enum
from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox,Separator, Button, CheckBox)
# # pyRevit
from pyrevit import revit, forms
from pyrevit.forms import select_views

from System.Collections.Generic import List


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
def get_type_by_name(type_name):
    "Extra Function to get Family Type by name"
    # CREATE RULE
    param_type        = ElementId(BuiltInParameter.ALL_MODEL_TYPE_NAME)
    f_param           = ParameterValueProvider(param_type)
    evaluator         = FilterStringEquals()
    f_rule            = FilterStringRule(f_param, evaluator, type_name, True) #Revit 2023 doesn't need last argument!

    # CREATE FILTER
    filter_type_name = ElementParameterFilter(f_rule)

    # GET ELEMENTS
    return FilteredElementCollector(doc).WherePasses(filter_type_name).WhereElementIsElementType().FirstElement()
def get_elements_by_family_name(family_name):
    """Function to get Elements by Family Name."""

    # CREATE RULE
    param_id    = ElementId(BuiltInParameter.ALL_MODEL_TYPE_NAME)
    f_param     = ParameterValueProvider(param_id)
    f_evaluator = FilterStringEquals()
    f_rule      = FilterStringRule(f_param, f_evaluator  , family_name, True)
    # Revit 2023 does not need last argument in f_rule!

    # CREATE FILTER
    filter_family_name = ElementParameterFilter(f_rule)

    # GET ELEMENTS
    return FilteredElementCollector(doc).WherePasses(filter_family_name)\
                               .WhereElementIsNotElementType().ToElements()
def convert_internal_units (value, get_internal = True, units='m'):
    # type: (float, bool, str) -> float I
    """Function to convert Internal units to meters or vice versa.
    :param value: Value to convert
    :param get_internal: True to get internal units, False to get Meters
    :param units:  Select desired Units: ['m', 'm2']
    :return: Length in Internal units or Meters."""

    if rvt_year >= 2021:
        from Autodesk.Revit.DB import UnitTypeId
        if units == 'm'   : units = UnitTypeId.Meters
        elif units == 'm2': units = UnitTypeId.SquareMeters
        elif units == 'cm': units = UnitTypeId.Centimeters
    else:
        from Autodesk.Revit.DB import DisplayUnitType
        if units == 'm'   : units = DisplayUnitType.DUT_METERS
        elif units == 'm2': units = DisplayUnitType.DUT_SQUARE_METERS
        elif units == 'cm': units = DisplayUnitType.DUT_CENTIMETERS

    if get_internal:
        return UnitUtils.ConvertToInternalUnits(value, units)
    return UnitUtils.ConvertFromInternalUnits(value, units)

def random_step(_min, _max, _step):
    import random
    return random.randrange(_min, _max+1, _step)
# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ===========================================================================


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN




# 1️⃣ Variables (Custom UI)

# Get all categories in the document
categories = doc.Settings.Categories

# Create a dictionary of category names and their corresponding Category objects
category_dict = {category.Name: category for category in categories}
# builtin_category_dict = {Enum.GetName(BuiltInCategory, category): category for category in BuiltInCategory.GetValues(BuiltInCategory)}


components = [Label("Select a Category:"),
              ComboBox('category', category_dict),
              Separator(),
              Label("First Parameter Name"), TextBox('first_param_name', Text="Mark"),
              Label('Second Parameter Name'), TextBox('second_param_name', Text="Comments"),
              Separator(),
              Button('Select')]

form = FlexForm(__title__, components)
# # Show the form
form.show()
#
# # Get the selected category
values = form.values
selected_category = values['category']
enumCategory = selected_category.Id.IntegerValue
first_parameter_name = values['first_param_name']
# print (selected_category)
second_parameter_name = values['second_param_name']
# Convert the integer value to a BuiltInCategory enum
# builtinCategory = BuiltInCategory(enumCategory)
builtinCategory = Enum.ToObject(BuiltInCategory, enumCategory)
# selected_builtin_category = BuiltInCategory(selected_category.Id.IntegerValue)
category_collector = FilteredElementCollector(doc).OfCategory(builtinCategory).WhereElementIsNotElementType().ToElements()

# print (category_collector)




t = Transaction(doc, __title__)
t.Start() # 🔓



# Commit the transaction

for elements in category_collector:
    param = elements.LookupParameter(first_parameter_name).AsString()
    # print (param)
    if param is None:
        param="None"
    print (param)
    elements.LookupParameter(second_parameter_name).Set(param)
    # elements.LookupParameter(second_parameter_name).Set('None')





t.Commit() #🔒







# 🔷 Bonus: Custom UI





























# value = form.values
# type_name   = values ['first_param_name']
# parma_name  = values ['second_param_name']


# from rpw import doc
# from rpw.ui.forms import FlexForm, Label, ComboBox, Button
#
#
#
# # Create components for the form
# components = [
#     Label("Select a Category:"),
#     ComboBox('category', category_dict),
#     Button('OK')
# ]
#
# # Create the form
# form = FlexForm("Category Selector", components)
#
# # # Show the form
# form.show()
# #
# # # Get the selected category
# selected_category = form.values['category']
#
# # Now 'selected_category' is the Category object selected by the user
