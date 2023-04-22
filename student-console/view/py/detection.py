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
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from commons import share
from commons.utils import getCurrentDay, getCurrentTime
from sql.tables.course import Course
from thread.detection_thread import DetectionThread
from thread.discern_face_thread import DiscernThread
from thread.now_datetime_thread import NowDateTimeThread
from thread.predict_thread import PredictThread
from thread.send_message_thread import SendMessageThread


class Ui_Detection(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1256, 791)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(270, 70, 711, 501))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.screen_label = QtWidgets.QLabel(self.groupBox)
        self.screen_label.setGeometry(QtCore.QRect(20, 20, 681, 471))
        self.screen_label.setText("")
        self.screen_label.setObjectName("screen_label")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 620, 711, 80))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.startDetectionBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.startDetectionBtn.setGeometry(QtCore.QRect(150, 20, 141, 41))
        self.startDetectionBtn.setObjectName("startDetectionBtn")
        self.stopDetectionBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.stopDetectionBtn.setGeometry(QtCore.QRect(390, 20, 141, 41))
        self.stopDetectionBtn.setObjectName("stopDetectionBtn")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(1010, 70, 231, 71))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(20, 20, 191, 31))
        self.label_24.setObjectName("label_24")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(1010, 170, 231, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 30, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 41, 16))
        self.label_4.setObjectName("label_4")
        self.student_no = QtWidgets.QLabel(self.groupBox_4)
        self.student_no.setGeometry(QtCore.QRect(80, 30, 91, 16))
        self.student_no.setObjectName("student_no")
        self.student_name = QtWidgets.QLabel(self.groupBox_4)
        self.student_name.setGeometry(QtCore.QRect(80, 60, 91, 16))
        self.student_name.setObjectName("student_name")
        self.gender = QtWidgets.QLabel(self.groupBox_4)
        self.gender.setGeometry(QtCore.QRect(80, 90, 91, 16))
        self.gender.setObjectName("gender")
        self.age = QtWidgets.QLabel(self.groupBox_4)
        self.age.setGeometry(QtCore.QRect(80, 120, 91, 16))
        self.age.setObjectName("age")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(1010, 360, 231, 341))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 41, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 41, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 41, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(10, 120, 41, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setGeometry(QtCore.QRect(10, 150, 41, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(10, 180, 41, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(10, 210, 41, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(10, 240, 41, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(10, 270, 71, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(10, 300, 71, 16))
        self.label_18.setObjectName("label_18")
        self.online = QtWidgets.QLabel(self.groupBox_5)
        self.online.setGeometry(QtCore.QRect(80, 30, 91, 16))
        self.online.setObjectName("online")
        self.isme = QtWidgets.QLabel(self.groupBox_5)
        self.isme.setGeometry(QtCore.QRect(80, 60, 91, 16))
        self.isme.setObjectName("isme")
        self.glass = QtWidgets.QLabel(self.groupBox_5)
        self.glass.setGeometry(QtCore.QRect(80, 90, 91, 16))
        self.glass.setObjectName("glass")
        self.emotion = QtWidgets.QLabel(self.groupBox_5)
        self.emotion.setGeometry(QtCore.QRect(80, 120, 91, 16))
        self.emotion.setObjectName("emotion")
        self.left_eye = QtWidgets.QLabel(self.groupBox_5)
        self.left_eye.setGeometry(QtCore.QRect(80, 150, 91, 16))
        self.left_eye.setObjectName("left_eye")
        self.right_eye = QtWidgets.QLabel(self.groupBox_5)
        self.right_eye.setGeometry(QtCore.QRect(80, 180, 91, 16))
        self.right_eye.setObjectName("right_eye")
        self.face_shape = QtWidgets.QLabel(self.groupBox_5)
        self.face_shape.setGeometry(QtCore.QRect(80, 210, 91, 16))
        self.face_shape.setObjectName("face_shape")
        self.face_type = QtWidgets.QLabel(self.groupBox_5)
        self.face_type.setGeometry(QtCore.QRect(80, 240, 91, 16))
        self.face_type.setObjectName("face_type")
        self.face_location = QtWidgets.QLabel(self.groupBox_5)
        self.face_location.setGeometry(QtCore.QRect(110, 270, 91, 16))
        self.face_location.setObjectName("face_location")
        self.face_size = QtWidgets.QLabel(self.groupBox_5)
        self.face_size.setGeometry(QtCore.QRect(110, 300, 91, 16))
        self.face_size.setObjectName("face_size")
        self.groupBox_6 = QtWidgets.QGroupBox(Form)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 80, 221, 241))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 72, 15))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(10, 90, 72, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 72, 15))
        self.label_8.setObjectName("label_8")
        self.label_19 = QtWidgets.QLabel(self.groupBox_6)
        self.label_19.setGeometry(QtCore.QRect(10, 150, 72, 15))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_6)
        self.label_20.setGeometry(QtCore.QRect(10, 180, 72, 15))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_6)
        self.label_21.setGeometry(QtCore.QRect(10, 210, 72, 15))
        self.label_21.setObjectName("label_21")
        self.course_name = QtWidgets.QLabel(self.groupBox_6)
        self.course_name.setGeometry(QtCore.QRect(110, 30, 111, 16))
        self.course_name.setObjectName("course_name")
        self.teacher_name = QtWidgets.QLabel(self.groupBox_6)
        self.teacher_name.setGeometry(QtCore.QRect(110, 60, 111, 16))
        self.teacher_name.setObjectName("teacher_name")
        self.class_name = QtWidgets.QLabel(self.groupBox_6)
        self.class_name.setGeometry(QtCore.QRect(110, 90, 111, 16))
        self.class_name.setObjectName("class_name")
        self.start_day = QtWidgets.QLabel(self.groupBox_6)
        self.start_day.setGeometry(QtCore.QRect(110, 120, 111, 16))
        self.start_day.setObjectName("start_day")
        self.start_time = QtWidgets.QLabel(self.groupBox_6)
        self.start_time.setGeometry(QtCore.QRect(110, 150, 111, 16))
        self.start_time.setObjectName("start_time")
        self.end_time = QtWidgets.QLabel(self.groupBox_6)
        self.end_time.setGeometry(QtCore.QRect(110, 180, 111, 16))
        self.end_time.setObjectName("end_time")
        self.remarks = QtWidgets.QLabel(self.groupBox_6)
        self.remarks.setGeometry(QtCore.QRect(80, 210, 141, 16))
        self.remarks.setObjectName("remarks")
        self.groupBox_7 = QtWidgets.QGroupBox(Form)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 420, 221, 151))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_22 = QtWidgets.QLabel(self.groupBox_7)
        self.label_22.setGeometry(QtCore.QRect(0, 40, 81, 16))
        self.label_22.setObjectName("label_22")
        self.current_datetime = QtWidgets.QLabel(self.groupBox_7)
        self.current_datetime.setGeometry(QtCore.QRect(30, 70, 181, 16))
        self.current_datetime.setObjectName("current_datetime")
        self.groupBox_8 = QtWidgets.QGroupBox(Form)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 609, 221, 91))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_23 = QtWidgets.QLabel(self.groupBox_8)
        self.label_23.setGeometry(QtCore.QRect(10, 30, 72, 15))
        self.label_23.setObjectName("label_23")
        self.connect_info = QtWidgets.QLabel(self.groupBox_8)
        self.connect_info.setGeometry(QtCore.QRect(31, 60, 161, 21))
        self.connect_info.setObjectName("connect_info")
        self.exitBtn = QtWidgets.QPushButton(Form)
        self.exitBtn.setGeometry(QtCore.QRect(1150, 760, 93, 28))
        self.exitBtn.setObjectName("exitBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.startDetectionBtn.setText(_translate("Form", "开始检测"))
        self.stopDetectionBtn.setText(_translate("Form", "暂停检测"))
        self.label_24.setText(_translate("Form", "课堂异常行为检测系统V1.0"))
        self.groupBox_4.setTitle(_translate("Form", "个人信息(Student)"))
        self.label.setText(_translate("Form", "学号:"))
        self.label_2.setText(_translate("Form", "姓名:"))
        self.label_3.setText(_translate("Form", "性别:"))
        self.label_4.setText(_translate("Form", "年龄:"))
        self.student_no.setText(_translate("Form", "#None"))
        self.student_name.setText(_translate("Form", "#None"))
        self.gender.setText(_translate("Form", "#None"))
        self.age.setText(_translate("Form", "#None"))
        self.groupBox_5.setTitle(_translate("Form", "检测信息(Detection)"))
        self.label_9.setText(_translate("Form", "在线:"))
        self.label_10.setText(_translate("Form", "本人:"))
        self.label_11.setText(_translate("Form", "眼镜:"))
        self.label_12.setText(_translate("Form", "表情:"))
        self.label_13.setText(_translate("Form", "左眼:"))
        self.label_14.setText(_translate("Form", "右眼:"))
        self.label_15.setText(_translate("Form", "脸型:"))
        self.label_16.setText(_translate("Form", "活体:"))
        self.label_17.setText(_translate("Form", "人脸位置:"))
        self.label_18.setText(_translate("Form", "人脸大小:"))
        self.online.setText(_translate("Form", "#None"))
        self.isme.setText(_translate("Form", "#None"))
        self.glass.setText(_translate("Form", "#None"))
        self.emotion.setText(_translate("Form", "#None"))
        self.left_eye.setText(_translate("Form", "#None"))
        self.right_eye.setText(_translate("Form", "#None"))
        self.face_shape.setText(_translate("Form", "#None"))
        self.face_type.setText(_translate("Form", "#None"))
        self.face_location.setText(_translate("Form", "#None"))
        self.face_size.setText(_translate("Form", "#None"))
        self.groupBox_6.setTitle(_translate("Form", "课程信息(Course)"))
        self.label_5.setText(_translate("Form", "课程名称:"))
        self.label_6.setText(_translate("Form", "教师姓名:"))
        self.label_7.setText(_translate("Form", "教课班级:"))
        self.label_8.setText(_translate("Form", "开始日期:"))
        self.label_19.setText(_translate("Form", "开始时间:"))
        self.label_20.setText(_translate("Form", "结束时间:"))
        self.label_21.setText(_translate("Form", "备注:"))
        self.course_name.setText(_translate("Form", "#None"))
        self.teacher_name.setText(_translate("Form", "#None"))
        self.class_name.setText(_translate("Form", "#None"))
        self.start_day.setText(_translate("Form", "#None"))
        self.start_time.setText(_translate("Form", "#None"))
        self.end_time.setText(_translate("Form", "#None"))
        self.remarks.setText(_translate("Form", "#None"))
        self.groupBox_7.setTitle(_translate("Form", "Current DateTime"))
        self.label_22.setText(_translate("Form", "当前时间:"))
        self.current_datetime.setText(_translate("Form", "#None"))
        self.groupBox_8.setTitle(_translate("Form", "Connection State"))
        self.label_23.setText(_translate("Form", "连接信息:"))
        self.connect_info.setText(_translate("Form", "<html><head/><body><p>#None</p></body></html>"))
        self.exitBtn.setText(_translate("Form", "切换/退出"))


class DetectionWindows(QWidget, Ui_Detection):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Online-Detection System")

        self.sendThreadFlag = False
        self.pixMapImage = None
        self.predict_data = None
        self.search_data = None
        self.current_datetime_data = None
        self.online_value = None
        self.isme_value = None
        self.glass_value = None
        self.emotion_value = None
        self.left_eye_value = None
        self.right_eye_value = None
        self.face_shape_value = None
        self.face_type_value = None
        self.face_size_value = None
        self.face_location_value = None
        self.face_size_value = None

        self.startDetectionBtn.clicked.connect(self.startDetectionThread)
        self.stopDetectionBtn.clicked.connect(self.stopDetectionThread)
        self.exitBtn.clicked.connect(self.exitMainWindow)
        self.stopDetectionBtn.setEnabled(False)


        self.connect_info.setStyleSheet("color:red;")
        self.connect_info.setText("未连接")

        self.course = Course()

        self.setMyselfData()
        self.setCourseData()
        self.startDateTimeThead()

    def setMyselfData(self):
        self.student_no.setText(share.currentUser[1])
        self.student_name.setText(share.currentUser[3])
        self.gender.setText(share.currentUser[4])
        self.age.setText(str(share.currentUser[5]))

    def setCourseData(self):

        self.currentCourse = None
        self.data = self.course.selectMyAllCourses()

        for i in range(0, len(self.data)):
            if self.data[i][4] == getCurrentDay():
                if self.data[i][5] <= getCurrentTime() and self.data[i][6] >= getCurrentTime():
                    self.currentCourse = self.data[i]
                    break

        self.course_name.setText(self.currentCourse[1])
        self.teacher_name.setText(self.currentCourse[2])
        self.class_name.setText(self.currentCourse[3])
        self.start_day.setText(self.currentCourse[4])
        self.start_time.setText(self.currentCourse[5])
        self.end_time.setText(self.currentCourse[6])
        self.remarks.setText(self.currentCourse[7])

    def startDateTimeThead(self):
        self.nowDateTimeThread = NowDateTimeThread()
        self.nowDateTimeThread.valueChange.connect(self.printDateTime)
        self.nowDateTimeThread.start()

    def printDateTime(self, datetime):
        self.current_datetime_data = datetime
        self.current_datetime.setText(datetime)

    def startDetectionThread(self):

        try:
            self.s = socket.socket()  # 创建 socket 对象
            host = socket.gethostname()  # 获取本地主机名
            port = 12345  # 设置端口号
            self.s.connect((host, port))
        except:
            QMessageBox().warning(self, "FAIL", "老师暂未开课, 请稍等片刻!!!")
            return


        self.detectionThread = DetectionThread()
        self.discernThread = DiscernThread()
        self.predictThread = PredictThread()
        self.sendMessageThread = Thread(target=self.sendMessage)


        self.detectionThread.valueChange.connect(self.printImage)
        self.discernThread.valueChange.connect(self.printDiscern)
        self.predictThread.valueChange.connect(self.printPredict)

        self.detectionThread.start()
        self.discernThread.start()
        self.predictThread.start()
        self.sendMessageThread.start()

        self.startDetectionBtn.setEnabled(False)
        self.stopDetectionBtn.setEnabled(True)

    def stopDetectionThread(self):

        self.detectionThread.cancel()
        self.discernThread.cancel()
        self.predictThread.cancel()
        self.sendThreadFlag = False

        self.stopDetectionBtn.setEnabled(False)
        self.startDetectionBtn.setEnabled(True)


    def printImage(self, image):
        self.pixMapImage = image
        self.screen_label.setPixmap(image)

    def printDiscern(self, data):
        self.search_data = data

        if data['result'] == None:
            self.isme.setStyleSheet("color:red;")
            self.isme.setText("否")
            self.isme_value = "否"
            return

        if data['error_code'] == 0 and data['result']['user_list'][0]['score'] >= 90:
            self.isme.setStyleSheet("color:green;")
            self.isme.setText("是")
            self.isme_value = "是"
        else:
            self.isme.setStyleSheet("color:blue;")
            self.isme.setText("系统故障...")
            self.isme_value = "系统故障..."

    def printPredict(self, data):
        self.predict_data = data

        if data['error_msg'] == "pic not has face":
            self.online.setStyleSheet("color:red;")
            self.online.setText("NOT FACE!!!")
            self.online_value = "NOT FACE!!!"

            self.glass.setText("#None")
            self.glass_value = "#None"

            self.emotion.setText("#None")
            self.emotion_value = "#None"

            self.left_eye.setText("#Node")
            self.left_eye_value = "#Node"

            self.right_eye.setText("#None")
            self.right_eye_value = "#None"

            self.face_shape.setText("#None")
            self.face_shape_value = "#None"

            self.face_type.setText("#None")
            self.face_type_value = "#None"

            self.face_location.setText("#None")
            self.face_location_value = "#None"

            self.face_size.setText("#None")
            self.face_size_value = "#None"

            return

        self.online.setStyleSheet("color:green;")
        self.online.setText("在线")
        self.online_value = "在线"

        if data['result']['face_list'][0]['glasses']['type'] == 'none':
            self.glass.setText("无")
            self.glass_value = "无"
        else:
            self.glass.setText("有")
            self.glass_value = "有"

        if data['result']['face_list'][0]['emotion']['type'] == "angry":
            self.emotion.setText("生气")
            self.emotion_value = "生气"
        elif data['result']['face_list'][0]['emotion']['type'] == "disgust":
            self.emotion.setText("厌恶")
            self.emotion_value = "厌恶"
        elif data['result']['face_list'][0]['emotion']['type'] == "fear":
            self.emotion.setText("恐惧")
            self.emotion_value = "恐惧"
        elif data['result']['face_list'][0]['emotion']['type'] == "happy":
            self.emotion.setText("高兴")
            self.emotion_value = "高兴"
        elif data['result']['face_list'][0]['emotion']['type'] == "sad":
            self.emotion.setText("伤心")
            self.emotion_value = "伤心"
        elif data['result']['face_list'][0]['emotion']['type'] == "surprise":
            self.emotion.setText("惊讶")
            self.emotion_value = "惊讶"
        elif data['result']['face_list'][0]['emotion']['type'] == "neutral":
            self.emotion.setText("正常")
            self.emotion_value = "正常"

        if data['result']['face_list'][0]['eye_status']['left_eye'] >= 0.50:
            self.left_eye.setText("正常")
            self.left_eye_value = "正常"
        else:
            self.left_eye.setText("疲劳")
            self.left_eye_value = "疲劳"

        if data['result']['face_list'][0]['eye_status']['right_eye'] >= 0.50:
            self.right_eye.setText("正常")
            self.right_eye_value = "正常"
        else:
            self.right_eye.setText("疲劳")
            self.right_eye_value = "疲劳"

        if data['result']['face_list'][0]['face_shape']['type'] == "square":
            self.face_shape.setText("正方形")
            self.face_shape_value = "正方形"
        elif data['result']['face_list'][0]['face_shape']['type'] == "triangle":
            self.face_shape.setText("三角形")
            self.face_shape_value = "三角形"
        elif data['result']['face_list'][0]['face_shape']['type'] == "oval":
            self.face_shape.setText("椭圆形")
            self.face_shape_value = "椭圆形"
        elif data['result']['face_list'][0]['face_shape']['type'] == "heart":
            self.face_shape.setText("心形")
            self.face_shape_value = "心形"
        elif data['result']['face_list'][0]['face_shape']['type'] == "round":
            self.face_shape.setText("圆形")
            self.face_shape_value = "圆形"
        if data['result']['face_list'][0]['face_type']['type'] == "human":
            self.face_type.setText("是")
            self.face_type_value = "是"
        else:
            self.face_type.setText("否")
            self.face_type_value = "否"

        self.face_location.setText(str(int(data['result']['face_list'][0]['location']['left'])) + "," + str(int(data['result']['face_list'][0]['location']['top'])))
        self.face_location_value= str(int(data['result']['face_list'][0]['location']['left'])) + "," + str(int(data['result']['face_list'][0]['location']['top']))

        self.face_size.setText(str(data['result']['face_list'][0]['location']['width']) + "," + str(data['result']['face_list'][0]['location']['height']))
        self.face_size_value = str(data['result']['face_list'][0]['location']['width']) + "," + str(data['result']['face_list'][0]['location']['height'])

    def sendMessage(self):
        self.sendThreadFlag = True

        self.connect_info.setStyleSheet("color:green")
        self.connect_info.setText("已连接")

        while True:

            if self.sendThreadFlag == False:
                break

            self.send_data = {
                "student_id":share.currentUser[0],
                "student_name":share.currentUser[3],
                "gender":share.currentUser[4],
                "age":str(share.currentUser[5]),
                "online":self.online_value,
                "isme":self.isme_value,
                "glass":self.glass_value,
                "emotion":self.emotion_value,
                "left_eye":self.left_eye_value,
                "right_eye":self.right_eye_value,
                "face_shape":self.face_shape_value,
                "face_type":self.face_type_value,
                "face_size":self.face_size_value,
                "location":self.face_location_value,
                "current_time":self.current_datetime_data
            }

            try:
                json_data = json.dumps(self.send_data)  # json对dict进行格式化
                self.s.send(json_data.encode("utf-8"))
            except:
                break

            time.sleep(0.5)

        self.s.close()
        if self.sendThreadFlag == True:
            self.connect_info.setText("老师断开连接!!!")
        else:
            self.connect_info.setText("未连接!!!")
        self.connect_info.setStyleSheet("color:red")

        if self.sendThreadFlag == True:
            self.stopDetectionThread()

    def exitMainWindow(self):

        if self.stopDetectionBtn.isEnabled() == True:
            QMessageBox().warning(self, "FAIL", "暂停检测后才可以进行退出!!!")
            return
        else:
            share.detectionWindow.hide()
            share.mainWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = DetectionWindows()
    example.show()
    sys.exit(app.exec_())

