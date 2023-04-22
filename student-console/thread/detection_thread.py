import time

import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
import sys

from commons import share


class DetectionThread(QThread):
    # 线程值信号
    valueChange = pyqtSignal(QPixmap)

    # 构造函数
    def __init__(self):
        super(DetectionThread, self).__init__()
        self.isPause = False            #用户点击暂停按钮
        self.isCancel = False           #用户点击取消按钮
        self.cond = QWaitCondition()        #wait() 阻塞等待，awake() 唤醒才继续往下执行。
        self.mutex = QMutex()               #互斥锁，临界资源只可以进行互斥访问


    # 暂停
    def pause(self):
        print("线程暂停")
        self.isPause = True

    # 恢复
    def resume(self):
        print("线程恢复")
        self.isPause = False
        self.cond.wakeAll()

    # 取消
    def cancel(self):
        print("线程取消")
        self.isCancel = True

    # 运行(入口)
    def run(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            # 线程锁on
            self.mutex.lock()
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                break

            ok, img = cap.read()

            share.image = img                   # 存入当前待检测的人脸变量之中
            share.detectionFlag = True          # 允许人脸识别模块进行分析检测

            img = cv2.flip(img, 1)

            # label_img = cv2.resize(img, (640, 480))

            label_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            show_img = QImage(label_img.data, label_img.shape[1], label_img.shape[0], QImage.Format_RGB888)

            # cv2.imshow("Vedio", img)
            # print("The type of img is -------------------->", type(img), img)
            # print("The type of showImage is -------------------->", type(show_img), show_img)
            pix = QPixmap.fromImage(show_img)
            # 业务代码
            self.valueChange.emit(pix)      # 任务线程发射信号用于与图形化界面进行交互
            time.sleep(0.001)
            # 线程锁off
            self.mutex.unlock()


        img = QPixmap('../images/gray_img.jpg')
        pix = QPixmap(img)
        self.valueChange.emit(pix)

        share.detectionFlag = False             #人脸检测标志位再次重置为Fasle