# coding=UTF-8
#import SocketServer
import socketserver


class SocketServerChat(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.sendall(b'我是多线程')
        Flag = True
        while Flag:
            data = conn.recv(1024)
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall(b'您输入的是0')
            else:
                conn.sendall(b'请重新输入.')
server = socketserver.ThreadingTCPServer(('127.0.0.1', 8009), SocketServerChat)
server.serve_forever()
