import base64
import time

import cv2
from PyQt5.QtCore import *

from commons import share
from properties import client


class PredictThread(QThread):
    # 线程值信号
    valueChange = pyqtSignal(dict)

    # 构造函数
    def __init__(self):
        super(PredictThread, self).__init__()
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
        self.imageType = "BASE64"

        while True:

            while share.detectionFlag == False:
                pass

            # 线程锁on
            self.mutex.lock()
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                break

            options = {}
            options[
                "face_field"] = "age,beauty,expression,face_shape,gender,glasses," \
                                "landmark,landmark72,landmark150,quality,eye_status,emotion,face_type"

            options["max_face_num"] = 2
            options["face_type"] = "LIVE"
            options["liveness_control"] = "LOW"


            base64_img = self.image_to_base64(share.image)
            data = client.detect(base64_img, self.imageType, options)

            # if (data['error_msg'] == 'pic not has face'):
            #     continue
            # print("检测结果:", data['error_msg'])
            # print("人脸数量:", data['result']['face_num'])
            # print("face_token:", data['result']['face_list'][0]['face_token'])
            # print("左边位置:", data['result']['face_list'][0]['location']['left'])
            # print("顶部位置:", data['result']['face_list'][0]['location']['top'])
            # print("宽度:", data['result']['face_list'][0]['location']['width'])
            # print("高度:", data['result']['face_list'][0]['location']['height'])
            # print("年龄:", data['result']['face_list'][0]['age'])
            # print("形象:", data['result']['face_list'][0]['beauty'])
            # print("表达:", data['result']['face_list'][0]['expression']['type'])
            # print("脸型:", data['result']['face_list'][0]['face_shape']['type'])
            # print("性别:", data['result']['face_list'][0]['gender']['type'])
            # print("有无眼镜:", data['result']['face_list'][0]['glasses']['type'])
            # print("情绪:", data['result']['face_list'][0]['emotion']['type'])

            # 业务代码
            self.valueChange.emit(data)      # 任务线程发射信号用于与图形化界面进行交互

            # 线程锁off
            self.mutex.unlock()
            time.sleep(0.5)

            share.detectionFlag = False

        share.detectionFlag = False         #人脸检测标志位再次重置为Fasle

    def image_to_base64(self, image_np):
        image = cv2.imencode('.jpg', image_np)[1]
        image_code = str(base64.b64encode(image))[2:-1]

        return image_code

