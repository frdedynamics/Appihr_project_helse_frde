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
from os import chdir, mkdir, listdir, path
import re

from datetime import datetime

from PyQt5.QtWidgets import QWidget # for split string with multiple delimiters
from Classes.threshold_selection_window import Ui_Dialog as ThresholdSelectionDialog

PKG_PATH = str(Path(QDir.currentPath()).parents[0])

class ThresholdSelection(QWidget, ThresholdSelectionDialog):
    def __init__(self, parent=None):
        super(ThresholdSelection, self).__init__(parent)
        self.setupUi(self)

        self.comboBox_th.setEnabled(False)
        self.button_assign.clicked.connect(self.create_new_th_data)
        self.button_load_older_data.clicked.connect(self.list_data)
        self.comboBox_th.currentTextChanged.connect(self.get_old_th_data)
        self.patient = None
        self.files_dict = {}

    
    def list_data(self):
        self.comboBox_th.setEnabled(True)
        self.comboBox_th.clear()
        print(self.patient)
        patient_path = PKG_PATH+'/test_users/'+self.patient
        chdir(patient_path)
        files = listdir(patient_path)
        sorted_files = sorted(files, key=lambda x: path.getmtime(path.join(patient_path, x)), reverse=True)

        # This is only for better visuals. Remove if not needed.
        for file in sorted_files:
            # Extract date and time using regex pattern
            pattern = r"thresholds(\d{2}-\d{2}-\d{4}-\d{2}-\d{2})"
            match = re.search(pattern, file)

            if match:
                datetime_str = match.group(1)  # Get the matched date and time string
                datetime_obj = datetime.strptime(datetime_str, "%d-%m-%Y-%H-%M")  # Convert string to datetime object
                formatted_datetime = datetime_obj.strftime("%d.%m.%Y %H:%M")  # Format datetime object
                print("Formatted Datetime:", formatted_datetime)
                self.comboBox_th.addItem(formatted_datetime)
                self.files_dict[formatted_datetime] = file
            else:
                print("Completed or No match found.")
            
        print(self.files_dict.keys())

        #TODO:Get the filename of the newest file and select the newest as default
        # newest_file = sorted_files[0] if sorted_files else None
        # print("Newest file:", newest_file)
        

    
    def get_old_th_data(self):
        filename = self.files_dict[self.comboBox_th.currentText()]
        # Variables to store the values
        shoulder_extension_flexion = None
        shoulder_pan_adduction_abduction = None
        internal_rotation = None
        external_rotation = None

        # Read the file and process each line
        with open(filename, "r") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()  # Remove leading/trailing whitespace
                key, value = line.split(":")  # Split line into key and value

                # Assign value to the respective variable
                if key == "Shoulder extension/flexion":
                    shoulder_extension_flexion = int(value)
                    self.lineEdit_shoulder_ext_flex.setText(value)
                elif key == "Shoulder pan adduction/abduction":
                    shoulder_pan_adduction_abduction = int(value)
                    self.lineEdit_shoulder_abd_add.setText(value)
                elif key == "Internal rotation":
                    internal_rotation = int(value)
                    self.lineEdit_intern_rot.setText(value)
                elif key == "External rotation":
                    external_rotation = int(value)
                    self.lineEdit_extern_rot.setText(value)


    def create_new_th_data(self):
        #TODO: make sure the lineedits are there for thresholds
        #TODO: move datetime to previous window.
        current_time = datetime.now().strftime("%d-%m-%Y-%H-%M") 
        filename = 'thresholds'+current_time+'.yaml'
        proc = subprocess.Popen(['touch', filename], stdout=subprocess.PIPE)

        with open(filename, "w") as file:
            data = {"Shoulder extension/flexion": self.lineEdit_shoulder_ext_flex.text(),
                    "Shoulder pan adduction/abduction": self.lineEdit_shoulder_abd_add.text(),
                    "Internal rotation": self.lineEdit_intern_rot.text(),
                    "External rotation": self.lineEdit_extern_rot.text()}

            # Write each line in dictionary form to the file
            for key, value in data.items():
                line = f"{key}: {value}\n"
                file.write(line)
        print("done")
