#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typing
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import re
import rospy, roslaunch
import subprocess, time
from pathlib import Path
from os import chdir, mkdir

from PyQt5.QtWidgets import QWidget # for split string with multiple delimiters

from Classes.main_window import Ui_MainWindow
from Classes.first_patient_selection import Ui_Dialog as PatientSelectionDialog #TODO: remove
from Classes.new_patient import Ui_Dialog as CreateNewPatientDialog #TODO: remove

from Classes.AddToExistingPatient import AddToExistingPatient
from Classes.ThresholdSelection import ThresholdSelection


# TODO: Put these classes into separate files as the project expands (like AddToExistingPatient.py)
class PatientSelection(QWidget, PatientSelectionDialog):
    def __init__(self, parent=None):
        super(PatientSelection, self).__init__(parent)
        self.setupUi(self)

class CreateNewPatient(QWidget, CreateNewPatientDialog):
    def __init__(self, parent=None):
        super(CreateNewPatient, self).__init__(parent)
        self.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(492, 377)
        self.setupUi(self)
        self.setWindowTitle("APPIRH Demo")
        self.Dialog = QDialog()

        self.button_record_data.clicked.connect(self.start_patient_selection_window)

        self.patient = None

        self.start_threshold_window()  ## FOR DEBUG ONLY
        self.show()

    
    def start_patient_selection_window(self):
        self.PatientSelection = PatientSelection(self)
        self.setCentralWidget(self.PatientSelection)
        self.setWindowTitle("Select Patient")

        self.PatientSelection.button_addPatient.clicked.connect(self.add_to_existing_patient)
        self.PatientSelection.button_newPatient.clicked.connect(self.create_new_patient)

        self.show()        


    def add_to_existing_patient(self):
        print("Add data to existing patient")
        self.addToPatientTool = AddToExistingPatient(self)
        self.setCentralWidget(self.addToPatientTool)
        self.setWindowTitle("Add to Existing Patient")

        self.addToPatientTool.button_back.clicked.connect(self.start_patient_selection_window)
        self.addToPatientTool.button_next.clicked.connect(self.start_threshold_window)

    def create_new_patient(self):  ## opens new patient creation dialog
        print("Create new patient")
        self.newPatientTool = CreateNewPatient(self)
        self.newPatientTool.setupUi(self.Dialog)
        self.Dialog.setWindowTitle("New Patient")

        #TODO: add actions.

        self.Dialog.show()


    def start_threshold_window(self):
        #self.patient = self.addToPatientTool.selected_patient
        self.patient = "gizem"
        print("Threshold selection started. Patient: ", self.patient)
        self.ThresholdSelection = ThresholdSelection(self)
        self.ThresholdSelection.patient = self.patient ## A bit ambigius but fix later if needed.
        self.setCentralWidget(self.ThresholdSelection)
        self.setWindowTitle("Threshold Selection")



    def start_measurement_window(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())