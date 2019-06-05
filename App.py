# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file1 = QtWidgets.QLabel(self.centralwidget)
        self.file1.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.file1.setObjectName("file1")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 631, 16))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 30, 631, 16))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.file2 = QtWidgets.QLabel(self.centralwidget)
        self.file2.setGeometry(QtCore.QRect(10, 30, 101, 21))
        self.file2.setObjectName("file2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 90, 191, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.image2 = QtWidgets.QLabel(self.centralwidget)
        self.image2.setGeometry(QtCore.QRect(10, 470, 191, 211))
        self.image2.setObjectName("image2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 440, 121, 21))
        self.label_2.setObjectName("label_2")
        self.image1 = QtWidgets.QLabel(self.centralwidget)
        self.image1.setGeometry(QtCore.QRect(10, 110, 229, 212))
        self.image1.setObjectName("image1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 51, 31))
        self.label.setObjectName("label")
        self.resultedImage = QtWidgets.QLabel(self.centralwidget)
        self.resultedImage.setGeometry(QtCore.QRect(490, 130, 231, 281))
        self.resultedImage.setObjectName("resultedImage")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 100, 211, 41))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 18))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menumenu.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file1.setText(_translate("MainWindow", "TextLabel"))
        self.file2.setText(_translate("MainWindow", "TextLabel"))
        self.image2.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "image2"))
        self.image1.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "image1"))
        self.resultedImage.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "ResultedImage"))
        self.menumenu.setTitle(_translate("MainWindow", "menu "))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))


