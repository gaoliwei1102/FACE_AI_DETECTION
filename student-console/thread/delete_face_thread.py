import base64
import time

import cv2
from PyQt5.QtCore import *

from commons import share
from commons.utils import image_to_base64
from properties import client


class DeleteThread(QThread):
    # 线程值信号
    valueChange = pyqtSignal(int)

    # 构造函数
    def __init__(self):
        super(DeleteThread, self).__init__()
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

        """ 调用获取用户人脸列表 """
        data = client.faceGetlist(userId, groupId)
        self.faceData = data['result']['face_list']

        for i in range(0, len(self.faceData)):

            # 线程锁on
            self.mutex.lock()
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                break

            faceToken = self.faceData[i]['face_token']

            """ 调用人脸删除 """
            result = client.faceDelete(userId, groupId, faceToken)


            # 业务代码
            self.valueChange.emit(i+1)      # 任务线程发射信号用于与图形化界面进行交互

            # 线程锁off
            self.mutex.unlock()
            time.sleep(0.5)

        while True:
            pass


