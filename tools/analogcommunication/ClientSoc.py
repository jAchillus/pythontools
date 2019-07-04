# coding=UTF-8
# python version 3.5
import socket
import sys
import time
import threading

port = 55773
# 开启ip和端口
ip_port = ('localhost', port)
# 生成句柄
webClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
webClient.bind(ip_port)


def startClient():
    webClient.connect(('localhost', 60007))
    threading.Thread(target=startClientAccept).start()
    while True:
        content = input("input:")
        # 向对方发送数据
        webClient.send(bytes(content, 'utf8'))
        if content == 'end':
            break

        # break
    pass
    # 关闭链接
    webClient.close()


def startClientAccept():
    while True:
        if webClient is not None:
            mess = webClient.recv(1024)
            print(mess)
        time.sleep(1)
    pass
# def main1():
#     thread.start_new_thread(startClient, ())
    # thread.start_new_thread(loop1, ())

if __name__ == '__main__':
    print(port)
    # port = input("port input:")
    threading.Thread(target=startClient).start()
