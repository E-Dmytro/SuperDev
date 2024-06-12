# -*- coding: UTF-8 -*-
import clr
import sys
import Autodesk
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')
#from system import *
from Autodesk.Revit.DB import *
from Autodesk.Revit.Exceptions import *
from Autodesk.Revit.UI.Selection import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI import Selection
import System
from System import Guid
#from Autodesk.Revit.UI.Selection import *
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
from System.Collections.Generic import List
import math
from random import randint

from operator import itemgetter
import operator
import itertools
curview = uidoc.ActiveGraphicalView
__doc__='Перевірка назви групи до колони'
__author__ = 'Дмитро Серебріян'
#1 - 01 form, #2 - 11 form
"""els = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]

for i in els:
	0#print(i.Id)

list1 = List[ElementId]()
list1.Add(els[0].Id)
rebars = uidoc.Selection.SetElementIds(list1)
"""
#Замінити ДСТУ в усій арматурі
"""rebar_types = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rebar).WhereElementIsElementType().ToElements()
t = Transaction(doc, 'd')
t.Start()
for i in rebar_types:
	par = i.LookupParameter('О_Обозначение')
	if par != None:
		par_string = par.AsString()
		try:
			if 'ДСТУ' in par_string:
				par.Set('ДСТУ 3760:2019')
		except:
			print(1)
	print(par)
t.Commit()"""

titleblocks = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks).WhereElementIsNotElementType().ToElements()
#t = Transaction(doc, '1')
#t.Start()
list1 = List[ElementId]()
for i in titleblocks:
	if i.Name == 'Універсальний':
		list1.Add(i.Id)
		#par_1 = i.LookupParameter('Підписи Увімкн.').Set(0)
		#par_2 = i.LookupParameter('Підпис_Виконав').Set(3)
		#par_2 = i.LookupParameter('Підпис_Перевірив').Set(4)
		print(i.Name)
#t.Commit()
rebars = uidoc.Selection.SetElementIds(list1)
