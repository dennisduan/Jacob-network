# -*- coding: UTF-8 -*-

import socket               # 导入 socket 模块
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口号
 
s.connect((host, port))
s.send(b'ls')
while True:
    ret = s.recv(1024)
    print(ret)
s.close()