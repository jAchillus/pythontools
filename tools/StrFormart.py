# -*- coding:utf-8 -*-
#-*-coding = utf-8-*-
#!D:/DevelopTools/softs/64/python35
# python version 3.X
import urllib
import urllib.request
oldStr = '你\n哈'
newStr = oldStr.replace('/', '.')
# 中文转url字符
newStr = urllib.parse.quote(oldStr)
print(newStr)
print(urllib.parse.unquote(newStr))
# str格式byte
#.encode('utf-8')
# byte转str
# .decode('utf-8')
newList = oldStr.splitlines()
print(newList)
