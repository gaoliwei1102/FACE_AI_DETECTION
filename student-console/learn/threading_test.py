#!/usr/bin/python3
# _*_ coding: utf-8 _*_

"""
@Software: PyCharm
@File: ac_job.py
@Author: 高留柱
@E-mail: liuzhu.gao@foxmail.com
@Time: 2020/9/19 10:30 上午
@Notes: 用于开启线程，执行ac_work中的任务
"""
import threading
import time

import cv2
from PyQt5.QtGui import QPixmap, QImage

from view.py import testDetection


class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()     # 用于暂停线程的标识

        self.__flag.set()       # 设置为True

        self.__running = threading.Event()      # 用于停止线程的标识

        self.__running.set()      # 将running设置为True

    def run(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while self.__running.isSet():
            print("Hello World!!!")
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            try:

                ok, img = cap.read()

                img = cv2.flip(img, 1)

                cv2.imshow("Hello", img)
                # label_img = cv2.resize(img, (640, 480))

                # label_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                #
                # show_img = QImage(label_img.data, label_img.shape[1], label_img.shape[0], QImage.Format_RGB888)
                #
                # # cv2.imshow("Vedio", img)
                # # print("The type of img is -------------------->", type(img), img)
                # # print("The type of showImage is -------------------->", type(show_img), show_img)
                #
                # pix = QPixmap.fromImage(show_img)
                # self.label.setPixmap(pix)
                # self.ui.screen_label.setPixmap(pix)
                # self.ui.date_label.setText(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                # self.ui.screen_label.setAlignment()

                cv2.waitKey(1)
                time.sleep(0.001)
                # hfac_work.start_ac()
            except Exception as e:
                # 如果任务失败，自动结束该线程，外层可用方法判断线程是否存活，从而判断任务是否失败。
                # return 方法在线程中不能使用
                self.stop()
                print(e)

    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


job = Job()
job.start()
job.stop()
# job.stop()