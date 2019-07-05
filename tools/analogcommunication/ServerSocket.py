# coding=UTF-8
# python version=3.5
import socket
import sys
import time
import threading


class ServerSocket(object):

    conn = None
    addr = None
    mesStr = []
    recv = ''
    name = 'a'
    threadLock1 = threading.Lock()
    """docstring for ServerSocket"""

    def __init__(self):
        super(ServerSocket, self).__init__()

    """init"""

    def __init__(self, conn, addr):
        print('start acc')
        self.conn = conn
        self.addr = addr
        # 两个线程是分别处理的，接收的信息经过处理, 再发送
        # 接收请求
        threading.Thread(target=self.startAcceptClientInfo, args=(self,)).start()
        # 发送信息
        threading.Thread(target=self.startSendClientInfo, args=(self,)).start()

    def sendInfo(self, data):
        # self.conn.send(data)
        # self.threadLock1.acquire()
        self.mesStr.append(data)
        print('send %s' % data)
        # self.threadLock1.release()

    # 发送给请求端

    def startSendClientInfo(self):
        global isClose
        while not isClose:
            # time.sleep(1)
            # self.threadLock1.acquire()
            if self.conn is None:
                break
            if self.mesStr is None or not self.mesStr or not len(self.mesStr):
                continue

            try:
                for x in self.mesStr:
                    print('sen one:' + x)
                    self.conn.send(bytes(x, 'utf-8'))
                self.mesStr = []
                pass
            except Exception as e:
                print('conn close')
                self.release()
                break
            # self.threadLock1.release()
            print('end cur send loop')
        pass

    # 接收请求端的信息

    def startAcceptClientInfo(self):
        global isClose
        global msgList
        print('cur msgList:' + str(msgList))
        while not isClose:
            if self.conn is None:
                print('conn close')
                break
            try:
                self.recv = (self.conn.recv(buffSize))
                pass
            except Exception as e:
                print('conn close')
                self.release()
                break
            finally:
                pass
            if self.recv is None or self.recv.decode('utf-8') == '':
                continue
            # threadLock.acquire()
            if msgList is None or msgList.get(self.name) is None:
                print('set msg')
                msgList[self.name] = ''
            print('recv data:' + self.recv.decode('utf-8'))
            msgList[self.name] = msgList.get(self.name, '') + ';' + self.recv.decode('utf-8')
            print('cur send client:' + msgList[self.name])
            self.recv = ''
            # threadLock.release()
            # time.sleep(1)
        print('end cur')
        pass

    def release(self):
        self.mesStr = []
        self.recv = ''
        if self.conn is not None:
            self.conn.close()
            self.conn = None


buffSize = 1024
# 连接到服务端的客户端
clientList = {}
# 连接服务器去请求内网的
linkList = {}

global isClose
isClose = False
# 客户端登陆
global connMain


def startAcceptClient(addrs, port):
    ip_port = (addrs, port)
    # 生成句柄
    webSer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    webSer.bind(ip_port)
    # 最多连接数
    webSer.listen(1)
    while not isClose:
        print("waiting...")
        # 阻塞
        conn, addr = webSer.accept()
        print(addr)
        # isEq = False
        # if addr not in linkList.keys():
        #     for x in linkList.keys():
        #         if x[0] == addr[0] and x[1] == addr[1]:
        #             isEq = True
        #             break
        #         pass
        #     if isEq:
        #         continue
        if linkList and linkList.get(addr) is not None:
            linkList[addr].release()
        threadLock.acquire()
        linkList[addr] = ServerSocket(conn, addr)
        threadLock.release()
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

# 接收访问服务器的客户端信息


def recvData(clientAddr):
    global isClose
    global connMain
    print(connMain)
    conn = clientList[clientAddr]
    while not isClose:
        if conn is None:
            print('client no link')
            break
        recvData = conn.recv(buffSize)
        mesStr = recvData.decode('utf-8')
        if mesStr is None or mesStr == '':
            continue
        print('client send data:' + mesStr)
        threadLock.acquire()
        tmp = linkList.keys()
        for link in tmp:
            if link is None:
                continue
            print(mesStr)
            if mesStr.split(':')[0] == linkList[link].name:
                print(mesStr.split(':')[1])
                linkList[link].sendInfo(mesStr.split(':')[1])
        threadLock.release()
        print('end cur loop2')
        # time.sleep(1)
    pass

# 信息发送给内网客户端


def sendData(clientAddr):
    global msgList
    conn = clientList[clientAddr]
    global isClose
    while not isClose:
        if conn is None:
            print('client no link')
            break
        if not msgList:
            continue
        print(msgList)
        # threadLock.acquire()
        for keyConn in msgList.keys():
            if keyConn is None or keyConn == '' or not len(keyConn):
                continue
            print(keyConn + ':' + msgList[keyConn])
            for msgs in msgList[keyConn].split(';'):
                if msgs is None or msgs == '' or not len(msgs):
                    continue
                conn.send(bytes(keyConn + ':' + msgs, 'utf-8'))
        for keyConn in msgList.keys():
            msgList[keyConn] = ''
        msgList = {}
        # self.conn.send(bytes(self.mesStr, 'utf-8'))
        # threadLock.release()
        print('end loop4')
    pass


def startRecvAndSend(clientAddr):
    threading.Thread(target=recvData, args=(clientAddr,)).start()
    threading.Thread(target=sendData, args=(clientAddr,)).start()
    pass


# 客户端信息


def startMainServer():
    global connMain
    ip_port = ('localhost', 60007)
    # 生成句柄
    webMainSer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    webMainSer.bind(ip_port)
    # 最多连接数
    webMainSer.listen(1)
    while not isClose:
        print("waiting client...")
        # 阻塞
        connMain, clientAddr = webMainSer.accept()
        print('new client:' + str(clientAddr))
        clientList[clientAddr] = connMain
        startRecvAndSend(clientAddr)
    pass


threadLock = threading.Lock()
global msgList
msgList = {}
webMainSer = None
if __name__ == '__main__':
    # 开启ip和端口
    ip_port = ('192.168.0.214', 60017)

    threading.Thread(target=startAcceptClient, args=ip_port).start()
    try:
        startMainServer()
        pass
    except Exception as e:
        isClose = True
        for x in clientList:
            x.close()
            pass
        for x in linkList:
            x.close
        if webMainSer:
            webMainSer.close()
        raise
    else:
        pass
    finally:
        pass
    print('end main')
