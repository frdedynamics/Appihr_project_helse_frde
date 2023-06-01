# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 220, 321, 131))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 141, 17))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 141, 17))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(170, 40, 121, 26))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit.setGeometry(QtCore.QRect(170, 70, 121, 26))
        self.timeEdit.setObjectName("timeEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 391, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(60, 70, 41, 17))
        self.label.setObjectName("label")
        self.comboBox_userlist = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_userlist.setGeometry(QtCore.QRect(120, 60, 131, 25))
        self.comboBox_userlist.setObjectName("comboBox_userlist")
        self.button_continue = QtWidgets.QPushButton(self.groupBox_2)
        self.button_continue.setGeometry(QtCore.QRect(250, 60, 89, 25))
        self.button_continue.setObjectName("button_continue")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 271, 17))
        self.label_4.setObjectName("label_4")
        self.button_new_user = QtWidgets.QPushButton(self.groupBox_2)
        self.button_new_user.setGeometry(QtCore.QRect(200, 90, 141, 41))
        self.button_new_user.setObjectName("button_new_user")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 280, 141, 61))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Appointment"))
        self.label_3.setText(_translate("MainWindow", "Appointment Time:"))
        self.label_2.setText(_translate("MainWindow", "Appointment Date:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "User"))
        self.label.setText(_translate("MainWindow", "User:"))
        self.button_continue.setText(_translate("MainWindow", "Continue"))
        self.label_4.setText(_translate("MainWindow", "Please select a user or create new user"))
        self.button_new_user.setText(_translate("MainWindow", "Create new user"))
        self.pushButton.setText(_translate("MainWindow", "> Next (Progress)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
