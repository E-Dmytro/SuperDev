# -*- coding: utf-8 -*-

__title__ = "Select Folder"
__author__ = "Dmytro Kh"
__doc__ = """Version = 1.2
Date    = 12.01.2024
____________________________________________________
"""


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ==================================================
from Autodesk.Revit.DB import (View,

                               ViewDuplicateOption,
                               Transaction,
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
from System.Windows.Forms import (DialogResult,
                                  MessageBox,
                                  MessageBoxButtons,
                                  OpenFileDialog,
                                  FolderBrowserDialog)
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


import clr
import sys
import os





class MyWindow(WPFWindow):
    """The dialog box that controls the whole script."""


    def __init__(self, xaml_file_name):
        self.form = WPFWindow.__init__(self, xaml_file_name)
        self.main_title.Text = __title__
        self.selected_views = get_selected_views(uidoc, exit_if_none=True, title=__title__)

        if self.selected_views:
            self.ShowDialog()



    # METHODS
    def getfilepath(self):
        """Function to duplicate views with given options.
        Possible options:
        - ViewDuplicateOption.Duplicate,
        - ViewDuplicateOption.WithDetailing,
        - ViewDuplicateOption.AsDependent"""
        new_views = []
        # t = Transaction(doc, __title__)
        # t.Start()
        try:
            # >>>>>>>>>> CHOOSE DIR
            fileDialog = FolderBrowserDialog()
            fileDialog.Description = "Select a folder."
            fileDialog.ShowDialog()

            # >>>>>>>>>> SELECTED PATH
            dir_selected = fileDialog.SelectedPath
            if not dir_selected:
                alert("No folder was selected!\n Please try again.", title=__title__, exitscript=True)
            else:
                return dir_selected
                # print("Selected folder: " + dir_selected)

        except:
            return None

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
        # self.getfilepath()


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================
# if __name__ == '__main__':
#     getdirectory = MyWindow("ScriptPath.xaml")
#     if getdirectory==None:
#         directory = os.path.join("C:\\", "Users", "user1", "Desktop", "Excel")
#
#         # Create the directory if it doesn't exist
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     else:
#         directory = os.path.join(getdirectory, "Excel")
#         # Now you can use 'directory' in your script
#         print(directory)
# if __name__ == '__main__':
#     window = MyWindow("ScriptPath.xaml")
#     getdirectory = window.getfilepath()  # Call getfilepath on the MyWindow instance
#     if getdirectory is None:
#         try:
#             directory = os.path.join("C:\\", "Users", "user1", "Desktop", "Excel")
#         except:
#             os.makedirs(directory)
#     else:
#         directory = os.path.join(getdirectory, "Excel")
#
#     # Now you can use 'directory' in your script
#     print(directory)