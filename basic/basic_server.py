# -*- coding: UTF-8 -*-
import os

'''
This is a simple socket server
'''
import socket               # 导入 socket 模块

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口

s.listen()                 # 等待客户端连接

c, addr = s.accept()     # 建立客户端连接
print('Connection Address %s:%d' % (addr[0], addr[1]))

while True:
    cmd = c.recv(2)
    print(cmd)
    if cmd == b'ls':
        files = os.listdir('.')
        for f in files:
            print(f)
            c.send(str.encode(f))