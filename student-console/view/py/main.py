# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 151, 601))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.testDetectionBtn = QtWidgets.QPushButton(self.groupBox)
        self.testDetectionBtn.setGeometry(QtCore.QRect(20, 30, 111, 41))
        self.testDetectionBtn.setObjectName("testDetectionBtn")
        self.myCoursesBtn = QtWidgets.QPushButton(self.groupBox)
        self.myCoursesBtn.setGeometry(QtCore.QRect(20, 100, 111, 41))
        self.myCoursesBtn.setObjectName("myCoursesBtn")
        self.myClassesBtn = QtWidgets.QPushButton(self.groupBox)
        self.myClassesBtn.setGeometry(QtCore.QRect(20, 170, 111, 41))
        self.myClassesBtn.setObjectName("myClassesBtn")
        self.updateFaceBtn = QtWidgets.QPushButton(self.groupBox)
        self.updateFaceBtn.setGeometry(QtCore.QRect(20, 310, 111, 41))
        self.updateFaceBtn.setObjectName("updateFaceBtn")
        self.deleteFaceBtn = QtWidgets.QPushButton(self.groupBox)
        self.deleteFaceBtn.setGeometry(QtCore.QRect(20, 380, 111, 41))
        self.deleteFaceBtn.setObjectName("deleteFaceBtn")
        self.editSelfBtn = QtWidgets.QPushButton(self.groupBox)
        self.editSelfBtn.setGeometry(QtCore.QRect(20, 520, 111, 41))
        self.editSelfBtn.setObjectName("editSelfBtn")
        self.enterDetectionBtn = QtWidgets.QPushButton(self.groupBox)
        self.enterDetectionBtn.setGeometry(QtCore.QRect(20, 240, 111, 41))
        self.enterDetectionBtn.setObjectName("enterDetectionBtn")
        self.searchViolateBtn = QtWidgets.QPushButton(self.groupBox)
        self.searchViolateBtn.setGeometry(QtCore.QRect(20, 450, 111, 41))
        self.searchViolateBtn.setObjectName("searchViolateBtn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(190, 20, 1051, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setGeometry(QtCore.QRect(1030, 640, 211, 21))
        self.author.setObjectName("author")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 620, 1291, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.datetime = QtWidgets.QLabel(self.centralwidget)
        self.datetime.setGeometry(QtCore.QRect(1030, 660, 241, 21))
        self.datetime.setObjectName("datetime")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 1281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testDetectionBtn.setText(_translate("MainWindow", "检测模拟"))
        self.myCoursesBtn.setText(_translate("MainWindow", "我的课表"))
        self.myClassesBtn.setText(_translate("MainWindow", "我的班级"))
        self.updateFaceBtn.setText(_translate("MainWindow", "人脸注册"))
        self.deleteFaceBtn.setText(_translate("MainWindow", "人脸删除"))
        self.editSelfBtn.setText(_translate("MainWindow", "个人设置"))
        self.enterDetectionBtn.setText(_translate("MainWindow", "进入课程"))
        self.searchViolateBtn.setText(_translate("MainWindow", "违规检索"))
        self.author.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\">Author:Mr.Gao(2022-create)</span></p></body></html>"))
        self.datetime.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\">Copyright 1607701069@qq.com</span></p></body></html>"))


