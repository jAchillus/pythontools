# -*- coding:utf-8 -*-
import urllib.request


class WebRequest(object):
    """网页数据对象"""

    def __init__(self, url, type='GET', headers={}):
        super(WebRequest, self).__init__()
        self.req = urllib.request.Request(url)
        self.headers = headers
        for key, value in headers.items():
            req.add_header(key, value)
            pass

    def getRequest(self):
        return self.req

    def getResponse(self):

        return urllib.request.urlopen(self.req)


web = WebRequest('http://www.baidu.com', {'User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'})
with urllib.request.urlopen(web.req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
