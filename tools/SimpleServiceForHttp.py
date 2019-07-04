# coding:utf-8
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys
import threading


class RequestHandler(BaseHTTPRequestHandler):

    def _writeheaders(self):
        print(self.path)
        print(self.headers)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_Head(self):
        self._writeheaders()

    def do_GET(self):
        self._writeheaders()
        print("client" + self.address_string())
        rsp = (self.address_string()+str(self.headers)).encode('utf-8')
        self.wfile.write(rsp)

    def do_POST(self):
        self._writeheaders()
        length = self.headers.getheader('content-length')
        nbytes = int(length)
        data = self.rfile.read(nbytes)
        rsp = ("""<!DOCTYPE HTML><html lang="en-US"><head><meta charset="UTF-8"><title></title></head><body><p>his is post!</p></body></html>"""+str(self.headers)+str(self.command)+str(self.headers.dict)+data).encode('utf-8')
        self.wfile.write(rsp)


def inp():
    age = input()
    print(age)
    if age == 'e':
        sys.exit(0)
    else:
        inp()
    pass

try:
    threading.Thread(target=inp).start()
    addr = ('', 8764)
    server = HTTPServer(addr, RequestHandler)
    server.serve_forever()
    pass
except Exception as e:
    raise e
finally:
    sys.exit(0)
    pass
