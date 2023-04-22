# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import json
import socket
import sys
import time
from ast import literal_eval
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QHeaderView, QAbstractItemView, QTableWidgetItem, QLabel, \
    QMessageBox, QInputDialog

from commons import share
from commons.utils import getCurrentDateTime, getRandomUUID
from sql.tables.student import Student
from sql.tables.violate import Violate
from sql.tables.violate_type import ViolateType
from thread.accept_thread import ReceiveMessageThread


class Ui_Dection(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1504, 797)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(200, 10, 1301, 761))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 161, 81))
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
        self.groupBox_4.setGeometry(QtCore.QRect(20, 150, 161, 221))
        self.groupBox_4.setObjectName("groupBox_4")
        self.noSingInWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.noSingInWidget.setGeometry(QtCore.QRect(10, 20, 141, 191))
        self.noSingInWidget.setObjectName("noSingInWidget")
        self.noSingInWidget.setColumnCount(0)
        self.noSingInWidget.setRowCount(0)
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 410, 161, 171))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.violate_type = QtWidgets.QLineEdit(self.groupBox_5)
        self.violate_type.setGeometry(QtCore.QRect(70, 60, 81, 21))
        self.violate_type.setObjectName("violate_type")
        self.remarksBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.remarksBtn.setGeometry(QtCore.QRect(10, 90, 51, 21))
        self.remarksBtn.setObjectName("remarksBtn")
        self.studentNameBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.studentNameBtn.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.studentNameBtn.setObjectName("studentNameBtn")
        self.student_name = QtWidgets.QLineEdit(self.groupBox_5)
        self.student_name.setGeometry(QtCore.QRect(70, 30, 81, 21))
        self.student_name.setObjectName("student_name")
        self.remarks = QtWidgets.QLineEdit(self.groupBox_5)
        self.remarks.setGeometry(QtCore.QRect(70, 90, 81, 21))
        self.remarks.setObjectName("remarks")
        self.recordBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.recordBtn.setGeometry(QtCore.QRect(10, 120, 141, 41))
        self.recordBtn.setObjectName("recordBtn")
        self.violateTypeBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.violateTypeBtn.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.violateTypeBtn.setObjectName("violateTypeBtn")

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
        self.remarksBtn.setText(_translate("Form", "备注"))
        self.studentNameBtn.setText(_translate("Form", "姓名"))
        self.recordBtn.setText(_translate("Form", "录入违规"))
        self.violateTypeBtn.setText(_translate("Form", "类型"))


