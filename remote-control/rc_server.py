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
    b_cmd = c.recv(100)
    cmd = bytes.decode(b_cmd)

    if cmd == 'quit':
        c.send(str.encode('DISCONNECT'))        # data sent should be 'bytes', using str.encode(...)
        break
    elif cmd == 'list':
        files = os.listdir('.')
        b_filenames = str.encode('\n'.join(files))
        s_content = b'-----Files under ccurrent directory:-----\n'
        s_content += b_filenames
        s_content += b'\n----------'
        c.send(s_content)
    else:
        c.send(b'UNKNOWN')                        # data sent should be 'bytes', using prefix 'b' alternatively

c.close()