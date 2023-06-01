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

from Classes.main import Ui_MainWindow
from Classes.first_patient_selection import Ui_Dialog as PatientSelectionDialog

class PatientSelection(QWidget, PatientSelectionDialog):
    def __init__(self, parent=None):
        super(PatientSelection, self).__init__(parent)
        self.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(492, 377)

        self.startPatientSelectionWindow()

    
    def startPatientSelectionWindow(self):
        self.PatientSelection = PatientSelection(self)
        self.setCentralWidget(self.PatientSelection)
        self.setWindowTitle("Select Patient")

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())