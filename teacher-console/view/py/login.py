# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QLineEdit

from commons import share
from sql.tables.teacher import Teacher
from view.py.main import MainWindow


class Ui_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 554)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 150, 61, 41))
        self.label.setObjectName("label")
        self.teacherNo = QtWidgets.QLineEdit(Form)
        self.teacherNo.setGeometry(QtCore.QRect(290, 150, 281, 41))
        self.teacherNo.setObjectName("teacherNo")
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
        self.label.setText(_translate("Form", "<html><head/><body><p>教师编号</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>密钥</p></body></html>"))
        self.loginBtn.setText(_translate("Form", "登录"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#7e7e7e;\">暂不支持注册</span></p></body></html>"))



class LoginWindow(QWidget, Ui_Login):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Face AI Detection System For Teacher")

        self.password.setEchoMode(QLineEdit.Password)

        self.loginBtn.clicked.connect(self.loginTest)

    def loginTest(self):
        teacherNo = self.teacherNo.text()
        password = self.password.text()

        if teacherNo == "":
            QMessageBox().information(self, "FAIL", "请输入账户密码后再进行登录!!!")
            return

        if password == "":
            QMessageBox().information(self, "FAIL", "请输入账户密码后再进行登录!!!")
            return

        teacher = Teacher()
        self.result = teacher.matchLogin(teacherNo, password)

        if len(self.result) > 0:
            share.currentUser = self.result[0]
            QMessageBox().information(self, "SUCCESS", "登录成功(请稍等几秒钟, 正在加载页面...)")

            share.loginWindow.hide()

            share.mainWindow = MainWindow()
            share.mainWindow.show()
        else:
            QMessageBox().information(self, "FAIL", "验证失败")
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)

    loginWindow = LoginWindow()
    loginWindow.show()

    sys.exit(app.exec_())
