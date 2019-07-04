# -*- coding:utf-8 -*-
# coding=utf-8
import urllib
import urllib.request
import re

reqData = urllib.request.Request('https://www.zhihu.com/people/gaoming623')
req = urllib.request.urlopen(reqData)
response = req.read()
response = response.decode('utf-8')
dataRe = re.compile(r'<span class=".*?-.*?>(.*?)</span>')
datePresonList = dataRe.findall(response, re.S)
dataRe = re.compile(r'<div class="Profile-sideColumn".*?知乎收录(.*?)个回答.*?获得(.*?)次赞同.*?获得(.*?)次收藏.*?关注了</div><div class="NumberBoard-value">(.*?)</div>.*?关注者</div><div class="NumberBoard-value">(.*?)</div>.*?关注的收藏夹</span><span')
dateSideList = dataRe.findall(response)

print(dateSideList)
