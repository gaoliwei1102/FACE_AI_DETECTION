# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faceDelete.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QHeaderView, QAbstractItemView, QTableWidgetItem, QMessageBox

from commons import share
from properties import client
from sql.tables.student import Student
from thread.delete_face_thread import DeleteThread


class Ui_FaceDelete(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1047, 600)
        self.startDeleteBtn = QtWidgets.QPushButton(Form)
        self.startDeleteBtn.setGeometry(QtCore.QRect(440, 530, 141, 41))
        self.startDeleteBtn.setObjectName("startDeleteBtn")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(40, 480, 991, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 91, 41))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 200, 262, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(350, 10, 641, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(820, 510, 211, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setGeometry(QtCore.QRect(850, 450, 141, 28))
        self.refreshButton.setObjectName("refreshButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.startDeleteBtn.setText(_translate("Form", "开始清空"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">注意：</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">人脸数据一旦删除，不可恢复</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">务必谨慎操作</span></p></body></html>"))
        self.refreshButton.setText(_translate("Form", "刷新列表(Refresh)"))



class FaceDeletePage(QWidget, Ui_FaceDelete):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startDeleteBtn.clicked.connect(self.deleteFaceData)
        self.refreshButton.clicked.connect(self.refreshFaceData)

        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(2)

        #设置表头信息
        self.tableWidget.setHorizontalHeaderLabels(['faceId', '创建时间'])

        # 设置表头可伸缩模式
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置表格为只读模式
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选中
        # tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        # # 隐藏水平方向的表头
        # tableWidget.verticalHeader().setVisible(False)
        # # 隐藏垂直方向表头
        # tableWidget.horizontalHeader().setVisible(False)


        """ 调用获取用户人脸列表 """
        data = client.faceGetlist(share.currentUser[0], share.currentUser[6])


        if data['result'] == None:      #若用户无面部信息, 直接返回
            return

        self.current_face_data = data['result']['face_list']
        self.showFaceData()


    def showFaceData(self):

        for i in range(0, len(self.current_face_data)):
            newItem01 = QTableWidgetItem(self.current_face_data[i]['face_token'])
            newItem02 = QTableWidgetItem(self.current_face_data[i]['ctime'])
            self.tableWidget.setItem(i, 0, newItem01)
            self.tableWidget.setItem(i, 1, newItem02)


    def deleteFaceData(self):

        if share.currentUser[7] == 0:
            QMessageBox().information(self, "FAIL", "未检测到您的人脸信息, 请先进行注册!!!")
            return

        self.startDeleteBtn.setEnabled(False)
        self.refreshButton.setEnabled(False)

        self.deleteThread = DeleteThread()
        self.deleteThread.valueChange.connect(self.writeProgressBar)
        self.deleteThread.start()


    def refreshFaceData(self):
        current_data = client.faceGetlist(share.currentUser[0], share.currentUser[6])
        if current_data['result'] == None:      #若用户无面部信息, 直接返回
            return

        refresh_current_face_data = current_data['result']['face_list']

        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(2)

        for i in range(0, len(refresh_current_face_data)):
            newItem01 = QTableWidgetItem(refresh_current_face_data[i]['face_token'])
            newItem02 = QTableWidgetItem(refresh_current_face_data[i]['ctime'])
            self.tableWidget.setItem(i, 0, newItem01)
            self.tableWidget.setItem(i, 1, newItem02)


    def writeProgressBar(self, value):
        self.tableWidget.removeRow(20-value)
        self.progressBar.setValue(value*5)
        self.label.setText("操作成功,已经删除#" + str(value) + "数据!")
        if value*5 == 100:
            self.deleteThread.cancel()          #线程取消

            student = Student()
            result = student.deleteStudentFace()
            share.currentUser = student.getStudent()[0]

            QMessageBox().information(self, "SUCCESS", "删除成功!!!")
            self.label.setText("")
            self.progressBar.setValue(0)
            self.startDeleteBtn.setEnabled(True)
            self.refreshButton.setEnabled(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    facePage =  FaceDeletePage()
    facePage.show()

    sys.exit(app.exec_())