# -*- coding: UTF-8 -*-

'''
This is a simple socket server
'''
import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口

s.listen()                 # 等待客户端连接

while True:
    c,addr = s.accept()     # 建立客户端连接
    print('Connection Address %s:%d' % (addr[0], addr[1]))
    c.send(b'Welcome to my server!')
    c.close()                # 关闭连接