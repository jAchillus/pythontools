# coding=UTF-8
# python version=3.5

import socketserver as ss
import socket

udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('10.45.22.54', 3001)
udpClient.connect(address)
udpClient.sendto(b'hi', address)
data = udpClient.recvfrom(1024)
print(data)
