#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket 模块
from threading import Thread

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(50)  # 等待客户端连接


def acceptClient():
    while True:
        client, addr = s.accept()  # 建立客户端连接
        thread = Thread(target=printMsg, args=(client,))
        thread.start()

def printMsg(client_socket):
    print(client_socket)
    while True:
        # print(client_socket)
        data = client_socket.recv(1024).decode("utf-8")

        if data != None and data != '':
            print(data)

        # client_socket.send("检测成功!!!".encode("utf-8"))


if __name__ == '__main__':
    acceptClient()