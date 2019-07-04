# -*- coding:utf-8 -*-
# -*- coding=utf-8 -*-
import urllib
import urllib.request
import re
import GetWebUsers
user_agent = GetWebUsers.user_agent_list[1]
headers = {'User-Agent': user_agent}
curDate = urllib.parse.quote('野性的呼唤')
url = 'http://222.27.200.21/NTRdrBookRetr.aspx?strType=text&strKeyValue='+curDate+'&strSortType=&strpageNum=10&strSort=asc'
print(url)
reqData = urllib.request.Request(url, data=b'', headers=headers)
req = urllib.request.urlopen(reqData)
response = req.read().decode('utf-8')

reg = r'<a href=\"(NTRdrBookRetrInfo.aspx\?.*?)<a class=link2 name=detail'
dataRe = re.compile(reg, re.S)
dateList = dataRe.findall(response)
if len(dateList):
    dateList[0] = dateList[0].replace('\n', '')
    dateList[0] = dateList[0].replace('\r', '')
    dateList[0] = dateList[0].replace('\t', '')
    # print(dateList[0])
    dataRe1 = re.compile(r'<span class=\"(.*?)\">(.*?)<strong.*?>(.*?)</strong></span>', re.S)
    dateList1 = dataRe1.findall(dateList[0])
    print(dateList1)
# 任意，书名，作者，分类，isbn,索书号，主题，出版社
# text,name,author,classno,isbn,callno,subject,publish
# http:
#     //222.27.200.21/NTRdrBookRetr.aspx?strType = text & strKeyValue = %E7 % 8E % B0 % E4 % BB % A3 & strSortType = &strpageNum = 10 & strSort = asc
# http:
#     //222.27.200.21/NTRdrBookRetr.aspx?strType = name & strKeyValue = %E7 % 8E % B0 % E4 % BB % A3 & strSortType = &strpageNum = 10 & strSort = asc
# http:
#     //222.27.200.21/NTRdrBookRetr.aspx?strType = author & strKeyValue = 12321 & strSortType = &strpageNum = 10 & strSort = asc
# http:
#     //222.27.200.21/NTRdrBookRetr.aspx?strType = classno & strKeyValue = 12321 & strSortType = &strpageNum = 10 & strSort = asc
# http:
#     //222.27.200.21/NTRdrBookRetr.aspx?strType = isbn & strKeyValue = 12321 & strSortType = &strpageNum = 10 & strSort = asc
# http:
#     //222.27.200.21/NTRdrBookRetr.aspx?strType = callno & strKeyValue = 12321 & strSortType = callno & strpageNum = 10 & strSort = asc
# http:
#     //222.27.200.21/NTRdrBookRetr.aspx?strType = subject & strKeyValue = 12321 & strSortType = callno & strpageNum = 10 & strSort = asc
# http:
#     //222.27.200.21/NTRdrBookRetr.aspx?strType = publish & strKeyValue = 12321 & strSortType = callno & strpageNum = 10 & strSort = asc
