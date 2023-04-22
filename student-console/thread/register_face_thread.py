import base64
import time

import cv2
from PyQt5.QtCore import *

from commons import share
from commons.utils import image_to_base64
from properties import client


class RegisterThread(QThread):

    # 线程值信号
    valueChange = pyqtSignal(int)

    # 构造函数
    def __init__(self):
        super(RegisterThread, self).__init__()
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

        userId = share.currentUser[0]
        groupId = share.currentUser[6]
        imageType = "BASE64"

        for i in range(0, 20):

            while share.detectionFlag == False:         #线程锁，当未检测到人脸图片时, 暂时不执行
                pass

            # 线程锁on
            self.mutex.lock()
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                break

            image = image_to_base64(share.image)


            """ 调用人脸注册 """
            print(client.addUser(image, imageType, groupId, userId))


            # 业务代码
            self.valueChange.emit(i+1)      # 任务线程发射信号用于与图形化界面进行交互

            # 线程锁off
            self.mutex.unlock()
            time.sleep(0.5)
            share.detectionFlag = False

        while True:
            pass

        share.detectionFlag = False     #人脸检测标志位再次重置为Fasle

    def image_to_base64(self, image_np):
        image = cv2.imencode('.jpg', image_np)[1]
        image_code = str(base64.b64encode(image))[2:-1]

        return image_code

