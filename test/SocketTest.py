# coding=UTF-8
import socket
import sys
# so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# so.connect(('www.baidu.com', 80))
# from socket import *
# host = 'localhost'
# port = 8080
# bufsize = 1024
# addr = (host,port)
# tcpSock = socket(AF_INET,SOCK_STREAM)
# tcpSock.connect(addr)
# while True:
#     data = raw_input('>')
#     if not data:
#         break
#     tcpSock.send(data)
#     data = tcpSock.recv(bufsize)
#     if not data:
#         break
#     if data == 'exit':
#         break
#     print data
# tcpSock.close()
#
#

# 导入socket模块
import socket
# 开启ip和端口
ip_port = ('127.0.0.1', 65327)
# 生成句柄
web = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
web.bind(ip_port)
# 最多连接数
web.listen(5)
# 等待信息
print('waiting...')
i = 0
# 开启死循环
while True:
    # 阻塞
    conn, addr = web.accept()
    # 获取客户端请求数据
    data = conn.recv(1024)
    # 打印接受数据 注：当浏览器访问的时候，接受的数据的浏览器的信息等。
    print(data)
    # 向对方发送数据
    conn.send(bytes('<h1>welcome</h1>', 'utf8'))
    # 关闭链接
    conn.close()
    break
if None == '':
    print('hi')
print('end!')
