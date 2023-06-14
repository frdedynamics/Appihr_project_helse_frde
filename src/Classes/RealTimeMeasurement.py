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
from Classes.real_time_measurement_window import Ui_Dialog as RealTimeMeasurementDialog

PKG_PATH = str(Path(QDir.currentPath()).parents[0])

class RealTimeMeasurement(QWidget, RealTimeMeasurementDialog):
    def __init__(self, parent=None):
        super(RealTimeMeasurement, self).__init__(parent)
        self.setupUi(self)

        print("here")