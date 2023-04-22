# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editMyself.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QMessageBox

from commons import share
from sql.tables.teacher import Teacher


class Ui_EditMyself(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1047, 600)
        self.saveBtn = QtWidgets.QPushButton(Form)
        self.saveBtn.setGeometry(QtCore.QRect(440, 510, 201, 41))
        self.saveBtn.setObjectName("saveBtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 100, 91, 51))
        self.label.setObjectName("label")
        self.teacher_id = QtWidgets.QLineEdit(Form)
        self.teacher_id.setGeometry(QtCore.QRect(430, 90, 301, 41))
        self.teacher_id.setObjectName("teacher_id")
        self.teacher_no = QtWidgets.QLineEdit(Form)
        self.teacher_no.setGeometry(QtCore.QRect(430, 170, 301, 41))
        self.teacher_no.setObjectName("teacher_no")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 170, 91, 51))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(430, 250, 301, 41))
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 250, 91, 51))
        self.label_3.setObjectName("label_3")
        self.password_again = QtWidgets.QLineEdit(Form)
        self.password_again.setGeometry(QtCore.QRect(430, 340, 301, 41))
        self.password_again.setObjectName("password_again")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(280, 340, 91, 51))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(90, 480, 881, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(90, 40, 881, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(80, 50, 20, 441))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(960, 50, 20, 441))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveBtn.setText(_translate("Form", "立即保存"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">教师ID</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">教师编号</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">密    码</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">再次输入</span></p></body></html>"))


class EditMyselfPage(QWidget, Ui_EditMyself):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.teacher_id.setEnabled(False)
        self.teacher_no.setEnabled(False)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_again.setEchoMode(QLineEdit.Password)

        self.teacher_id.setText(share.currentUser[0])
        self.teacher_no.setText(share.currentUser[1])

        self.saveBtn.clicked.connect(self.editMyself)


    def editMyself(self):
        password = self.password.text()
        password_again = self.password_again.text()

        if password == "" or password_again == "":
            QMessageBox().warning(self, "FAIL", "请先输入后, 再进行保存!!!")
            return

        if password != password_again:
            QMessageBox().warning(self, "FAIL", "两次输入的密码不一致, 无法修改密码!!!")
            return

        teacher = Teacher()
        result  = teacher.modifyPassword(password)

        if result >= 1:
            QMessageBox().information(self, "SUCCESS", "修改密码成功!!!")
            share.currentUser = teacher.getTeacher()[0]
            self.password.setText("")
            self.password_again.setText("")
            return
        else:
            QMessageBox().warning(self, "FAIL", "出现异常, 请稍后......")
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = EditMyselfPage()
    example.show()
    sys.exit(app.exec_())