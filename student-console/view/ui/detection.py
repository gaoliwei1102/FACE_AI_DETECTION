# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1504, 797)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(200, 10, 1301, 761))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 161, 111))
        self.groupBox.setObjectName("groupBox")
        self.number = QtWidgets.QLabel(self.groupBox)
        self.number.setGeometry(QtCore.QRect(30, 30, 51, 21))
        self.number.setObjectName("number")
        self.state = QtWidgets.QLabel(self.groupBox)
        self.state.setGeometry(QtCore.QRect(10, 60, 101, 20))
        self.state.setObjectName("state")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 660, 161, 111))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.startDetectionBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.startDetectionBtn.setGeometry(QtCore.QRect(10, 10, 141, 41))
        self.startDetectionBtn.setObjectName("startDetectionBtn")
        self.stopDetectionBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.stopDetectionBtn.setGeometry(QtCore.QRect(10, 60, 141, 41))
        self.stopDetectionBtn.setObjectName("stopDetectionBtn")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 200, 161, 221))
        self.groupBox_4.setObjectName("groupBox_4")
        self.noSingInWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.noSingInWidget.setGeometry(QtCore.QRect(10, 20, 141, 191))
        self.noSingInWidget.setObjectName("noSingInWidget")
        self.noSingInWidget.setColumnCount(0)
        self.noSingInWidget.setRowCount(0)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 500, 161, 80))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.startDetectionBtn_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.startDetectionBtn_2.setGeometry(QtCore.QRect(10, 20, 141, 41))
        self.startDetectionBtn_2.setObjectName("startDetectionBtn_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "已到学生人数"))
        self.number.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">#None</span></p></body></html>"))
        self.state.setText(_translate("Form", "#None"))
        self.startDetectionBtn.setText(_translate("Form", "开始上课"))
        self.stopDetectionBtn.setText(_translate("Form", "下课"))
        self.groupBox_4.setTitle(_translate("Form", "未进入课程同学"))
        self.startDetectionBtn_2.setText(_translate("Form", "录入违规"))


