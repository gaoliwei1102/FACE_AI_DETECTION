# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faceRegister.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from commons import share
from sql.tables.student import Student
from thread.detection_thread import DetectionThread
from thread.register_face_thread import RegisterThread


class Ui_FaceRegister(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1047, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 20, 641, 471))
        self.label.setText("")
        self.label.setObjectName("label")
        self.startRegisterBtn = QtWidgets.QPushButton(Form)
        self.startRegisterBtn.setGeometry(QtCore.QRect(440, 550, 141, 41))
        self.startRegisterBtn.setObjectName("startRegisterBtn")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(50, 510, 991, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 91, 41))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 110, 161, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.startRegisterBtn.setText(_translate("Form", "开始注册"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">注意：</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "1、请正视摄像头"))
        self.label_4.setText(_translate("Form", "2、不得佩戴口罩"))
        self.label_5.setText(_translate("Form", "3、保证光亮充足"))
        self.label_6.setText(_translate("Form", "4、不得中途退出"))
        self.label_7.setText(_translate("Form", "5、面部表情平和"))
        self.label_8.setText(_translate("Form", "6、最好进行模拟检测"))


class FaceRegisterPage(QWidget, Ui_FaceRegister):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label.setScaledContents(True)
        self.label.setStyleSheet("background-color:gray;")
        self.startRegisterBtn.clicked.connect(self.register)

    def register(self):
        if share.currentUser[7]== 20:
            QMessageBox().information(self, "FAIL", "您已经注册过人脸, 不能多次注册!!!")
            return
        self.startRegisterBtn.setEnabled(False)

        self.detectionThread = DetectionThread()
        self.registerThread = RegisterThread()
        self.detectionThread.valueChange.connect(self.printImage)
        self.registerThread.valueChange.connect(self.printProgress)
        self.detectionThread.start()
        self.registerThread.start()

    def printImage(self, img):
        self.label.setPixmap(img)

    def printProgress(self, value):
        self.progressBar.setValue(value*5)
        if value*5 == 100:
            self.detectionThread.cancel()                                           #线程取消
            self.registerThread.cancel()

            student = Student()
            student.addStudentFace()                                                #更改数据库的信息

            share.currentUser = student.getStudent()[0]                         #更新系统的人脸信息

            QMessageBox().information(self, "SUCCESS", "注册成功!!!")
            self.progressBar.setValue(0)
            self.startRegisterBtn.setEnabled(True)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    facePage =  FaceRegisterPage()
    facePage.show()

    sys.exit(app.exec_())
