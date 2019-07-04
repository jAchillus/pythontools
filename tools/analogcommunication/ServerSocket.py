# coding=UTF-8
# python version=3.5
import socket
import sys
import time
import threading


class ServerSocket(object):

    conn = None
    addr = None
    mesStr = None
    """docstring for ServerSocket"""

    def __init__(self, arg):
        super(ServerSocket, self).__init__()
        self.arg = arg

    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        threading.Thread(target=ServerSocket.startAcceptClientInfo, args=(self,)).start()
        threading.Thread(target=ServerSocket.startSendClientInfo, args=(self,)).start()

    def sendInfo(self, data):
        self.conn.send(data)

    def startSendClientInfo(self):
        while True:
            time.sleep(1)
            if self.mesStr is None or self.mesStr == '':
                continue
            addr = (self.addr[0], int(self.mesStr.split(',')[0]))

            print(addr)
            if addr in clientList.keys():
                clientList[addr].sendInfo(bytes(self.mesStr, 'utf-8'))
            else:
                print('error')
            self.mesStr = ''
        pass

    def startAcceptClientInfo(self):
        while True:
            if self.conn is None:
                continue
            recvData = self.conn.recv(buffSize)
            self.mesStr = recvData.decode('utf-8')
            # print(mesStr)
            if self.mesStr is None or self.mesStr == '':
                continue
            print(self.mesStr)
            # self.conn.send(bytes(self.mesStr, 'utf-8'))
            if self.mesStr == 'end':
                print('close')
                isClode = True
                return
            pass
        time.sleep(1)
        pass
# 开启ip和端口
ip_port = ('localhost', 60007)
buffSize = 1024
# 生成句柄
webSer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientList = {}
# 绑定端口
webSer.bind(ip_port)
# 最多连接数
webSer.listen(5)
isClode = False
# 客户端登陆


def startAcceptClient():
    while True:
        print("waiting...")
        if isClode:
            print('close1')
            break
        # 阻塞
        conn, addr = webSer.accept()
        clientList[addr] = ServerSocket(conn, addr)
        print(addr)
        # 获取客户端请求数据
        # recvData = conn.recv(buffSize)
        # 打印接受数据 注：当浏览器访问的时候，接受的数据的浏览器的信息等。
        # print(b'get:' + recvData)
        # print(addr)
        # print(conn.getsockname())
        # print(conn.getpeername())
        # 向对方发送数据
        # conn.send(bytes('<h1>welcome</h1>', 'utf8'))
        # 关闭链接
        # conn.close()
        # break
    pass

# 客户端信息


if __name__ == '__main__':
    threading.Thread(target=startAcceptClient).start()
