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
from Classes.add_to_existing_patient import Ui_Dialog as AddToExistingPatientDialog

PKG_PATH = str(Path(QDir.currentPath()).parents[0])

class AddToExistingPatient(QWidget, AddToExistingPatientDialog):
    def __init__(self, parent=None):
        super(AddToExistingPatient, self).__init__(parent)
        self.setupUi(self)

        self.list_patient()

        self.comboBox_patientlist.setEnabled(True)
        self.comboBox_patientlist.setEditable(True)
        self.comboBox_patientlist.completer().setCompletionMode(QCompleter.PopupCompletion) 
        self.comboBox_patientlist.setInsertPolicy(QComboBox.NoInsert) 
        self.comboBox_patientlist.currentIndexChanged.connect(self.select_patient)

        self.button_next.clicked.connect(self.select_patient)


    def list_patient(self):
        chdir(PKG_PATH+"/test_users/")
        proc = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
        self.patient_list = []
        self.comboBox_patientlist.addItems([''])
        # print(proc.stdout.read())
        for patient in str(proc.stdout.read()).split('\\n')[1:-1]:
            patient_folder_info = re.split(r"\s+", patient)[-4:] # ['juni', '20', '23:20', '0']
            patient_info = str(patient_folder_info[3])
            self.patient_list.append(patient_info)
        self.comboBox_patientlist.addItems(self.patient_list)


    def select_patient(self):
        self.selected_patient = self.comboBox_patientlist.currentText()