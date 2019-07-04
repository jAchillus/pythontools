# -*- coding:utf-8 -*-
#!D:/DevelopTools/softs/64/python35
import itertools
# te = itertools.count(1)
# te = itertools.takewhile(lambda x: x <= 10, te)
te = itertools.repeat('1', 20)
for i in te:
    print(i)
# 迭代器,重复
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
# 分组迭代重复
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key)
    print(list(group))
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
#import paramiko

file = open('D:\\J\\Downloads\\新建文本文档.txt', 'w')
i = 0
while i < 1000:
    i = i + 1
    iccid = 629012019011000 + i
    file.write(str(iccid) + "," + str(iccid) + '\n')
    pass
file.flush()
file.close()
import re
fellowNbr = '659192000'
res = False
if(re.match(r'^\d{8,9}$', fellowNbr)):
    res = True


import re
def main(r):
    fellowNbr = r.getFellowNbr()
    res = False
    if(re.match(r'^\d{8,9}$',fellowNbr)):
        res = r.isFellowNbrOnNet()
    r.setResult(res)
# 】.
