# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/first_patient_selection.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 377)
        self.button_new_user = QtWidgets.QPushButton(Dialog)
        self.button_new_user.setGeometry(QtCore.QRect(260, 190, 171, 41))
        self.button_new_user.setObjectName("button_new_user")
        self.button_new_user_2 = QtWidgets.QPushButton(Dialog)
        self.button_new_user_2.setGeometry(QtCore.QRect(70, 190, 171, 41))
        self.button_new_user_2.setObjectName("button_new_user_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_new_user.setText(_translate("Dialog", "Create new patient "))
        self.button_new_user_2.setText(_translate("Dialog", "Add to existing patient"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
