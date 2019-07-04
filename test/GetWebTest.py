# -*- coding: utf-8 -*-
import sys
import urllib
import urllib.request
import re
import os


class GetWebTest(object):
    pass


f = urllib.request.urlopen('http://10.45.4.10:9089/ZCIP/filetemp/SimianCheck/20170614/9639240/20170614090243/9639240/Simian_9639240_Result.html')
# print(f.read())

response = f.read().decode('utf-8')
# print(response)
# reg = r'<td>(com\.ztesoft\.zsmart\.bss\..*?)</td>'
reg = '<a href="#set-.*?">\/home\/dailyci\/ZCIPClient\/workpath\/1146\/code\/web\/web\/java\/.*?(com/ztesoft.*\.java)</a>'
dataRe = re.compile(reg)
dateList = dataRe.findall(response)
# print(dateList)
for x in range(len(dateList)):

    da = dateList[x]
    das = da.split('.')
    str = "**"
    for x1 in range(len(das)):
        if (x1 < len(das) - 1):
            str += '/' + das[x1]
            if (x1 == len(das) - 2):
                str += '.java'
    print(str)
    pass
