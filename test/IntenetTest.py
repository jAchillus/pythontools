# coding=UTF-8
import socket
try:
    lis = [60007]
    for x in lis:
        ip_port = ('localhost', x)
        try:
            # 生成句柄
            web = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            web.bind(('localhost', 55774))
            # 绑定端口
            conn = web.connect(ip_port)
            web.send(b"hello")
            # conn1, addr = web.accept()
            data = web.recv(1024)
            print(data)
            web.close()
            pass
        except Exception as e:
            raise e
            # print("%s,%d" % (e, x))
        finally:
            pass
        pass
    pass
except Exception as e:
    raise e
finally:
    web.close()
    pass
print('end')
