# -*- coding: cp936 -*-
##网络
from socket import *
from time import ctime

host =""
port = 21567
bufsize = 1024
addr = (host,port)
tcpSock = socket(AF_INET,SOCK_STREAM)
tcpSock.bind(addr)
tcpSock.listen(2)
while(True):
    print 'wait...'
    tcpCliSock , addr = tcpSock.accept()
    print '...',addr
    while True:
        data = tcpCliSock.recv(bufsize)
        if not data:
            break
        tcpCliSock.send('[%s} %s' % (ctime(),data))
    tcpCliSock.close()
tcpSock.close()
