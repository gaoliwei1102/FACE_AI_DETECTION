import base64
import datetime
import socket
import time

from PyQt5.QtCore import *

from commons import share
# from view.py.Detection import DetectionWindows


class SendMessageThread(QThread):
    # 线程值信号
    valueChange = pyqtSignal(int)

    # 构造函数
    def __init__(self):
        super(SendMessageThread, self).__init__()
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

        s = socket.socket()  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        port = 12345  # 设置端口号
        s.connect((host, port))


        count = 0
        while True:

            # 线程锁on
            self.mutex.lock()
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                break

            # 业务代码

            # self.detectionWindow = DetectionWindows()
            # print(s.recv(1024).decode("utf-8"))


            # dict_data = {
            #     "image":self.detectionWindow.pixMapImage,
            #     "predict":self.detectionWindow.predict_data,
            #     "search":self.detectionWindow.search_data,
            #     "datetime":self.detectionWindow.current_datetime_data,
            #     "student":share.currentUser,
            # }
            print(self.data)

            # s.send("123".encode("utf-8"))


            self.valueChange.emit(count)            # 任务线程发射信号用于与图形化界面进行交互

            # 线程锁off
            self.mutex.unlock()
            count += 1
            time.sleep(1)

        while True:
            pass


