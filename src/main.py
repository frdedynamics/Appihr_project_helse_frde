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
from os import chdir, mkdir, getcwd
from time import sleep

from PyQt5.QtWidgets import QWidget # for split string with multiple delimiters

from Classes.main_window import Ui_MainWindow
from Classes.first_patient_selection import Ui_Dialog as PatientSelectionDialog #TODO: remove
from Classes.new_patient import Ui_Dialog as CreateNewPatientDialog #TODO: remove

from Classes.gui_node_class import GUInode

from Classes.AddToExistingPatient import AddToExistingPatient
from Classes.ThresholdSelection import ThresholdSelection
from Classes.RealTimeMeasurement import RealTimeMeasurement

PKG_PATH = str(Path(QDir.currentPath()).parents[0])


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

        self.pkg_path = Path(QDir.currentPath()).parents[0]  ##(?) QDir() instead? check later
        self.launch = roslaunch.scriptapi.ROSLaunch()
        # Might need 2 separate timers because they block each other when the visualization is involved.
        self.ros_node = GUInode()
        self.rosTimer = QTimer() ## Simply ROS rate -- frequency of the ROS Node
        self.rosTimer.timeout.connect(self.ros_node.update)

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

        self.Dialog.show() ## This is needed because this one create a NEW dialog. Not only changing UI.


    def start_threshold_window(self):
        #self.patient = self.addToPatientTool.selected_patient
        self.patient = "gizem"
        print("Threshold selection started. Patient: ", self.patient)
        self.ThresholdSelection = ThresholdSelection(self)
        self.ThresholdSelection.patient = self.patient ## A bit ambigius but fix later if needed.
        self.setCentralWidget(self.ThresholdSelection)
        self.setWindowTitle("Threshold Selection")

        self.ThresholdSelection.button_assign.clicked.connect(self.start_measurement_window)
        self.ThresholdSelection.button_back.clicked.connect(self.add_to_existing_patient)



    def start_measurement_window(self):
        print("Measurement started")
        self.MeasurementTool = RealTimeMeasurement(self)
        self.setCentralWidget(self.MeasurementTool)
        self.setWindowTitle("Measurement")
        self.resize(947, 600)

        self.MeasurementTool.button_back.clicked.connect(self.start_threshold_window)
        self.MeasurementTool.button_start_sensor.clicked.connect(self.start_awindamonitor)


    def start_awindamonitor(self):
        chdir(PKG_PATH+"/launch/")
        print(getcwd())
        self.rosTimer.start(10)        
        self.ros_node.init_subscribers_and_publishers()
        self.start_single_roslaunch('/launch/gui.launch') # I need this to set a UUID for later added nodes
        sleep(1)

        # Start marker publisher node
        # self.add_rosnode("appirh_project_helse_frde", "visualize_angles.py", "visualize_angles") 

        # Start Awindamonitor
        self.add_rosnode("awindamonitor", "awindamonitor", "awindamonitor")

        self.human_proc = subprocess.Popen(["sh", "sh/human.sh"]) ## Otherway halts the system. You need to use Popen: https://stackoverflow.com/questions/16855642/execute-a-shell-script-from-python-subprocess


    def start_single_roslaunch(self, name):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        self.launch.parent = roslaunch.parent.ROSLaunchParent(uuid, [str(self.pkg_path)+name])
        self.launch.start()


    def add_rosnode(self, pkg_name, node_name, name, args=None, respawn=True):
        node = roslaunch.core.Node(pkg_name, node_name, name, args)
        self.launch.launch(node)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())