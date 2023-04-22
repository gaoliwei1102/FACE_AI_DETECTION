import base64
import datetime
import json
import socket
import time
from threading import Thread

from PyQt5.QtCore import *

from commons import share
# from view.py.Detection import DetectionWindows


class QueryAllNotSignINThread(QThread):

    # 线程值信号
    valueChange = pyqtSignal(dict)

    # 构造函数
    def __init__(self, client_socket):
        super(QueryAllNotSignINThread, self).__init__()
        self.isPause = False            #用户点击暂停按钮
        self.isCancel = False           #用户点击取消按钮
        self.cond = QWaitCondition()        #wait() 阻塞等待，awake() 唤醒才继续往下执行。
        self.mutex = QMutex()               #互斥锁，临界资源只可以进行互斥访问
        self.client_socket = client_socket

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

        while True:

            # 线程锁on
            self.mutex.lock()
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                break

            try:
                data = self.client_socket.recv(1024).decode("utf-8")

                if data != None and data != '':
                    dict_data = json.loads(data)
                    self.valueChange.emit(dict_data)
            except:
                print("断开学生客户端---->", self.client_socket)
                break

            # 线程锁off
            self.mutex.unlock()




