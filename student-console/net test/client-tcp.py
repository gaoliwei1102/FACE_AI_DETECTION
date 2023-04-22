#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket  # 导入 socket 模块
import time
import traceback
from properties import client

if __name__ == '__main__':
    s = socket.socket()             # 创建 socket 对象
    host = socket.gethostname()     # 获取本地主机名
    port = 12345                    # 设置端口号

    try:
        s.connect((host, port))
        while True:
            s.send("亮亮呀!".encode("utf-8"))
            # print(s.recv(1024).decode("utf-8"))

            time.sleep(2)
        s.close()

    except:
        print("连接失败!!!")

