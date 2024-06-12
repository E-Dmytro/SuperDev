# Import the necessary libraries
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction
from pyrevit import revit, DB

# Get all elements of the Window category
windows = FilteredElementCollector(revit.doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()

# Start a new transaction
t = Transaction(revit.doc, 'Assign Family and Type')
t.Start()

# Iterate through each window
for window in windows:
    # Get the Family name
    family_name = window.Symbol.Family.Name
    # print (family_name)
    # Get the Type name
    # type_name = window.Symbol.get_Parameter(DB.BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
    # # Combine Family and Type
    # # Assign to the new parameter (replace 'NewParameterName' with the actual parameter name)
    window.LookupParameter('NameFamily').Set(family_name)

# Commit the transaction
t.Commit()