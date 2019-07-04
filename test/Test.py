# -*- coding: utf-8 -*-
# import sys
# print sys.version
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.baidu.com', 80))
# print'done.'
import re
charge = '10'
comDate = 'nihao'
offerName = 'haha'
if charge is None:
    charge = '0'
if comDate is None:
    comDate = ''
if offerName is None:
    offerName = ''
strMsg = ''
strMsg += 'Dear customer, you have successfully subscribed to ' + offerName + ' on ' + comDate + '. ' + charge + ' Ks will be deducted from your main account. Enjoy MPT services with preferential price.'
print(strMsg)

str1 = 'flowpage/bundle/BundleReactivationUnderRequestPage.swf'
str1 = str1.replace('/', '.')
print(str1)

a = ''
if a == '':
    print('asdsa')
    pass
sd = 'url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_0e814c16. \
png);background-repeat:no-repeat;_background-image:url(http://s1.bdstatic.com/r/ \
w/cache/static/global/img/icons_5c448026.gif)'
#p = re.compile(r'sd')
#match = p.match('sd')
#match = re.search('sd', sd)
# if (match is not None):
# print 'test'
# print match.group()
# pass
# 找第一个字母开始，不满就结束
p = re.match('url(.)http(.)?://(.*)[")",";"]', sd)
if p is not None:
    print(p.group())
    pass
# 一直找
p = re.search('s', sd, 1)
if p is not None:
    print(p.group())
    pass
    # 查询所有
    # url(.)http(.)?://(.*);
#p = re.findall('url((http://)([A-z0-9./]+[_-]?[A-z0-9./]+)*\);', sd)
if p is not None:
    print('test:')
    print(p)
    pass

# print p.group(1)
#
#
# http://10.45.62.250/ac_portal/default/pc.html?template=default&tabs=pwd&vlanid=0&url=http://www.baidu.com%2f
#
#
import re
import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    # print(html)
    html = html.decode('UTF-8')
    return html


def getImg(html):

    reg = r'src="(.+?\.jpg)" pic_ext'

    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 100
    for imgurl in imglist:
        print("%s" % (x))
        urllib.request.urlretrieve(imgurl, 'D://own//img//%s.jpg' % x)
        x += 1
    return imglist

#html = getHtml("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0")

# getImg(html)
#print('\n'.join([''.join([('PYTHON!'[(x-y)%7]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

#_=[__import__('sys').stdout.write("\n".join('.' * i + 'Q' + '.' * (8-i-1) for i in vec) + "\n===\n") for vec in __import__('itertools').permutations(range(8)) if 8 == len(set(vec[i]+i for i in range(8))) == len(set(vec[i]-i for i in range(8)))]

#_='_=%r;print( _%%_)';print( _%_)

x = 1
ut = 'ftp://ygdy8:ygdy8@y153.dydytt.net:9204/[阳光电影www.ygdy8.com].海边的曼彻斯特.BD.720p.中英双字幕.mkv'
# urllib.request.urlretrieve(ut, 'D://own//img//%s.mkv' % x)
import ctypes
dll = ctypes.windll.LoadLibrary('TestDLL.dll')
dll.foo(4, 3)
test = ctypes.windll.LoadLibrary("./TestCython.so")
test.foo(1, 2)
#import TestCython

#TestCython.foo(1, 2)
# import jpype
# startJVM(getDefaultJVMPath(), "-ea")
# java.lang.System.out.println("Hello World")
# shutdownJVM()