class DetectionPage(QWidget, Ui_Dection):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.student_name.setEnabled(False)
        self.violate_type.setEnabled(False)
        self.remarks.setEnabled(False)
        self.studentNameBtn.clicked.connect(self.clickedStudentNameBtn)
        self.violateTypeBtn.clicked.connect(self.clickedViolateTypeBtn)
        self.remarksBtn.clicked.connect(self.clickedRemarks)
        self.recordBtn.clicked.connect(self.clickedRecordViolate)

        student = Student()
        self.students = student.selectAllStudentsByClass(share.currentCourse[3])
        # print(self.students)

        self.clients = []
        self.students_id = []
        self.light = -1

        self.startDetectionBtn.clicked.connect(self.openServer)
        self.stopDetectionBtn.clicked.connect(self.closeServer)
        self.startDetectionBtn.setEnabled(True)
        self.stopDetectionBtn.setEnabled(False)
        self.recordBtn.setEnabled(False)
        self.studentNameBtn.setEnabled(False)
        self.violateTypeBtn.setEnabled(False)
        self.remarksBtn.setEnabled(False)



        self.initTable()
        self.initLittleTbale()


    def initTable(self):

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

        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setHorizontalHeaderLabels(['学生ID', '姓名', '性别', '年龄', '在线', '本人', '眼镜',
                                                    '表情', '疲劳状况', '脸型', '真实人脸', '脸部位置', '脸部大小',
                                                    '更新时间', '状态判断'])

    def initLittleTbale(self):
        # 设置表头可伸缩模式
        self.noSingInWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置表格为只读模式
        self.noSingInWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选中
        # tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.noSingInWidget.resizeColumnsToContents()
        self.noSingInWidget.resizeRowsToContents()

        # # 隐藏水平方向的表头
        # tableWidget.verticalHeader().setVisible(False)
        # # 隐藏垂直方向表头
        # tableWidget.horizontalHeader().setVisible(False)

        self.noSingInWidget.setRowCount(50)
        self.noSingInWidget.setColumnCount(1)
        self.noSingInWidget.setHorizontalHeaderLabels(['学生姓名'])

    def openServer(self):
        self.s = socket.socket()  # 创建 socket 对象
        self.host = socket.gethostname()  # 获取本地主机名
        self.port = 12345  # 设置端口
        self.s.bind((self.host, self.port))  # 绑定端口
        self.s.listen(50)  # 等待客户端连接

        acceptConncetThread = Thread(target=self.acceptConncet)
        acceptConncetThread.start()

        self.printNotSigninStudents()
        self.state.setText("正在连接中...")

        self.startDetectionBtn.setEnabled(False)
        self.stopDetectionBtn.setEnabled(True)
        self.recordBtn.setEnabled(True)
        self.studentNameBtn.setEnabled(True)
        self.violateTypeBtn.setEnabled(True)
        self.remarksBtn.setEnabled(True)

    def closeServer(self):

        data = str(QMessageBox().information(self, "Information", "您确定要结束当前课堂退出到主页面嘛?", QMessageBox.Yes|QMessageBox.No))

        if data == "16384":
            for i in range(0, len(self.clients)):
                self.clients[i].close()

            self.clearTable()
            self.s.close()
            share.detectionWindow.hide()
            share.mainWindow.show()
        else:
            return

    def acceptConncet(self):

        while True:

            try:
                client, addr = self.s.accept()  # 建立客户端连接

            except:
                break

            self.clients.append(client)


            thread = ReceiveMessageThread(client)
            thread.valueChange.connect(self.printMessage)
            thread.start()

    def printMessage(self, data):


        self.light = self.light * (-1)
        idItem = QTableWidgetItem()
        nameItem = QTableWidgetItem()
        sexItem = QTableWidgetItem()
        ageItem = QTableWidgetItem()
        online = QTableWidgetItem()
        isme = QTableWidgetItem()
        glass = QTableWidgetItem()
        emotion = QTableWidgetItem()
        eye = QTableWidgetItem()
        face_shape = QTableWidgetItem()
        face_type = QTableWidgetItem()
        location = QTableWidgetItem()
        face_size = QTableWidgetItem()
        current_time = QTableWidgetItem()


        if data != None and data != '':
            print(data)

            try:
                row = self.students_id.index(data['student_id'])
            except:
                self.students_id.append(data['student_id'])
                row = self.students_id.index(data['student_id'])


            self.printNotSigninStudents()
            self.number.setText(str(len(self.students_id)))

            idItem.setText(data['student_id'])
            self.tableWidget.setItem(row, 0, idItem)

            nameItem.setText(data['student_name'])
            self.tableWidget.setItem(row, 1, nameItem)

            sexItem.setText(data['gender'])
            self.tableWidget.setItem(row, 2, sexItem)

            ageItem.setText(data['age'])
            self.tableWidget.setItem(row, 3, ageItem)

            if data['online'] == "NOT FACE!!!":
                online.setForeground(QBrush(QColor(255, 0, 0)))
            else:
                online.setForeground(QBrush(QColor(0, 255, 0)))
            online.setText(data['online'])
            self.tableWidget.setItem(row, 4, online)


            if data['isme'] == "是":
                isme.setForeground(QBrush(QColor(0, 255, 0)))
            else:
                isme.setForeground(QBrush(QColor(255, 0, 0)))
            isme.setText(data['isme'])
            self.tableWidget.setItem(row, 5, isme)


            if data['glass'] == "#None":
                glass.setForeground(QBrush(QColor(255, 0, 0)))
            else:
                glass.setForeground(QBrush(QColor(0, 255, 0)))
            glass.setText(data['glass'])
            self.tableWidget.setItem(row, 6, glass)



            if data['emotion'] == "#None":
                emotion.setForeground(QBrush(QColor(255, 0, 0)))
            else:
                emotion.setForeground(QBrush(QColor(0, 255, 0)))
            emotion.setText(data['emotion'])
            self.tableWidget.setItem(row, 7, emotion)


            if data['left_eye'] == "正常" and data['right_eye'] == "正常":
                eye.setForeground(QBrush(QColor(0, 255, 0)))
                eye.setText("正常")
                self.tableWidget.setItem(row, 8, eye)
            else:
                eye.setForeground(QBrush(QColor(255, 0, 0)))
                eye.setText("疲劳")
                self.tableWidget.setItem(row, 8, eye)


            if data['face_shape'] == "#None":
                face_shape.setForeground(QBrush(QColor(255, 0, 0)))
            else:
                face_shape.setForeground(QBrush(QColor(0, 255, 0)))
            face_shape.setText(data['face_shape'])
            self.tableWidget.setItem(row, 9, face_shape)



            if data['face_type'] == "#None":
                face_type.setForeground(QBrush(QColor(255, 0, 0)))
            else:
                face_type.setForeground(QBrush(QColor(0, 255, 0)))
            face_type.setText(data['face_type'])
            self.tableWidget.setItem(row, 10, face_type)


            if data['location'] == "#None":
                location.setForeground(QBrush(QColor(255, 0, 0)))
            else:
                location.setForeground(QBrush(QColor(0, 255, 0)))
            location.setText(data['location'])
            self.tableWidget.setItem(row, 11, location)


            if data['face_size'] == "#None":
                face_size.setForeground(QBrush(QColor(255, 0, 0)))
            else:
                face_size.setForeground(QBrush(QColor(0, 255, 0)))
            face_size.setText(data['face_size'])
            self.tableWidget.setItem(row, 12, face_size)

            if self.light > 0:
                current_time.setForeground(QBrush(QColor(230, 11, 240)))
            else:
                current_time.setForeground(QBrush(QColor(90, 69, 241)))

            current_time.setText(data['current_time'])
            self.tableWidget.setItem(row, 13, current_time)

    def printNotSigninStudents(self):

        for i in range(0, len(self.students)):
            item = QTableWidgetItem("")
            self.noSingInWidget.setItem(i, 0, item)

        not_signin = 0
        for i in range(0, len(self.students)):
            flag = True
            for j in range(0, len(self.students_id)):
                if self.students_id[j] == self.students[i][0]:
                    flag = False
                    break
            if flag == True:
                item = QTableWidgetItem(self.students[i][2])
                self.noSingInWidget.setItem(not_signin, 0, item)
                not_signin += 1

    def clearTable(self):
        for i in range(0, self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)

    def clickedStudentNameBtn(self):

        items = []
        for i in range(0, len(self.students)):
            items.append(self.students[i][2])

        item, ok = QInputDialog.getItem(self, 'Select Student', "学生列表", items, 0, False)
        if ok and item:
            self.student_name.setText(item)

    def clickedViolateTypeBtn(self):
        violateType = ViolateType()
        violateTypes = violateType.selectAllViolateType()

        items = []
        for i in range(0, len(violateTypes)):
            items.append(violateTypes[i][1])

        item, ok = QInputDialog.getItem(self, 'Select Violate', "违规列表", items, 0, False)

        if ok and item:
            self.violate_type.setText(item)

    def clickedRemarks(self):
        text, ok = QInputDialog.getText(self, 'Text input dialog', '输入备注')
        if ok:
            self.remarks.setText(str(text))

    def clickedRecordViolate(self):
        id = getRandomUUID()
        course = share.currentCourse[0]

        student_name = self.student_name.text()

        violate_name = self.violate_type.text()

        remarks = self.remarks.text()

        now = getCurrentDateTime()

        if student_name=="" or violate_name=="" or remarks=="":
            QMessageBox().information(self, "FAIL", "请输入具体信息后再录入违规系统!!!")
            return


        for i in range(0, len(self.students)):
            if self.students[i][2] == student_name:
                student_id = self.students[i][0]
                break

        violateType = ViolateType()
        violateTypes = violateType.selectViolateTypeByName(violate_name)
        violate_type_id = violateTypes[0][0]

        violate = (id, violate_type_id, course, student_id, remarks, now)

        violateMapper = Violate()

        result = violateMapper.insertViolate(violate)

        if result > 0:
            QMessageBox().information(self, "SUCCESS", "录入违规系统成功!!!")
            self.student_name.setText("")
            self.violate_type.setText("")
            self.remarks.setText("")
            return
        else:
            QMessageBox().warning(self, "FAIL", "录入违规系统失败!!!")
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)

    detection = DetectionPage()
    detection.show()

    sys.exit(app.exec_())