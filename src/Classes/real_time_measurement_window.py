# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/real_time_measurement_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(947, 562)
        self.groupBox_prev = QtWidgets.QGroupBox(Dialog)
        self.groupBox_prev.setGeometry(QtCore.QRect(30, 190, 441, 191))
        self.groupBox_prev.setObjectName("groupBox_prev")
        self.label_3 = QtWidgets.QLabel(self.groupBox_prev)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 261, 17))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_prev)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 261, 17))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_prev)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 211, 17))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_prev)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 261, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_shoulder_ext_flex = QtWidgets.QLineEdit(self.groupBox_prev)
        self.lineEdit_shoulder_ext_flex.setGeometry(QtCore.QRect(270, 40, 113, 25))
        self.lineEdit_shoulder_ext_flex.setObjectName("lineEdit_shoulder_ext_flex")
        self.lineEdit_shoulder_abd_add = QtWidgets.QLineEdit(self.groupBox_prev)
        self.lineEdit_shoulder_abd_add.setGeometry(QtCore.QRect(270, 70, 113, 25))
        self.lineEdit_shoulder_abd_add.setObjectName("lineEdit_shoulder_abd_add")
        self.lineEdit_intern_rot = QtWidgets.QLineEdit(self.groupBox_prev)
        self.lineEdit_intern_rot.setGeometry(QtCore.QRect(270, 100, 113, 25))
        self.lineEdit_intern_rot.setObjectName("lineEdit_intern_rot")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_prev)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 130, 113, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.button_snap = QtWidgets.QPushButton(Dialog)
        self.button_snap.setGeometry(QtCore.QRect(270, 490, 121, 51))
        self.button_snap.setObjectName("button_snap")
        self.button_end_and_save = QtWidgets.QPushButton(Dialog)
        self.button_end_and_save.setGeometry(QtCore.QRect(410, 490, 131, 51))
        self.button_end_and_save.setObjectName("button_end_and_save")
        self.plainTextEdit_add_note = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_add_note.setGeometry(QtCore.QRect(30, 410, 891, 70))
        self.plainTextEdit_add_note.setObjectName("plainTextEdit_add_note")
        self.groupBox_current = QtWidgets.QGroupBox(Dialog)
        self.groupBox_current.setGeometry(QtCore.QRect(480, 190, 441, 191))
        self.groupBox_current.setObjectName("groupBox_current")
        self.label_6 = QtWidgets.QLabel(self.groupBox_current)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 261, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_current)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 261, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_current)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 211, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_current)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 261, 17))
        self.label_9.setObjectName("label_9")
        self.lineEdit_shoulder_ext_flex_2 = QtWidgets.QLineEdit(self.groupBox_current)
        self.lineEdit_shoulder_ext_flex_2.setGeometry(QtCore.QRect(270, 40, 113, 25))
        self.lineEdit_shoulder_ext_flex_2.setObjectName("lineEdit_shoulder_ext_flex_2")
        self.lineEdit_shoulder_abd_add_2 = QtWidgets.QLineEdit(self.groupBox_current)
        self.lineEdit_shoulder_abd_add_2.setGeometry(QtCore.QRect(270, 70, 113, 25))
        self.lineEdit_shoulder_abd_add_2.setObjectName("lineEdit_shoulder_abd_add_2")
        self.lineEdit_intern_rot_2 = QtWidgets.QLineEdit(self.groupBox_current)
        self.lineEdit_intern_rot_2.setGeometry(QtCore.QRect(270, 100, 113, 25))
        self.lineEdit_intern_rot_2.setObjectName("lineEdit_intern_rot_2")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_current)
        self.lineEdit_12.setGeometry(QtCore.QRect(270, 130, 113, 25))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 390, 131, 17))
        self.label.setObjectName("label")
        self.button_back = QtWidgets.QPushButton(Dialog)
        self.button_back.setGeometry(QtCore.QRect(10, 10, 89, 25))
        self.button_back.setObjectName("button_back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_prev.setTitle(_translate("Dialog", "Previous Best"))
        self.label_3.setText(_translate("Dialog", "Shoulder pan adduction/abduction:"))
        self.label_5.setText(_translate("Dialog", "External rotation:"))
        self.label_2.setText(_translate("Dialog", "Shoulder extension/flexion:"))
        self.label_4.setText(_translate("Dialog", "Internal rotation:"))
        self.button_snap.setText(_translate("Dialog", "Get a snap of \n"
" the moment"))
        self.button_end_and_save.setText(_translate("Dialog", "End and Save"))
        self.groupBox_current.setTitle(_translate("Dialog", "Current Measurements"))
        self.label_6.setText(_translate("Dialog", "Shoulder pan adduction/abduction:"))
        self.label_7.setText(_translate("Dialog", "External rotation:"))
        self.label_8.setText(_translate("Dialog", "Shoulder extension/flexion:"))
        self.label_9.setText(_translate("Dialog", "Internal rotation:"))
        self.label.setText(_translate("Dialog", "Additional Notes:"))
        self.button_back.setText(_translate("Dialog", "< Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
