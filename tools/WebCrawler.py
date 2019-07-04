# -*- coding: utf-8 -*-
import sys
import urllib
import urllib.request
import re
import os
import traceback

'''
 获取网页数据
'''


def getWebByUrlIp(url):
    req = urllib.request.urlopen(url)
    return req

'''正则解析'''


def parseRe(data, reg):
    imgre = re.compile(reg)
    imglist = re.findall(imgre, data)
    return imglist
    pass

'''处理文件 '''


def dealFile(url, savePath, x=0, regOriginal=None):
    response = getWebByUrlIp(url).read()
    response = response.decode('UTF-8')
    if regOriginal:
        reg = regOriginal
    else:
        reg = r'src="(http:.+?\.(jpe{0,1}g|gif|png))" '
    imglist = parseRe(response, reg)

    for imgurl in imglist:
        urlData = imgurl[0]
        print("%s : %s" % (x, urlData))
        di = urlData.split('.')

        urllib.request.urlretrieve(urlData, savePath + '%s.%s' % (x, di[len(di) - 1]))
        x += 1
        break
    pass

'''处理数据 '''


def dealData(url, saveFile, regOriginal=None):
    response = getWebByUrlIp(url).read()
    response = response.decode('UTF-8')
    if regOriginal:
        reg = regOriginal
    else:
        reg = r'src="(http:.+?\.(jpe{0,1}g|gif|png))" '
    imglist = parseRe(response, reg)

    for imgurl in imglist:
        urlData = imgurl[0]
        print("%s : %s" % (x, urlData))
        di = urlData.split('.')

        #urllib.request.urlretrieve(urlData, savePath + '%s.%s' % (x, di[len(di) - 1]))
        x += 1
        break
    pass

if __name__ == '__main__':
    savePath = 'D://own//img//'
    #regOriginal = r'src="(http:.+?\.(jpe{0,1}g|gif|png))" '
    regOriginal = r'src="(http:.+?\.(jpe{0,1}g|gif|png))" '
    url = 'https://youke.baidu.com/course/list/8_s0_g0_v87_u0_l0'
    dealFile(url, savePath, 500, regOriginal)
