# -*- coding: utf-8 -*-
import re

response = 'src="http://img6.bdstatic.com/img/image/smallpic/chongwu112.jpeg" \
 class="img_pic_layer" onload=window.speed.loadmark(); \
 > </div> </a> </div>  <div src="http://img6.bdstatic.com.png" '
reg = r'src="(http:.+?\.(jpe{0,1}g|gif|png))" '
# r':"http://(.+?\.jpg)"'
imgPattern = re.compile(reg)
imglist = re.findall(imgPattern, response)
print("1:", imglist)
imgPattern2 = re.compile(r'\w.+"(.+?\.jpg)"')
match = imgPattern2.match(response)
if match:
    print(match.groups())


# 将正则表达式编译成Pattern对象
pattern = re.compile(r'h\w(.+?)w(.)')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match1 = pattern.match('jhelloworld!hheelhohhellod')

if match1:
    # 使用Match获得分组信息
    print(match1.groups())
import urllib
import urllib.request
x = 490
imgurl = 'http://m2.music.126.net/JbPyLbkMncDEup9MqpBctA==/18762066418099738.mp3'
# urllib.request.urlretrieve(imgurl, 'D://own//img//%s.jpg' % x)


da = '<img src="http://tb.himg.baidu.com/sys/portrait/item/eabee5ad9fe7b4abe6b6b56e696365d067" alt="头像" /></a>                    </li>            \
<li class="visitor_card" ><a href="/home/main?un=some\
times3762&fr=home" target="_blank" class="j_user_card" \
locate="visitor#ihome_v1" data-field="\
locate="visitor#ihome_v1" data-field="{ \
& quot; un & quot; : & quot; wenzheng886 & quot; }">\
<img src="http://tb.himg.baidu.com/sys/portrait/item/0\
e0077656e7a68656e67383836a106" alt="头像" /></a>                    </li>    \
        <li class="visitor_card" ><a href="/home/main?un=二桃U&fr=home" target="_blank" class="j_user_card" locate="visitor#ihome_v1"\
         data-field="{ & quot; un & quot; : & quot; "><img src="http://tb.himg.baidu.com/sys/portrait/item/ba16e4ba8ce6a183556e4b\
         " alt="头像" /></a>  '
da = 'href="/home/main?un=asdsadhfsaj&fr=home" target="_blank"'
# da = 'href="/home/main?un=二桃U&fr=home" target='
reg = r'href=\"(/home/main\?un=.*?&fr=home\")'
# reg = ".+(\d+-\d+-\d+-\d+)"
# da = "hello world!helko"
# reg = r'hel.o'
dataRe = re.compile(reg)
# match = dataRe.match(da)
# print(match.group())
dateList = dataRe.findall(da)
print("new:", dateList)
r = re.match(reg, da)

print(r.group(1))
# m = re.match(r'(hel.o)', 'helao world!helko')
# if m is not None:
#   print(m.group())
s = "This is a number 234-235-22-423"
r = re.match(".+(\d+-\d+-\d+-\d+)", s)

print(r.group(1))
r = re.match(".+?(\d+-\d+-\d+-\d+)", s)
print(r.group(1))
