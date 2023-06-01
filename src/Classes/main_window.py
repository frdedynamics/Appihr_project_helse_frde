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
        self.button_review_data = QtWidgets.QPushButton(self.centralwidget)
        self.button_review_data.setGeometry(QtCore.QRect(230, 70, 141, 61))
        self.button_review_data.setObjectName("button_review_data")
        self.button_record_data = QtWidgets.QPushButton(self.centralwidget)
        self.button_record_data.setGeometry(QtCore.QRect(230, 160, 141, 61))
        self.button_record_data.setObjectName("button_record_data")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 260, 100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/gizem/catkin_ws/src/appirh_project_helse_frde/ui/../fig/hvlLogo_original.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
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
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_review_data.setText(_translate("MainWindow", "Review Data"))
        self.button_record_data.setText(_translate("MainWindow", "Record Data"))
        self.menuFile.setTitle(_translate("MainWindow", "Options"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
