# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/threshold_selection_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        self.comboBox_th = QtWidgets.QComboBox(Dialog)
        self.comboBox_th.setGeometry(QtCore.QRect(220, 100, 251, 31))
        self.comboBox_th.setCurrentText("")
        self.comboBox_th.setObjectName("comboBox_th")
        self.lineEdit_extern_rot = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_extern_rot.setGeometry(QtCore.QRect(360, 230, 113, 25))
        self.lineEdit_extern_rot.setObjectName("lineEdit_extern_rot")
        self.button_assign = QtWidgets.QPushButton(Dialog)
        self.button_assign.setGeometry(QtCore.QRect(350, 260, 141, 51))
        self.button_assign.setObjectName("button_assign")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 110, 91, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 261, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 210, 261, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_shoulder_ext_flex = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_shoulder_ext_flex.setGeometry(QtCore.QRect(360, 140, 113, 25))
        self.lineEdit_shoulder_ext_flex.setObjectName("lineEdit_shoulder_ext_flex")
        self.lineEdit_shoulder_abd_add = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_shoulder_abd_add.setGeometry(QtCore.QRect(360, 170, 113, 25))
        self.lineEdit_shoulder_abd_add.setObjectName("lineEdit_shoulder_abd_add")
        self.lineEdit_intern_rot = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_intern_rot.setGeometry(QtCore.QRect(360, 200, 113, 25))
        self.lineEdit_intern_rot.setObjectName("lineEdit_intern_rot")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 211, 17))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 240, 261, 17))
        self.label_5.setObjectName("label_5")
        self.button_load_older_data = QtWidgets.QPushButton(Dialog)
        self.button_load_older_data.setGeometry(QtCore.QRect(350, 40, 131, 31))
        self.button_load_older_data.setObjectName("button_load_older_data")
        self.button_back = QtWidgets.QPushButton(Dialog)
        self.button_back.setGeometry(QtCore.QRect(0, 10, 89, 25))
        self.button_back.setObjectName("button_back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox_th.setToolTip(_translate("Dialog", "Bring values from the previous sessions"))
        self.button_assign.setText(_translate("Dialog", "Assign values \n"
" for this session"))
        self.label.setText(_translate("Dialog", "Thresholds"))
        self.label_3.setText(_translate("Dialog", "Shoulder pan adduction/abduction:"))
        self.label_4.setText(_translate("Dialog", "Internal rotation:"))
        self.label_2.setText(_translate("Dialog", "Shoulder extension/flexion:"))
        self.label_5.setText(_translate("Dialog", "External rotation:"))
        self.button_load_older_data.setText(_translate("Dialog", "Load Older Data"))
        self.button_back.setText(_translate("Dialog", "< Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
