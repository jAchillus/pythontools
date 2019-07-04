# -*- coding:utf-8 -*-
#!D:/DevelopTools/softs/64/python35
#-*-coding = utf-8-*-
import string

"测试序列"


class SequenceTest:

    def __init__(self):
        pass

    def test1(self):
        # 元组
        y = ('a', 2)
        #y[1] = 2
        # 列表
        l = [1, 2]
        l *= 2
        print(l)
        l[1] = 3
        print(y[-2:30])
        print(range(0, len(y) + 1, 1))
        for s in range(0, len(y) + 1, 1):
            print('s:', s)
            print('end:', y[:s])
            print('start:', y[s:])
        print(y[0:])
        print(y[:None])

    def testFor(self):
        for s in range(5):
            print(s)
        else:
            print('else')
        print('\n', r'\n')
        co = compile('for i in range(0, 10): print(i)', '', 'exec')
        exec(co)
        # print(u'a\u1234')

        pass
    "字符串"

    def testString(self):
        str1 = 'a'
        print(id(str1))
        str1 = 'a' + 'b'
        print('strID:', id(str1))
        print('strID:', id('a'))
        return
        i1 = 1
        print(id(i1))
        print(id(1))
        i2 = 1
        print(id(i2))
        list1 = [1, 2]
        list2 = [1, 2]
        print(id(list1))
        print(id(list2))
        pass
    "Unicode Test"

    def testUnicode(self):
        str1 = 'Hell'
        str2 = u'H-_`@ell'
        print(id(str1))
        print(id(str2))
        # Unicode.unicode(str1)
        pass
    "Test list"

    def testList(self):
        li = list('foo')
        li.remove('o')
        li.append('E')
        li[0]
        print(li[1])
        pass
import sys
if __name__ == '__main__':
    se = SequenceTest()
    se.testList()
    #v = sys.version_info.serial
    # print(v)
f = None
try:
    f = open("D:\\J\\Desktop\\error.txt")
    lines = f.readlines()
    for line in lines:
        print(line.replace(' ', ''))
    pass
except Exception as e:
    print(e)
    # raise
# else:
    # pass
finally:
    if (f):
        print(id(f))
        # f.close()
        print(id(f))

    pass

try:
    pass
except Exception as e:
    raise e
finally:
    pass

j = 0
for x in range(1, 10):
    # j = j ++
    pass
print(j)
lis = [1, 2, 4, 5]
for x in lis:
    print(x)
    pass
del lis

# print(lis)


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
sd = 'url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_0e814c16.png);background-repeat:no-repeat;_background-image:url(http://s1.bdstatic.com/r/w/cache/static/global/img/icons_5c448026.gif)'
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
p = re.findall('url((http://)([A-z0-9./]+[_-]?[A-z0-9./]+)*\);', sd)
if p is not None:
    print('test:')
    print(p)
    pass

# print p.group(1)
#
#
# http://10.45.62.250/ac_portal/default/pc.html?template=default&tabs=pwd&vlanid=0&url=http://www.baidu.com%2f
#
