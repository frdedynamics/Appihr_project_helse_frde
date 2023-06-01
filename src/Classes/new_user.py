# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/new_user.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 376)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 151, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 100, 141, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 130, 141, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 160, 141, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(50, 190, 141, 17))
        self.label_9.setObjectName("label_9")
        self.lineEdit_chest_to_shoulder = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_chest_to_shoulder.setGeometry(QtCore.QRect(250, 90, 113, 25))
        self.lineEdit_chest_to_shoulder.setObjectName("lineEdit_chest_to_shoulder")
        self.lineEdit_shoulder_to_elbow = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_shoulder_to_elbow.setGeometry(QtCore.QRect(250, 120, 113, 25))
        self.lineEdit_shoulder_to_elbow.setObjectName("lineEdit_shoulder_to_elbow")
        self.lineEdit_elbow_to_wrist = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_elbow_to_wrist.setGeometry(QtCore.QRect(250, 150, 113, 25))
        self.lineEdit_elbow_to_wrist.setObjectName("lineEdit_elbow_to_wrist")
        self.lineEdit_wrist_to_fingertip = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_wrist_to_fingertip.setGeometry(QtCore.QRect(250, 180, 113, 25))
        self.lineEdit_wrist_to_fingertip.setObjectName("lineEdit_wrist_to_fingertip")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(150, 350, 166, 25))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(50, 60, 141, 17))
        self.label_10.setObjectName("label_10")
        self.lineEdit_userID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_userID.setGeometry(QtCore.QRect(250, 60, 113, 25))
        self.lineEdit_userID.setObjectName("lineEdit_userID")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "User Measures:"))
        self.label_6.setText(_translate("Dialog", "Chest to shoulder:"))
        self.label_7.setText(_translate("Dialog", "Shoulder to elbow:"))
        self.label_8.setText(_translate("Dialog", "Elbow to wrist:"))
        self.label_9.setText(_translate("Dialog", "Wrist to finger tip:"))
        self.label_10.setText(_translate("Dialog", "ID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
