# -*- coding: utf-8 -*-
import sys
# print(sys.version)
# 获取网页，爬虫
import urllib
import re
# import requests
from bs4 import BeautifulSoup
# import urllib2
#import cookielib
import urllib.request


def print0(msg):
    print(msg)


def getHtml(url):
    # page = urllib.urlopen(url)
    # html = page
    pass
# html = getHtml('http://www.baidu.com')
html = ''
print(html)
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
}


class GetWebTest(object):
    # 地址
    url = None
    # 请求的数据
    postDict = None
    requst = None
    cookie = None
    opener = None
    """docstring for GetWebTest"""

    def __init__(self, url, postData=None):
        super(GetWebTest, self).__init__()
        self.url = url
        self.postDict = postData
        #self.cookie = cookielib.CookieJar()
        #self.opener = urllib.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib.request.urlopen(url)
        self.opener = urllib.request.urlopen(url)

    def log(self, msg):
        print0(msg)
        pass
    # 获取请求

    def getReq(self):
        if self.requst is None:
            self.requst = urllib.Request(url=self.url, data=self.postDict)
        return self.requst
        pass
        # 获取网页

    # def getWebByBuild(self):
    #    result = self.opener.open(self.getReq())
    #    return result

    def getWebByUrl(self):
        # req = urllib2.urlopen(url = self.url, data = self.postDict)
        req = urllib.request.urlopen(url=self.url, data=self.postDict)
        return req

if __name__ == '__main__':
    #需要POST的数据#
    # postdata=urllib.urlencode({
    #     'stuid':'201100300428',
    #     'pwd':'921030'
    # })
    #t = GetWebTest('http://www.baidu.com')
    # t.log(sys.version)
    #response = t.getWebByUrl().read()
    # print t.getWebByUrl().read()
    # print0(response)
    # print0(type(response))
    # t.getWebByUrl().geturl()
    # print0('分')
    #repList = re.findall('http(.)?://(.*)[;,}]', response)
    # print0(repList)
    # for item in repList:
    #    print0("Num:")
    #    print0(item)
    soup = BeautifulSoup(open('http://www.baidu.com', 'r'), 'lxml')
    print0(soup.title)
