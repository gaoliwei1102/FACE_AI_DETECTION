import base64
import datetime
import uuid

import cv2

#随机返回一个32位定长的id
def getRandomUUID():
    return str(uuid.uuid1()).replace("-", "")


#将普通格式的图片转化为base64格式的图片
def image_to_base64(image_np):
    image = cv2.imencode('.jpg', image_np)[1]
    image_code = str(base64.b64encode(image))[2:-1]

    return image_code


#获取当前日期
def getCurrentDay():
    return datetime.datetime.now().strftime('%Y-%m-%d')


#获取当前时间
def getCurrentTime():
    return datetime.datetime.now().strftime('%H:%M')

def getCurrentDateTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    print(getCurrentDateTime())