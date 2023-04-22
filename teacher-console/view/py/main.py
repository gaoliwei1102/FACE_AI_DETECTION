# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QStackedLayout

from commons import share
from view.py.editMyself import EditMyselfPage
from view.py.enterDetection import EnterDetectionPage
from view.py.mycourse import MyCoursePage


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
        self.myCoursesBtn = QtWidgets.QPushButton(self.groupBox)
        self.myCoursesBtn.setGeometry(QtCore.QRect(20, 30, 111, 41))
        self.myCoursesBtn.setObjectName("myCoursesBtn")
        self.editMyselfBtn = QtWidgets.QPushButton(self.groupBox)
        self.editMyselfBtn.setGeometry(QtCore.QRect(20, 190, 111, 41))
        self.editMyselfBtn.setObjectName("editMyselfBtn")
        self.enterCourseBtn = QtWidgets.QPushButton(self.groupBox)
        self.enterCourseBtn.setGeometry(QtCore.QRect(20, 110, 111, 41))
        self.enterCourseBtn.setObjectName("enterCourseBtn")
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
        self.myCoursesBtn.setText(_translate("MainWindow", "我的课表"))
        self.editMyselfBtn.setText(_translate("MainWindow", "个人设置"))
        self.enterCourseBtn.setText(_translate("MainWindow", "进入课程"))
        self.author.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\">Author:Mr.Gao(2022-create)</span></p></body></html>"))
        self.datetime.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\">Copyright 1607701069@qq.com</span></p></body></html>"))





class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(share.currentUser)

        # 实例化一个堆叠布局
        self.qsl = QStackedLayout(self.frame)

        # 实例化分页面
        self.myCoursesPage = MyCoursePage()
        self.enterDetectionPage = EnterDetectionPage()
        self.editMyself = EditMyselfPage()

        # 加入到布局中
        self.qsl.addWidget(self.myCoursesPage)
        self.qsl.addWidget(self.enterDetectionPage)
        self.qsl.addWidget(self.editMyself)

        # 控制函数
        self.controller()

    def controller(self):
        self.myCoursesBtn.clicked.connect(self.switch)
        self.enterCourseBtn.clicked.connect(self.switch)
        self.editMyselfBtn.clicked.connect(self.switch)


    def switch(self):
        sender = self.sender().objectName()

        index = {
            "myCoursesBtn": 0,
            "enterCourseBtn":1,
            "editMyselfBtn":2,
        }

        self.qsl.setCurrentIndex(index[sender])






if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())



