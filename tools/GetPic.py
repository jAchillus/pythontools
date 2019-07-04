# -*- coding: utf-8 -*-
import sys
import urllib
import urllib.request
import re
import os
import traceback
'''
获取网络图片
'''


class GetWebPic(object):
    # 地址
    url = None
    # 请求的数据
    postDict = {}
    requst = None
    cookie = None
    opener = None
    """docstring for GetWebTest"""

    def __init__(self, url, postData=None):
        super(GetWebPic, self).__init__()
        self.url = url
        self.postDict = postData
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))

    def log(self, msg):
        print(msg)
        pass

    # 获取请求
    def getReq(self):
        if self.requst is None:
            self.requst = urllib.request.Request(url=self.url, data=self.postDict)
        return self.requst
        pass
    # 获取网页

    def getWebByBuild(self):
        result = self.opener.open(self.getReq())
        return result

    def getWebByUrl(self):
        req = urllib.request.urlopen(self.getReq())
        return req


def getWebByUrlIp(url):
    req = urllib.request.urlopen(url)
    return req


def parseRe(data, reg):
    imgre = re.compile(reg)
    imglist = re.findall(imgre, data)
    return imglist
    pass
'''处理图片 '''


def dealImg(url, x=0, regOld=None):

    #t = GetWebPic(url)

    response = getWebByUrlIp(url).read()
    response = response.decode('UTF-8')
    if regOld:
        reg = regOld
    else:
        reg = r'src="(http:.+?\.(jpe{0,1}g|gif|png))" '
    imglist = parseRe(response, reg)

    for imgurl in imglist:
        urlData = imgurl[0]
        print("%s : %s" % (x, urlData))
        di = urlData.split('.')

        urllib.request.urlretrieve(urlData, 'D://own//img//%s.%s' % (x, di[len(di) - 1]))
        x += 1
        break
    pass


if __name__ == '__main1__':
    try:
        print(sys.version)
        url = 'http://music.163.com/api/playlist/detail?id=3779629'
        #url = 'http://www.nipic.com/photo/index.html'
        x = 340
        reg = r'"mp3Url":"(http:.+?\.(mp3))",'
        #dealImg(url, x, reg)
        pass
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise
    else:
        pass
    finally:
        os._exit(0)
        pass
