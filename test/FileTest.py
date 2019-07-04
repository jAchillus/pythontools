# -*- coding: utf-8 -*-
# logfile = open('../tmp/mylog.txt', 'a')
# print >> logfile, "asjd"
# sys.stdout.write("hello"+sys.version)
# user = raw_input("enter:")

print('你')
b = 1
if b == 1:
    a = 2
print(a)
# fd()


def fd():
    pass
import time
ticks = time.time()
print(ticks)
localtime = time.localtime(time.time())
print(localtime)
print(time.asctime())
import time
a = "Sat Mar 28 22:24:24 2016"
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# pattern = re.compile(r'hello')
benefit_value = int(float(-12884901888.00))
print(benefit_value)
benefit_value = '-12884901888'
benefit_value = int(benefit_value)
print(benefit_value)
import math
idx = 0
p = math.pow(3, idx)
depart = math.exp(-3) * p
depart = depart / math.factorial(idx)
# math.exp(2**8635)
a = '12'
b = int(a * 122)
# print(b)
# match = pattern.search('hello world!')
# pattern.match('hello world!')
# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
a = list(range(100))
print(a[7:0:-2])
import threading
threadLock = threading.Lock()
threadLock.acquire()
threadLock.release()
# import MySQLdb
# from distutils.core import setup, Extension

# module1 = Extension('demo',
#                     sources=['demo.c'])

# setup(name='Demo hello',
#       version='1.0',
#       description='This is a demo package by Sink',
#       ext_modules=[module1])

# bo = {"a": 1, "b": 2}
# for x in bo:
#     print(x)
#     pass
# res = 4000
# b = {1: 23}
# a = str(res) + ";"
# if (ticks == '0'):
#     a = str(res) + ";" + str(res)
# import os
# print(os.getcwd())
# os.chdir("C:\\Users\\ZDJ\Desktop\\test")
# print(os.getcwd())
# p = os.popen("svn info")
# # p = os.popen("svn add *")
# # print(os.system("ipconfig"))
# print(p.read())
# print(round(100.0163, 2))
# print(round(float(200/3), 2))

# import re
# file = open("D:\\Users\\ZDJ\\Documents\\Tencent Files\\526908979\\FileRecv\\20170802172916_FlexPMD_10380067_Result.xml", 'rb')
# try:
#     all_the_text = file.read()
#     all_the_text = all_the_text.decode('UTF-8')
#     # print(all_the_text)
#     reg = r'<file name="(.+?)">'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, all_the_text)

#     for im in imglist:
#         print(im)
#         pass
# finally:
#     file.close()

import urllib
import urllib.request
import http.cookiejar

hosturl = 'https://oa.ztesoft.com/Login.jsp?login=0&serviceId=null'

cj = http.cookiejar.CookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
h = urllib.request.urlopen(hosturl)

url = "https://oa.ztesoft.com/queryTransDtl.action?transid=1221738&language=zh%5FCN&orgState=O"
url = "https://oa.ztesoft.com/index.flex"
url = url.encode('utf-8').decode('utf-8')
oridata = {"opr": "pwdLogin",
           "edt_username": "6027020546",
           "edt_pwd1": "jiang123",
           "edt_pwd": "427c0094b8c4e10898b45c60aae502c43409b244f03b43f3f8b003cc5bf248215a6ce19452d6515af3ee9f62f28cf198281f2be6f59c7d8001612851b77057e98f3a62055a2a134042597d227d97a1ca00698dd031046418272e7323fefc01a91cb3df305f10669facf91d49be85cecaa505cfa5cdfa4350ee20a5dc605354f8",
           "ecy_key": 'modify',
           "remember_pwd": "1"
           }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
           'Referer': url}

data = urllib.parse.urlencode(oridata).encode('utf-8')
reqData = urllib.request.Request(url, data=data, headers={})
req = urllib.request.urlopen(reqData)
ss = req.read()
ss = ss.decode('utf-8')
print(ss)
