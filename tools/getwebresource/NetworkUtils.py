#!python3
# -*- coding: utf-8 -*-

import urllib
import urllib.request

#import requests
'''
是否是path。简单的以是否http开头判断
'''


def isPathUrl(url):
    if url is not None and url.startswith('http'):
        return False
    return True


'''
获取url对应的连接（原始对象，无解析）
'''


def getWebByUrlIp(url):
    res = urllib.request.urlopen(url)
    return res


'''
获取原始的url返回数据，是byte类型
'''


def getWebByteByUrlIp(url):
    with urllib.request.urlopen(url) as rsp:
        return rsp.read()


'''
返回网址的数据，通过编码进行转义为string，默认utf-8
'''


def getWebDataByUrlIp(url, encode='utf-8'):
    return getWebByteByUrlIp(url).decode(encode)


def getRequest(url, header):

    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')


def getPageData(url, reg, isPrint=False):

    response = getWebDataByUrlIp(url)
    if isPrint:
        print(response)

    imglist = parseRe(response, reg)
    print("parse dataList:%s" % (imglist))
    return (response, imglist)


#print(getWebDataByUrlIp('http://www.baidu.com'))
