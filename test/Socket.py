import socket
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.connect(('www.baidu.com', 80))
print 'done...'
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
import logging  
from suds.client import Client
if __name__ == '__main__':  
    logging.basicConfig(level=logging.INFO)  
    logging.getLogger('suds.client').setLevel(logging.DEBUG)  
    hello_client = Client('http://localhost:8080/testWebService/services/TestQryInfo?wsdl', cache=None)  
    result = hello_client.service.qrySex(0)
    print result
