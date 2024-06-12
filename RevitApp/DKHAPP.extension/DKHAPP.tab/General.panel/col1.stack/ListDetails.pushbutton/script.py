# -*- coding: UTF-8 -*-
import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = os.path.realpath(os.path.join(location + '/log.txt'))
from datetime import datetime

from rpw import revit
user = revit.username
with open(file, mode='a+') as csv_file:
	csv_file.writelines(str(user) + ' ' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '\n')
import clr
import sys
from System.Collections.Generic import *
__persistentengine__ = True
import Autodesk
from Autodesk.Revit.UI import IExternalEventHandler, IExternalApplication, Result, ExternalEvent, IExternalCommand, TaskDialog
from Autodesk.Revit.DB import Transaction
from Autodesk.Revit.Exceptions import InvalidOperationException, OperationCanceledException, ArgumentException
import rpw
from rpw import revit, DB, UI
from pyrevit.forms import WPFWindow
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
from Autodesk.Revit.Exceptions import *
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

#app = uiapp.Application
import Autodesk.Revit.DB as RVT
RS = RVT.Structure
curview = uidoc.ActiveGraphicalView
from operator import itemgetter

__doc__='Створити специфікацію на активному виді'
__author__ = 'Дмитро Серебріян'
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')
from system import *

class CustomizableEvent:
	def __init__(self):
		""" An instance of this class need to be created before any modeless operation.
		You can then call the raise_event method to perform any modeless operation.
		Any modification to Revit DB need to be performed inside a valid Transaction.
		This Transaction needs to be open inside the function_or_method, NOT before calling raise_event.
		>>> customizable_event = CustomizableEvent()
		>>> customizable_event.raise_event(rename_views, views_and_names)
		"""
		# Create an handler instance and his associated ExternalEvent
		custom_handler = _CustomHandler()
		custom_handler.customizable_event = self
		self.custom_event = UI.ExternalEvent.Create(custom_handler)

		# Initialise raise_event variables
		self.function_or_method = None
		self.args = ()
		self.kwargs = {}

	def _raised_method(self):
		""" !!! DO NOT USE THIS METHOD IN YOUR SCRIPT !!!
		Method executed by IExternalEventHandler.Execute when ExternalEvent is raised by ExternalEvent.Raise.
		"""
		self.function_or_method(*self.args, **self.kwargs)

	def raise_event(self, function_or_method, *args, **kwargs):
		"""
		Method used to raise an external event with custom function and parameters
		Example :
		>>> customizable_event = CustomizableEvent()
		>>> customizable_event.raise_event(rename_views, views_and_names)
		"""
		self.args = args
		self.kwargs = kwargs
		self.function_or_method = function_or_method
		self.custom_event.Raise()

class _CustomHandler(UI.IExternalEventHandler):
	""" Subclass of IExternalEventHandler intended to be used in CustomizableEvent class
	Input : function or method. Execute input in a IExternalEventHandler"""
	def __init__(self):
		self.customizable_event = None

	# Execute method run in Revit API environment.
	# noinspection PyPep8Naming, PyUnusedLocal
	def Execute(self, application):
		try:
			self.customizable_event._raised_method()
		except InvalidOperationException:
			# If you don't catch this exeption Revit may crash.
			print "InvalidOperationException catched"

	# noinspection PyMethodMayBeStatic, PyPep8Naming
	def GetName(self):
		return "Execute an function or method in a IExternalHandler"


