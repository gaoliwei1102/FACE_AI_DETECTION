# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enterDetection.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import datetime
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from commons import share
from commons.utils import getCurrentDay, getCurrentTime
from sql.tables.course import Course
from view.py.detection import DetectionWindows


class Ui_EnterDetection(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1047, 600)
        self.enterBtn = QtWidgets.QPushButton(Form)
        self.enterBtn.setGeometry(QtCore.QRect(390, 500, 201, 41))
        self.enterBtn.setObjectName("enterBtn")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 152, 591, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.course_id = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.course_id.setObjectName("course_id")
        self.gridLayout.addWidget(self.course_id, 0, 1, 1, 1)
        self.end__time = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.end__time.setObjectName("end__time")
        self.gridLayout.addWidget(self.end__time, 6, 1, 1, 1)
        self.subject_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.subject_name.setObjectName("subject_name")
        self.gridLayout.addWidget(self.subject_name, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.teacher_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.teacher_name.setObjectName("teacher_name")
        self.gridLayout.addWidget(self.teacher_name, 2, 1, 1, 1)
        self.start_day = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.start_day.setObjectName("start_day")
        self.gridLayout.addWidget(self.start_day, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.start_time = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.start_time.setObjectName("start_time")
        self.gridLayout.addWidget(self.start_time, 5, 1, 1, 1)
        self.class_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.class_name.setObjectName("class_name")
        self.gridLayout.addWidget(self.class_name, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.remarks = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.remarks.setObjectName("remarks")
        self.gridLayout.addWidget(self.remarks, 7, 1, 1, 1)
        self.course_mssage = QtWidgets.QLabel(Form)
        self.course_mssage.setGeometry(QtCore.QRect(190, 430, 241, 21))
        self.course_mssage.setObjectName("course_mssage")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(670, 430, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(860, 150, 101, 21))
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(860, 180, 181, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(330, 50, 331, 61))
        self.label_20.setObjectName("label_20")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.enterBtn.setText(_translate("Form", "进入课堂"))
        self.label_5.setText(_translate("Form", "授课日期"))
        self.label_3.setText(_translate("Form", "授课老师"))
        self.label_2.setText(_translate("Form", "课程名称"))
        self.label_6.setText(_translate("Form", "开始时间"))
        self.label.setText(_translate("Form", "课程Id"))
        self.label_7.setText(_translate("Form", "结束时间"))
        self.label_4.setText(_translate("Form", "上课班级"))
        self.label_8.setText(_translate("Form", "备注"))
        self.course_mssage.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "刷新(refresh)"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">注意事项:</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "1、按时进入课程,"))
        self.label_11.setText(_translate("Form", "不得迟到(3min)、早退"))
        self.label_12.setText(_translate("Form", "2、保持网络畅通,"))
        self.label_13.setText(_translate("Form", "减少网络不稳定的影响"))
        self.label_14.setText(_translate("Form", "3、学生本人进入,"))
        self.label_15.setText(_translate("Form", "不得出现替听等情况"))
        self.label_16.setText(_translate("Form", "4、保持在摄像头范围,"))
        self.label_17.setText(_translate("Form", "不得长时间离开(3min)"))
        self.label_18.setText(_translate("Form", "5、神态自然"))
        self.label_19.setText(_translate("Form", "6、不得睡觉"))
        self.label_20.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">异常行为检测与分析的在线课堂</span></p></body></html>"))


class EnterDetectionPage(QWidget, Ui_EnterDetection):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.searchCurrentCourse)
        self.enterBtn.clicked.connect(self.enterDetectionWindows)

        self.course =  Course()
        self.currentCourse = None

        self.start_day.setDisplayFormat("yyyy-MM-dd")
        self.start_time.setDisplayFormat("hh:mm")
        self.end__time.setDisplayFormat("hh:mm")


        self.course_id.setEnabled(False)
        self.subject_name.setEnabled(False)
        self.teacher_name.setEnabled(False)
        self.class_name.setEnabled(False)
        self.start_day.setEnabled(False)
        self.start_time.setEnabled(False)
        self.end__time.setEnabled(False)
        self.remarks.setEnabled(False)


        self.searchCurrentCourse()


    def searchCurrentCourse(self):
        self.currentCourse = None
        self.data = self.course.selectMyAllCourses()


        for i in range(0, len(self.data)):
            if self.data[i][4] == getCurrentDay():
                if self.data[i][5] <= getCurrentTime() and self.data[i][6] >= getCurrentTime():
                    self.currentCourse = self.data[i]
                    break

        self.setData()

    def setData(self):

        if self.currentCourse != None:

            self.course_id.setText(self.currentCourse[0])
            self.subject_name.setText(self.currentCourse[1])
            self.teacher_name.setText(self.currentCourse[2])
            self.class_name.setText(self.currentCourse[3])


            self.start_day.setDate(datetime.date.fromisoformat(self.currentCourse[4]))
            self.start_time.setTime(datetime.time.fromisoformat(self.currentCourse[5]))
            self.end__time.setTime(datetime.time.fromisoformat(self.currentCourse[6]))
            self.remarks.setText(self.currentCourse[7])

            self.course_mssage.setStyleSheet("color:green;")
            self.course_mssage.setText("成功检索到可以进入的课程!!!")
            self.enterBtn.setEnabled(True)

        else:

            self.course_id.setText("#None")
            self.subject_name.setText("#None")
            self.teacher_name.setText("#None")
            self.class_name.setText("#None")

            self.start_day.setDate(datetime.date.fromisoformat("1752-09-14"))
            self.start_time.setTime(datetime.time.fromisoformat("00:01"))
            self.end__time.setTime(datetime.time.fromisoformat("00:01"))
            self.remarks.setText("#None")

            self.course_mssage.setStyleSheet("color:red;")
            self.course_mssage.setText("未检索到可以进入的课程!!!")
            self.enterBtn.setEnabled(False)


    def enterDetectionWindows(self):
        if share.currentUser[7] == 0:
            QMessageBox().warning(self, "FAIL", "您未注册相应的人脸信息, 无法进入系统!")
            return



        share.mainWindow.close()
        share.detectionWindow = DetectionWindows()
        share.detectionWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    enterPage = EnterDetectionPage()
    enterPage.show()

    sys.exit(app.exec_())
