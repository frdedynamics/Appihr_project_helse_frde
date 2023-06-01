# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/add_to_existing_patient.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(100, 20, 391, 171))
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
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 200, 321, 131))
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
        self.button_next = QtWidgets.QPushButton(Dialog)
        self.button_next.setGeometry(QtCore.QRect(400, 240, 141, 61))
        self.button_next.setObjectName("button_next")
        self.button_back = QtWidgets.QPushButton(Dialog)
        self.button_back.setGeometry(QtCore.QRect(0, 0, 89, 25))
        self.button_back.setObjectName("button_back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "User"))
        self.label.setText(_translate("Dialog", "User:"))
        self.button_continue.setText(_translate("Dialog", "Continue"))
        self.label_4.setText(_translate("Dialog", "Please select a user or create new user"))
        self.groupBox.setTitle(_translate("Dialog", "Appointment"))
        self.label_3.setText(_translate("Dialog", "Appointment Time:"))
        self.label_2.setText(_translate("Dialog", "Appointment Date:"))
        self.button_next.setText(_translate("Dialog", "> Next (Progress)"))
        self.button_back.setText(_translate("Dialog", "< Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
