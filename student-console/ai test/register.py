import base64
import time

import cv2

from properties import client


def image_to_base64(image_np):
    image = cv2.imencode('.jpg', image_np)[1]
    image_code = str(base64.b64encode(image))[2:-1]

    return image_code


if __name__ == '__main__':
    groupIdList = "3424001048b942d8890977e3f62293c1"
    imageType = "BASE64"

    """ 如果有可选参数 """
    options = {}
    options["match_threshold"] = 80
    options["quality_control"] = "NORMAL"
    options["user_id"] = "263d47552442480181671e4c3bf17ba1"
    options["max_user_num"] = 1

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        ok, img = cap.read()
        image = image_to_base64(img)


        options["liveness_control"] = "LOW"

        """ 带参数调用人脸检测 """
        print(client.search(image, imageType, groupIdList, options))

        cv2.imshow("windows", img)
        time.sleep(1)

        cv2.waitKey(1)








