#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typing
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import re

from PyQt5.QtWidgets import QWidget # for split string with multiple delimiters

from Classes.main_window import Ui_MainWindow
from Classes.first_patient_selection import Ui_Dialog as PatientSelectionDialog
from Classes.new_patient import Ui_Dialog as CreateNewPatientDialog
from Classes.add_to_existing_patient import Ui_Dialog as AddToExistingPatientDialog

class PatientSelection(QWidget, PatientSelectionDialog):
    def __init__(self, parent=None):
        super(PatientSelection, self).__init__(parent)
        self.setupUi(self)

class CreateNewPatient(QWidget, CreateNewPatientDialog):
    def __init__(self, parent=None):
        super(CreateNewPatient, self).__init__(parent)
        self.setupUi(self)

class AddToExistingPatient(QWidget, AddToExistingPatientDialog):
    def __init__(self, parent=None):
        super(AddToExistingPatient, self).__init__(parent)
        self.setupUi(self)
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(492, 377)
        self.setupUi(self)
        self.setWindowTitle("APPIRH Demo")
        self.Dialog = QDialog()

        self.button_record_data.clicked.connect(self.start_patient_selection_window)

        self.show()

    
    def start_patient_selection_window(self):
        self.PatientSelection = PatientSelection(self)
        self.setCentralWidget(self.PatientSelection)
        self.setWindowTitle("Select Patient")

        self.PatientSelection.button_addPatient.clicked.connect(self.add_to_existing_patient)
        self.PatientSelection.button_newPatient.clicked.connect(self.create_new_patient)

        self.show()


    def add_to_existing_patient(self):
        print("add")
        self.addToPatientTool = AddToExistingPatient(self)
        self.setCentralWidget(self.addToPatientTool)
        self.setWindowTitle("Add to Existing Patient")

        self.addToPatientTool.button_back.clicked.connect(self.start_patient_selection_window)

    def create_new_patient(self):  ## opens new patient creation dialog
        print("create")
        self.newPatientTool = CreateNewPatient(self)
        self.newPatientTool.setupUi(self.Dialog)
        self.Dialog.setWindowTitle("New Patient")
        self.Dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())