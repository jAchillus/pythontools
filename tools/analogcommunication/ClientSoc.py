# coding=UTF-8
# python version 3.5
import socket
import sys
import time
import threading

port = 60007
# 开启ip和端口
server_ip_port = ('localhost', port)
# 生成句柄
webClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
global isclose
isclose = False
global isRecv
isRecv = ''


def startClient():
    global isclose
    global isRecv
    webClient.connect(server_ip_port)
    threading.Thread(target=startClientAccept).start()
    while True:
        if isRecv is None or isRecv == '':
            continue
        # server_ip_port = ('192.168.0.214', 60007)
        # 生成句柄
        webClient1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        webClient1.connect(('192.168.0.106', 6082))
        webClient1.send(bytes(isRecv.decode('utf-8').split(':')[1], 'utf-8'))

        content = isRecv.decode('utf-8').split(':')[0] + ':' + webClient1.recv(1024).decode('utf-8')
        # input("input:")
        # 向对方发送数据
        webClient.send(bytes(content, 'utf8'))
        isRecv = ''
        webClient1.close()
        if content == 'exit':
            isclose = True
            break
    # 关闭链接
    webClient.close()


def startClientAccept():
    global isRecv
    while True:
        if webClient is not None and not webClient._closed and not isclose:
            isRecv = webClient.recv(1024)
            print(isRecv)
    pass
# def main1():
#     thread.start_new_thread(startClient, ())
    # thread.start_new_thread(loop1, ())


if __name__ == '__main__':
    print(port)
    # port = input("port input:")
    threading.Thread(target=startClient).start()
