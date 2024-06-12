# -*- coding: UTF-8 -*-
import clr
#Подключение библиотек
from System.Threading import Thread, ThreadStart
from operator import itemgetter
import math
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
from pyrevit import revit, DB, UI
from pyrevit import forms




__doc__ = 'Видаляє вид із проекта'


selection = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]

t=Transaction(doc, 'viewdel')
# Opens the associated view with the selected viewport on a sheet.
if len(selection) > 0 and isinstance(selection[0], DB.Viewport):
    vp = selection[0]
    vpid = vp.ViewId
    view = doc.GetElement(vpid)
    t.Start()
    doc.Delete(view.Id)
    t.Commit()
    #revit.uidoc.ActiveView = view
else:
    forms.alert('Виберіть спочатку видовий екран')