customizable_event = CustomizableEvent()
class ModelessForm(WPFWindow):

	def __init__(self, xaml_file_name):
		WPFWindow.__init__(self, xaml_file_name)
		self.out_list = None
		self.Show()

	def write_filter(self):
		doc = __revit__.ActiveUIDocument.Document
		t=Transaction(doc, 'Відомості')
		t.Start()
		els = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]

		if len(els) > 0:
			if str(els[0].Category.Id) == '-2000510':
				filter_status = '0'
				for e in FilteredElementCollector(doc, els[0].ViewId).OfCategory(BuiltInCategory.OST_DetailComponents).WhereElementIsNotElementType().ToElements():
					e_type = doc.GetElement(e.GetTypeId())
					det_fam_name = e_type.get_Parameter(BuiltInParameter.ALL_MODEL_FAMILY_NAME).AsString()
					if det_fam_name == 'Дет0':
						if self.radio_1.IsChecked:
							filter_type = 'marka'
						elif self.radio_2.IsChecked:
							filter_type = 'mrkcon'
						elif self.radio_3.IsChecked:
							filter_type = 'mrkizd'
						#TaskDialog.Show('er','er2')
						change_com = ('{}*/{}*/{}*/{}').format(self.Filter_value.Text, filter_type, str(self.One_construction_check.IsChecked), str(self.Arm_vupysk_check.IsChecked))
						filter_status = e.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).Set(change_com)
						#TaskDialog.Show('er','er3')
						compl_draw = els[0].LookupParameter('Орг.КомплектКреслень').Set(self.Complect_value.Text)
						vidm_draw = els[0].LookupParameter('Орг.Відмітка').Set(self.Elevation_value.Text)
						view_name = els[0].get_Parameter(BuiltInParameter.VIEW_NAME).Set(self.Name_value.Text + '_Відомість деталей')
						#TaskDialog.Show('er','er4')
			else:
				TaskDialog.Show('error', 'Виберіть відомість деталей')

		else:
			TaskDialog.Show('error', 'Виберіть відомість деталей')
		t.Commit()

	def read_filter(self):
		doc = __revit__.ActiveUIDocument.Document
		#TaskDialog.Show('er','1')
		els = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]
		if len(els) > 0:
			if str(els[0].Category.Id) == '-2000510':
				view_name = els[0].get_Parameter(BuiltInParameter.VIEW_NAME).AsString()
				#TaskDialog.Show('er','2')
				if '_' in view_name:
					mark_name = view_name.split('_')[0]
				else:
					mark_name = error
				compl_draw = els[0].LookupParameter('Орг.КомплектКреслень').AsString()
				vidm_draw = els[0].LookupParameter('Орг.Відмітка').AsString()
				for e in FilteredElementCollector(doc, els[0].ViewId).OfCategory(BuiltInCategory.OST_DetailComponents).WhereElementIsNotElementType().ToElements():
					e_type = doc.GetElement(e.GetTypeId())
					det_fam_name = e_type.get_Parameter(BuiltInParameter.ALL_MODEL_FAMILY_NAME).AsString()
					if det_fam_name == 'Дет0':

						#newdet=doc.Create.NewFamilyInstance(XYZ(0,0,0), r0, detail_create)
						filter_status = e.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).AsString()
						if len(filter_status.split('*/')) == 4:

							filter_type = filter_status.split('*/')[1]
							one_cons = filter_status.split('*/')[2]
							s_filter = filter_status.split('*/')[0]
							arm_vup_check = filter_status.split('*/')[3]
							self.Complect_value.Text = compl_draw
							self.Elevation_value.Text = vidm_draw
							self.Name_value.Text = mark_name
							self.Filter_value.Text = s_filter

							if one_cons == 'True':
								self.One_construction_check.IsChecked = True
							else:
								self.One_construction_check.IsChecked = False
							if arm_vup_check == 'True':
								self.Arm_vupysk_check.IsChecked = True
							else:
								self.Arm_vupysk_check.IsChecked = False
							if filter_type == 'marka':
								self.radio_1.IsChecked = True
							elif filter_type == 'mrkcon':
								self.radio_2.IsChecked = True
							elif filter_type == 'mrkizd':
								self.radio_3.IsChecked = True

			else:
				TaskDialog.Show('error', 'Виберіть відомість деталей')
		else:
			TaskDialog.Show('error', 'Виберіть відомість деталей')
	def create_detail(self, status):
		status = status[0]

		uidoc = __revit__.ActiveUIDocument
		doc = __revit__.ActiveUIDocument.Document
		curview = uidoc.ActiveGraphicalView

		s_name = ('{}*/{}*/{}').format(self.Complect_value.Text,self.Elevation_value.Text,self.Name_value.Text)
		s_filter = self.Filter_value.Text
		if self.radio_1.IsChecked:
			filter_type = 'marka'
		elif self.radio_2.IsChecked:
			filter_type = 'mrkcon'
		elif self.radio_3.IsChecked:
			filter_type = 'mrkizd'
		one_cons = self.One_construction_check.IsChecked
		arm_vupysk = self.Arm_vupysk_check.IsChecked
		exit_error = False
		if not isinstance(curview, ViewSheet):
			exit_error = True
			TaskDialog.Show('error', 'Зайдіть на аркуш')
		t=Transaction(doc, 'Відомості')
		t.Start()
		position_list = []
		if status == 'refresh':

			els = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]

			if len(els) > 0:
				if str(els[0].Category.Id) == '-2000510':
					detail_create = doc.GetElement(els[0].ViewId)

					filter_status = '0'
					for e in FilteredElementCollector(doc, detail_create.Id).OfCategory(BuiltInCategory.OST_DetailComponents).WhereElementIsNotElementType().ToElements():
						e_type = doc.GetElement(e.GetTypeId())
						det_fam_name = e_type.get_Parameter(BuiltInParameter.ALL_MODEL_FAMILY_NAME).AsString()
						if det_fam_name == 'Дет0':
							#newdet=doc.Create.NewFamilyInstance(XYZ(0,0,0), r0, detail_create)
							filter_status = e.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).AsString()

						else:
							num_mark = e.LookupParameter('Арм_Марка').AsString()
							if len(str(num_mark))==1: #додам 0 в марки від 1 до 9 для сортування
								num_mark=str('0'+ num_mark)
							position_list.append([e.Location.Point, num_mark])
							doc.Delete(e.Id)
					#print(filter_status)
					if len(filter_status.split("*/")) >= 3:
						filter_type = filter_status.split('*/')[1]
						one_cons = filter_status.split('*/')[2]
						s_filter = filter_status.split('*/')[0]
						arm_vupysk = 'False'
					if len(filter_status.split("*/")) == 4:
						arm_vupysk = filter_status.split('*/')[3]
					if filter_status == '0':
						exit_error = True
						TaskDialog.Show('error', 'Не задані параметри сімейства')
					#TaskDialog.Show('1', )
				else:
					TaskDilog.Show('error', 'Виберіть видовий екран на аркуші')
					exit_error = True
			else:
				TaskDialog.Show('error', 'Виберіть відомість деталей')
				exit_error = True


		if not exit_error:
			rebar_list=[]
			rebar_shapes=[]
			rebar_type=[]
			rebar_mark=[]
			rebar_osn=[]
			#armA_l=[]
			#armB_l=[]
			#armV_l=[]
			#armG_l=[]
			#armK_l=[]
			result=[]
			#TaskDialog.Show('3',s_filter)
			rebar_filter = ElementCategoryFilter(BuiltInCategory.OST_Rebar)

			rebars = FilteredElementCollector(doc).WherePasses(rebar_filter).WhereElementIsNotElementType().ToElements()
			det_comp = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DetailComponents).WhereElementIsElementType().ToElements()
			sheets = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType().ToElements()

			wall = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]

			name_wall=s_filter#wall[0].LookupParameter('Мрк.МаркаКонструкции').AsString()

			list_names=[]
			arm_a_set=0
			arm_b_set=0
			arm_v_set=0
			arm_g_set=0
			arm_d_set=0
			arm_e_set=0
			arm_j_set=0
			arm_mark=0
			arm_alpha=0

			def arm_param(name, i):
				global arm_a_set, arm_b_set, arm_v_set, arm_g_set, arm_d_set, arm_e, arm_j, arm_mark, arm_alpha
				arm_mark=i[3]
				arm_a_set=i[4]
				arm_b_set=i[5]
				arm_v_set=i[6]
				arm_g_set=i[7]
				arm_d_set=i[8]
				arm_e_set=i[9]
				arm_j_set=i[10]
				arm_alpha=i[11]
			def det_line(det_name):
				for det in det_comp:
					det_r = det.get_Parameter(BuiltInParameter.ALL_MODEL_FAMILY_NAME)
					name = det_r.AsString()
					list_names.append(name)
					if name==det_name:
						detail_line=det
						break
				try:
					return detail_line
				except:
					return 0

			if len(s_filter)==0 and status != 'refresh': #якщо немає фільтру
				ids = uidoc.Selection.GetElementIds()
				if isinstance(ids, list) == True:
					ids=[ids]
				list=[]
				for id in ids:
					el = doc.GetElement(id)
					name = el.GetType().Name
					#stage = el.get_Parameter(BuiltInParameter.PHASE_CREATED)
					#stage_name = stage.AsString()
					if name!="Rebar":
						list.append(id)

				list1 = List[ElementId]()
				for rebar in rebars:
					try:
						el_id = rebar.GetHostId()
					except:
						0
					for id in list:
						if id==el_id:
							list1.Add(rebar.Id)
				rebars_1 = uidoc.Selection.SetElementIds(list1)

				#----------------------------------------------------------

				rebars = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]
			else:	#якщо заданий фільтр
				rebar_f = []
				#TaskDialog.Show('1', str(s_filter))
				for rebar in rebars:
					#try:
					r_type = doc.GetElement(rebar.GetTypeId())
					family = r_type.LookupParameter('Арм.ВыполненаСемейством').AsValueString()
					#except:
					#	0#family = rebar.LookupParameter('Арм.ВыполненаСемейством').AsValueString()

					if family == 'Нет':
						if filter_type == 'marka':
							mitka = rebar.get_Parameter(BuiltInParameter.REBAR_ELEM_HOST_MARK).AsString()

						elif filter_type == 'mrkcon':
							mitka = rebar.LookupParameter('Мрк.МаркаКонструкции').AsString()
						elif filter_type == 'mrkizd':
							mitka = rebar.LookupParameter('Мрк.МаркаИзделия')
							if mitka != None:
								mitka = mitka.AsString()
							else:
								mitka = None
					else:
						if filter_type == 'marka':
							mitka = rebar.LookupParameter('Мрк.МаркаКонструкции').AsString()
						elif filter_type == 'mrkcon':
							mitka = rebar.LookupParameter('Мрк.МаркаКонструкции').AsString()
						elif filter_type == 'mrkizd':
							mitka = rebar.LookupParameter('Мрк.МаркаИзделия')
							if mitka != None:
								mitka = mitka.AsString()
							else:
								mitka = None
					stage = rebar.get_Parameter(BuiltInParameter.PHASE_CREATED)
					stage_name = stage.AsValueString()
					#print(one_cons)
					arm_pruzn = rebar.LookupParameter('Арм.Призначення')
					#print(1)
					if arm_pruzn != None and arm_pruzn != 'None':
						arm_pruzn = arm_pruzn.AsString()
					else:
						arm_pruzn = 'ran'
						#arm_vupysk = False
					if one_cons == True or one_cons == 'True':
						#print(3)

						if mitka == s_filter and stage_name == 'Підрахунок на 1 конструкцію':
							if arm_vupysk == 'True' or arm_vupysk == True:
								if str(arm_pruzn).lower() != 'випуски':
									#print(2)
									rebar_f.append(rebar)
							else:
								rebar_f.append(rebar)
							#print(4)
					else:
						if mitka == s_filter:
							#try:
							if arm_vupysk == 'True' or arm_vupysk == True:
								if str(arm_pruzn).lower() != 'випуски':

									rebar_f.append(rebar)
								#else:
								#    print(arm_pruzn)
							else:
								rebar_f.append(rebar)
							#except:
							#    0
				rebars=rebar_f
			mark_list=[]

			#TaskDialog.Show('1', str(len(rebars)))
			for rebar in rebars:

				try:
					try: #системна арматура
						sh=rebar.get_Parameter(BuiltInParameter.REBAR_SHAPE).AsValueString()
						if ' ' in sh:
							sh = sh.split(' ')[0]
							#print(sh)
						type = rebar.get_Parameter(BuiltInParameter.REBAR_BAR_DIAMETER).AsValueString()
						type=type.split(' ')[0]
						mark = rebar.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).AsString()
						#print(mark)
						#mark_list.append(mark)
						if len(str(mark))==1: #додам 0 в марки від 1 до 9 для сортування
							mark=str('0'+ mark)
						#print('+')
						#print(mark)

					except: #IFC арматура
						sh = rebar.LookupParameter('Арм.Форма').AsString()
						type = rebar.LookupParameter('Рзм.Диаметр').AsString()
						mark = rebar.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).AsString()
						if len(str(mark))==1: #додам 0 в марки від 1 до 9 для сортування
							mark=str('0'+ mark)
					try:
						armA = str(int(5*(round(int(rebar.LookupParameter('Арм_А').AsValueString())/5))))
						#armA_l.append(armA)
					except:
						armA = '0'
					try:
						armB = str(int(5*(round(int(rebar.LookupParameter('Арм_Б').AsValueString())/5))))
						#armB_l.append(armB)
					except:
						armB='0'
						#armB_l.append('0')
					try:
						armV = str(int(5*(round(int(rebar.LookupParameter('Арм_В').AsValueString())/5))))
					except:
						armV='0'
						#armV_l.append('0')
					try:
						armG = str(int(5*(round(int(rebar.LookupParameter('Арм_Г').AsValueString())/5))))
						if sh=='26':
							armG = str(int(1*(round(int(rebar.LookupParameter('Арм_Г').AsValueString())/1))))
							armG=str(int(float(armG)-float(type)))
					except:
						armG='0'
						#armG_l.append('0')
					try:
						armD = str(int(5*(round(int(rebar.LookupParameter('Арм_Д').AsValueString())/5))))
					except:
						armD = '0'
					try:
						armE = str(int(5*(round(int(rebar.LookupParameter('Арм_E').AsValueString())/5))))
					except:
						armE = '0'
					try:
						armJ = str(int(5*(round(int(rebar.LookupParameter('Арм_Ж').AsValueString())/5))))
					except:
						armJ = '0'

					try:
						armAlpha = rebar.LookupParameter('Арм.РазмерAlpha').AsValueString()
						armAlpha = armAlpha.split(' ')[0]
					except:
						armAlpha = '0'
						#armG_l.append('0')
					if mark not in mark_list:
						#print(mark)
						result.append([rebar, sh, type, mark, armA, armB,armV,armG, armD, armE, armJ, armAlpha])
						#TaskDialog.Show('1', str(arm_mark))
						mark_list.append(mark)
				except:
					0
			new_rebar_list =[]
			mark_list=[]
			#TaskDialog.Show('Done', str('Успішно створено'))

			result = [x for x in result if x[1] != '01'] #видаллення прямих стрижнів зі списку
			result_f = []
			#TaskDialog.Show('1', str(len(result)))
			for sublist in result: #вилаляю дублікати
				if sublist not in result_f:
					if sublist[3] not in mark_list:
						mark_list.append(sublist[3])
						result_f.append(sublist)
			result_f.sort(key=lambda x: x[3])#сортування списку арматури по марці


			count_1 = 0
			x_change_pos = []
			for p in position_list:
				if round(position_list[count_1][0].X, 5) != round(position_list[count_1-1][0].X, 5):
					x_change_pos.append(count_1)
				count_1 += 1
			count_1 = 0
			final_position_list = []
			x_pos = 0
			y_pos = -240/304.8
			for p in position_list:
				if count_1 == 0:
					final_position_list.append(XYZ(0, y_pos, 0))
				else:
					if count_1 not in x_change_pos:
						y_pos -= 240/304.8
						final_position_list.append(XYZ(x_pos, y_pos, 0))
					else:
						y_pos = -240/304.8
						x_pos += 870/304.8
						final_position_list.append(XYZ(x_pos, y_pos, 0))

				count_1 += 1
			count_position = 0
			if len(final_position_list) == 0:
				final_position_list.append(XYZ(0, -240/304.8, 0))

			#TaskDialog.Show('Done', str(result_f))
			for i in result_f: #прибираю нулі з марок від 1 до 9
				if i[3] != None:
					s = i[3]
					s = [c for c in s]
					#i[3]=i[3]+s[0]
					if s[0]=='0':
						s.pop(0)
						i[3]=s[0]
			detail_det_k = None
			views = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).WhereElementIsNotElementType().ToElements()
			for x in views:
				name_x = x.get_Parameter(BuiltInParameter.VIEW_NAME).AsString()
				#list_schedules.append(name_s)
				if name_x == "КБ1.-3100.Колона К1.1 Деталі":
					detail_det_k = x

			#Створюю відомість деталей креслярський вид----------
			if len(s_filter) == 0:
				view_num = curview.get_Parameter(BuiltInParameter.VIEWPORT_SHEET_NUMBER).AsString()
			else:
				view_num = curview.get_Parameter(BuiltInParameter.SHEET_NUMBER).AsString()
			for sheet in sheets:
				sheet_num = sheet.get_Parameter(BuiltInParameter.SHEET_NUMBER).AsString()
				if view_num == sheet_num:
					sheet_id = sheet
					break
			if status == 'create':
				detail_det_k_new = detail_det_k.Duplicate(ViewDuplicateOption.Duplicate)
				detail_create = doc.GetElement(detail_det_k_new)

			#---------------------------------------------------
			#створюю поля на креслярському виді відомості деталі
			h_line = 240/304.8
			r0=det_line('Дет0')

			"""
			if self.radio_1.IsChecked:
				filter_type = 'marka'
			elif self.radio_2.IsChecked:
				filter_type = 'mrk_con'
			elif self.radio_3.IsChecked:
				filter_type = 'mrk_izd'
			"""
			r0.Activate()
			doc.Regenerate()
			if status == 'create':
				newdet = doc.Create.NewFamilyInstance(XYZ(0,0,0), r0, detail_create)
				r0_comment = newdet.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
				r0_comment.Set(('{}*/{}*/{}*/{}').format(s_filter, filter_type, one_cons, arm_vupysk))

			count = a_1+b_1
			result_det = []

			for r in result_f:

				result_det.append(r)
				forma = r[1]
				r1 = det_line('Shape_'+ forma)
				if r1 != 0:
					r1.Activate()
					doc.Regenerate()
					#arm_param('Shape_'+ forma, r)
					#TaskDialog.Show('Done', '1')
					if status == 'create':
						newdet = doc.Create.NewFamilyInstance(XYZ(0,-h_line,0), r1, detail_create)
					else:
						if len(final_position_list) <= count_position: #якщо список закінчився додаю по У нову координату
							old_xyz = final_position_list[count_position-1]
							new_xyz = XYZ(old_xyz.X, old_xyz.Y - 240/304.8, old_xyz.Z)
							final_position_list.append(new_xyz)
						newdet = doc.Create.NewFamilyInstance(final_position_list[count_position], r1, detail_create)

					h_line+=240/304.8
					arm_mark=r[3]
					#TaskDialog.Show('Done', '2')
					try:
						prefix = r[0].LookupParameter('Арм.ПрефиксФормы')
						if prefix != None:
						    prefix = prefix.AsString()
						    arm_mark = prefix+arm_mark
					except:
						0
					arm_a_set=r[4]
					arm_b_set=r[5]
					arm_v_set=r[6]
					arm_g_set=r[7]
					arm_d_set=r[8]
					arm_e_set=r[9]
					arm_j_set=r[10]
					arm_alpha=r[11]
					try:
						arm_det = newdet.LookupParameter('АрмА')
						arm_det.Set(arm_a_set)
					except:
						0
					try:
						arm_det = newdet.LookupParameter('АрмБ')
						arm_det.Set(arm_b_set)
					except:
						0
					try:
						arm_det = newdet.LookupParameter('АрмВ')
						arm_det.Set(arm_v_set)
					except:
						0
					try:
						arm_det = newdet.LookupParameter('АрмГ')
						arm_det.Set(arm_g_set)
					except:
						0
					try:
						arm_det = newdet.LookupParameter('АрмД')
						arm_det.Set(arm_d_set)
					except:
						0
					try:
						arm_det = newdet.LookupParameter('АрмЕ')
						arm_det.Set(arm_e_set)
					except:
						0
					try:
						arm_det = newdet.LookupParameter('АрмЖ')
						arm_det.Set(arm_j_set)
					except:
						0
					try:
						arm_det = newdet.LookupParameter('Арм_Марка')
						arm_det.Set(str(arm_mark))
					except:
						0
					result_det=[]

				else:
					print('Невірно задана форма, марка стрижня '+r[3])
				count_position+=1

			if status == 'create':
				d_k = Viewport.Create(doc, sheet_id.Id, detail_det_k_new, XYZ(0,0,0))
				d_k_name = doc.GetElement(detail_det_k_new).get_Parameter(BuiltInParameter.VIEW_NAME)
				d_k_name.Set(s_name.split('*/')[2] + '_Відомість деталей')
				d_k_tom = doc.GetElement(detail_det_k_new).LookupParameter("Орг.КомплектКреслень")
				if d_k_tom != None:
					d_k_tom.Set(s_name.split('*/')[0])
				d_k_tom2 = doc.GetElement(detail_det_k_new).LookupParameter("Орг.Відмітка")
				if d_k_tom2 != None:
					d_k_tom2.Set(s_name.split('*/')[1])
			t.Commit()
		else:
			t.RollBack()

	def print_mes(self):
		TaskDialog.Show('1','1')

	def Button_Ok(self, sender, e):
		try:
			customizable_event.raise_event(self.create_detail, ['create'])
		except:
			TaskDialog.Show('error','error')

	def Button_Refresh(self, sender, e):
		try:
			customizable_event.raise_event(self.create_detail, ['refresh'])
		except:
			TaskDialog.Show('error2','error2')

	def Button_Read(self, sender, e):
		try:
			customizable_event.raise_event(self.read_filter)
		except:
			TaskDialog.Show('error3','error3')
	def Button_Write(self, sender, e):
		try:
			customizable_event.raise_event(self.write_filter)
		except:
			TaskDialog.Show('error4','error4')

	def radio_1_button(self, sender, e):
		self.radio_2.IsChecked = False
		self.radio_3.IsChecked = False

	def radio_2_button(self, sender, e):
		self.radio_1.IsChecked = False
		self.radio_3.IsChecked = False

	def radio_3_button(self, sender, e):
		self.radio_1.IsChecked = False
		self.radio_2.IsChecked = False
# Let's launch our beautiful and useful form !
#print(1)
modeless_form = ModelessForm("interface.xaml")




