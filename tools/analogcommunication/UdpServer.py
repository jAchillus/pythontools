# coding=UTF-8
# python version=3.5

import socketserver as ss
import socket

udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('10.45.22.54', 3001)
udpserver.bind(address)
# udp不支持，因为是非连接形式的
# udpserver.listen()
updClient, addr = udpserver.recvfrom(1024)
print(updClient)
udpserver.sendto(b'hi', addr)
