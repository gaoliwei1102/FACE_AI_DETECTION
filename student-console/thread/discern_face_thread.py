import base64
import time

import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
import sys

from commons import share
from properties import client


class DiscernThread(QThread):
    # 线程值信号
    valueChange = pyqtSignal(dict)

    # 构造函数
    def __init__(self):
        super(DiscernThread, self).__init__()
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

        groupIdList = share.currentUser[6]
        imageType = "BASE64"

        """ 如果有可选参数 """
        options = {}
        options["match_threshold"] = 80
        options["quality_control"] = "NORMAL"
        options["user_id"] = share.currentUser[0]
        options["max_user_num"] = 1

        while True:
            # 线程锁on
            self.mutex.lock()
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                break


            """ 带参数调用人脸搜索 """
            while share.detectionFlag == False:
                pass

            image_base64 = self.image_to_base64(share.image)


            concern_data = client.search(image_base64, imageType, groupIdList, options)

            self.valueChange.emit(concern_data)

            # 线程锁off
            self.mutex.unlock()

            time.sleep(0.5)
            share.detectionFlag = False

        share.detectionFlag = False

    #将普通图片类型转化为base64
    def image_to_base64(self, image_np):
        image = cv2.imencode('.jpg', image_np)[1]
        image_code = str(base64.b64encode(image))[2:-1]

        return image_code