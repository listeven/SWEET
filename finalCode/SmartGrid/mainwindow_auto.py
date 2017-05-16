# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 326)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgb(0,121,193)\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.SmartGridButton = QtWidgets.QPushButton(self.centralWidget)
        self.SmartGridButton.setGeometry(QtCore.QRect(0, 0, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.SmartGridButton.setFont(font)
        self.SmartGridButton.setStyleSheet("QPushButton{\n"
"    background-color: rbg(255,255,255)\n"
"}")
        self.SmartGridButton.setObjectName("SmartGridButton")
        self.BostonSkyline = QtWidgets.QLabel(self.centralWidget)
        self.BostonSkyline.setGeometry(QtCore.QRect(10, 70, 141, 91))
        self.BostonSkyline.setText("")
        self.BostonSkyline.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Code/graphics/BostonSkyline.png"))
        self.BostonSkyline.setScaledContents(True)
        self.BostonSkyline.setObjectName("BostonSkyline")
        self.RenewableContribution = QtWidgets.QLabel(self.centralWidget)
        self.RenewableContribution.setGeometry(QtCore.QRect(170, 50, 141, 131))
        self.RenewableContribution.setText("")
        self.RenewableContribution.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Code/graphics/RenewableContribution.png"))
        self.RenewableContribution.setScaledContents(True)
        self.RenewableContribution.setObjectName("RenewableContribution")
        self.PercentGreen = QtWidgets.QLabel(self.centralWidget)
        self.PercentGreen.setGeometry(QtCore.QRect(340, 40, 111, 141))
        self.PercentGreen.setText("")
        self.PercentGreen.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Code/graphics/100percent.png"))
        self.PercentGreen.setScaledContents(True)
        self.PercentGreen.setObjectName("PercentGreen")
        self.lcdBostonNeed = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdBostonNeed.setGeometry(QtCore.QRect(40, 220, 71, 31))
        self.lcdBostonNeed.setStyleSheet("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 85, 0);\n"
"}")
        self.lcdBostonNeed.setObjectName("lcdBostonNeed")
        self.lcdRenewable = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdRenewable.setGeometry(QtCore.QRect(200, 220, 71, 31))
        self.lcdRenewable.setStyleSheet("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 85, 0);\n"
"}")
        self.lcdRenewable.setObjectName("lcdRenewable")
        self.lcdPercentGreen = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdPercentGreen.setGeometry(QtCore.QRect(360, 220, 71, 31))
        self.lcdPercentGreen.setStyleSheet("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 85, 0);\n"
"}")
        self.lcdPercentGreen.setObjectName("lcdPercentGreen")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(130, 200, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(340, 200, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralWidget)
##        self.menuBar = QtWidgets.QMenuBar(MainWindow)
##        self.menuBar.setGeometry(QtCore.QRect(0, 0, 514, 22))
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
        self.SmartGridButton.setText(_translate("MainWindow", "Smart Grid"))
        self.label.setText(_translate("MainWindow", "SWEET City"))
        self.label_2.setText(_translate("MainWindow", "Renewable Contribution:"))
        self.label_3.setText(_translate("MainWindow", "Boston Need:"))
        self.label_4.setText(_translate("MainWindow", "Percent Green:"))

