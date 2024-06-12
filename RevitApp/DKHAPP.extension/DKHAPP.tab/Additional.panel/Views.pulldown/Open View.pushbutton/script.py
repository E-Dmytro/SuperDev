# -*- coding: UTF-8 -*-
from pyrevit import revit, DB, UI
from pyrevit import forms


__doc__ = 'Відкрити вид поточного видового екрана'


selection = revit.get_selection()

# Opens the associated view with the selected viewport on a sheet.
if len(selection) > 0 and isinstance(selection[0], DB.Viewport):
    vp = selection[0]
    vpid = vp.ViewId
    view = revit.doc.GetElement(vpid)
    revit.uidoc.ActiveView = view
else:
    forms.alert('Виберіть спочатку видовий екран')
