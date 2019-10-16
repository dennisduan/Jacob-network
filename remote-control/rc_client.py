# -*- coding: UTF-8 -*-

import socket               # 导入 socket 模块
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口号
 
s.connect((host, port))
print('Connected to server OK!')

# Simulate a command terminal 
while True:
    cmd = input('Commands>').strip()
    s.send(str.encode(cmd))
    ret = bytes.decode(s.recv(1024))
    if ret == 'UNKNOWN':
        print('Command unknown')
    elif ret == 'DISCONNECT':
        print('Exiting')
        break
    else:
        print(ret)

s.close()