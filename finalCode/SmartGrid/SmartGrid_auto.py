# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SmartGrid.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 323)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgb(0, 121, 193)\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 210, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rbg(255,255,255)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lcdTotalCustomer = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdTotalCustomer.setGeometry(QtCore.QRect(50, 50, 81, 41))
        self.lcdTotalCustomer.setStyleSheet("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 85, 0);\n"
"}")
        self.lcdTotalCustomer.setObjectName("lcdTotalCustomer")
        self.lcdCustomerOut = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdCustomerOut.setGeometry(QtCore.QRect(300, 50, 81, 41))
        self.lcdCustomerOut.setStyleSheet("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 85, 0);\n"
"}")
        self.lcdCustomerOut.setObjectName("lcdCustomerOut")
        self.lcdtimer = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdtimer.setGeometry(QtCore.QRect(160, 140, 141, 61))
        self.lcdtimer.setStyleSheet("QLCDNumber{\n"
"    background-color: rgb(255, 255, 255)\n"
"}")
        self.lcdtimer.setObjectName("lcdtimer")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(170, 100, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 131, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Code/graphics/Blog_Gados_NatGrid.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralWidget)
##        self.menuBar = QtWidgets.QMenuBar(MainWindow)
##        self.menuBar.setGeometry(QtCore.QRect(0, 0, 470, 22))
##        self.menuBar.setObjectName("menuBar")
##        MainWindow.setMenuBar(self.menuBar)
##        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
##        self.mainToolBar.setObjectName("mainToolBar")
##        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
##        self.statusBar = QtWidgets.QStatusBar(MainWindow)
##        self.statusBar.setObjectName("statusBar")
##        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Total Number Customers:"))
        self.label_2.setText(_translate("MainWindow", "Number Customers Out:"))
        self.label_3.setText(_translate("MainWindow", "Time Out:"))

