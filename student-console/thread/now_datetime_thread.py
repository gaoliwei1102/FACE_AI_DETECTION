import base64
import datetime
import time

from PyQt5.QtCore import *


class NowDateTimeThread(QThread):
    # 线程值信号
    valueChange = pyqtSignal(str)

    # 构造函数
    def __init__(self):
        super(NowDateTimeThread, self).__init__()
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

        while True:

            # 线程锁on
            self.mutex.lock()
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                break

            # 业务代码
            self.valueChange.emit(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))     # 任务线程发射信号用于与图形化界面进行交互

            # 线程锁off
            self.mutex.unlock()
            time.sleep(0.5)

        while True:
            pass


