# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QLineEdit

from commons import share
from sql.tables.student import Student
from view.main import MainWindow


class Ui_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 554)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 150, 61, 41))
        self.label.setObjectName("label")
        self.studentNo = QtWidgets.QLineEdit(Form)
        self.studentNo.setGeometry(QtCore.QRect(290, 150, 281, 41))
        self.studentNo.setObjectName("studentNo")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 250, 61, 41))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(290, 250, 281, 41))
        self.password.setObjectName("password")
        self.loginBtn = QtWidgets.QPushButton(Form)
        self.loginBtn.setGeometry(QtCore.QRect(300, 400, 201, 51))
        self.loginBtn.setObjectName("loginBtn")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(480, 300, 111, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">学号</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">密码</span></p></body></html>"))
        self.loginBtn.setText(_translate("Form", "登录"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#7e7e7e;\">暂不支持注册</span></p></body></html>"))

class LoginWindow(QWidget, Ui_Login):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.loginBtn.clicked.connect(self.loginMatch)

    def loginMatch(self):

        student = Student()
        studentNo = self.studentNo.text()
        password = self.password.text()

        if studentNo=='' or password=='':
            QMessageBox.warning(self, "Error", "登录失败, 请输入学号和密码!!!")
            return

        data = student.loginMatch(studentNo,password)

        if len(data) != 0:
            QMessageBox.information(self, "SUCCESS", "登录成功(初始化页面, 可能稍等几秒钟......)")
            share.loginWindow.hide()

            share.currentUser = data[0]
            share.mainWindow = MainWindow()
            share.mainWindow.show()

        else:
            QMessageBox.information(self, "FAIL", "验证失败!!!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = LoginWindow()
    example.show()
    sys.exit(app.exec_())


