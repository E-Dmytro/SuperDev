# -*- coding: utf-8 -*-

__title__ = "From Schedule to Excel"
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
                               ElementId)
# pyRevit
from pyrevit.forms import WPFWindow, alert

# Custom imports
from Snippets._selection import get_selected_views


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

import re
import clr
import sys
import os

from ScriptPath import (MyWindow)  # replace 'your_script' with the name of your script file

# Instantiate the MyWindow class

# Call the getfilepath method
dir_selected = MyWindow("ScriptPath.xaml").getfilepath()

# If no directory is selected, use the default directory
if dir_selected is None:
    directory = os.path.join("C:\\", "Users", "user1", "Desktop", "Excel")
else:
    directory = os.path.abspath(dir_selected)

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# print("The directory used is" + {directory})





class MyWindow(WPFWindow):
    """The dialog box that controls the whole script."""

    VIEW_TYPES = [ViewPlan, ViewSection, View3D,ViewSchedule, View]

    def __init__(self, xaml_file_name):
        self.form = WPFWindow.__init__(self, xaml_file_name)
        self.main_title.Text = __title__
        self.selected_views = get_selected_views(uidoc, exit_if_none=True, title=__title__)

        if self.selected_views:
            self.ShowDialog()



    # METHODS
    def duplicate_selected_views(self):
        """Function to duplicate views with given options.
        Possible options:
        - ViewDuplicateOption.Duplicate,
        - ViewDuplicateOption.WithDetailing,
        - ViewDuplicateOption.AsDependent"""
        new_views = []
        # t = Transaction(doc, __title__)
        # t.Start()
        try:

            for view in self.selected_views:
                # if doc.CanViewBeDuplicated(view):

                # Specify the directory to save the text files


                # Export each schedule to a text file

                if not view.Name:
                    continue

                # Specify the file path for each schedule
                # filepath = os.path.join(directory, view.Name + ".txt")
                # print (filepath)
                # Specify the export options
                options = ViewScheduleExportOptions()
                options.FieldDelimiter = ","
                # Replace invalid characters in view.Name with "." if they exist
                if re.search(r'[\\/*?:"<>|]', view.Name):
                    valid_view_name = re.sub(r'[\\/*?:"<>|]', '', view.Name)
                else:
                    valid_view_name = view.Name

                # Specify the file path for each schedule
                filepath = os.path.join(directory, valid_view_name + ".txt")
                print(filepath)
                # Export the schedule
                view.Export(directory, valid_view_name + ".txt", options)
                view.Export(directory, valid_view_name + ".csv", options)
                # # Export the schedule
                # view.Export(directory, view.Name + ".txt", options)
                # view.Export(directory, view.Name + ".csv", options)


                # LEGENDS
                if view.ViewType == ViewType.Legend:
                    alert("Value error: Wrong View.\nPlease, try again.", exitscript=True, title=__title__)
                    # for i in range(self.count):
                    #     view.Duplicate(ViewDuplicateOption.WithDetailing)


                # REGULAR VIEWS
                # else:

                    # for i in range(self.count):
                    #     alert("Value error: Wrong View.\nPlease, try again.", exitscript=True, title=__title__)
                        # new_view = view.Duplicate(options)
                        # new_views.append(new_view)
        except:
            pass

        if new_views:
            uidoc.Selection.SetElementIds(List[ElementId]([]))
            uidoc.Selection.SetElementIds(List[ElementId](new_views))
        # t.Commit()


#____________________________________________________________________ PROPERTIES

    # GUI INPUTS
    @property
    def count(self):
        try:
            return int(self.duplicate_count.Text)
        except:
            alert("Value error: Duplicate_count input should only contain integers.\nPlease, try again.", exitscript=True, title=__title__)

    # GUI EVENT HANDLERS:
    def button_close(self,sender,e):
        """Stop application by clicking on a <Close> button in the top right corner."""
        self.Close()

    def Hyperlink_RequestNavigate(self, sender, e):
        """Forwarding for a Hyperlink"""
        Start(e.Uri.AbsoluteUri)

    def header_drag(self,sender,e):
        """Drag window by holding LeftButton on the header."""
        if e.LeftButton == MouseButtonState.Pressed:
            DragMove(self)


    def button_run(self,sender,e):
        """Duplicate selected views and close the GUI."""
        self.Close()
        self.duplicate_selected_views()

    def button_path(self,sender,e):
        """Duplicate selected views and close the GUI."""
        self.Close()
        self.duplicate_selected_views(ViewDuplicateOption.Duplicate)

    # def button_duplicate_detailing(self,sender,e):
    #     """Duplicate selected views with detailing and close the GUI."""
    #     self.Close()
    #     self.duplicate_selected_views(ViewDuplicateOption.WithDetailing)
    #
    # def button_duplicate_dependant(self, sender, e):
    #     """Duplicate selected views as dependant and close the GUI."""
    #     self.Close()
    #     self.duplicate_selected_views(ViewDuplicateOption.AsDependent)

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================
if __name__ == '__main__':
    MyWindow("Script.xaml")
