# -*- coding:utf-8 -*-
# -*- coding=utf-8 -*-
# coding=utf-8
import urllib
import urllib.request
import re
import sys
import logging
import traceback
import json
import zlib
import sqlite3
import time
import threading

'''一些伪装浏览器访问的head'''
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",

    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",

    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0 Zune 3.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 4.0.20402; MS-RTC LM 8)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 1.1.4322; InfoPath.2)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 3.0.04506; Media Center PC 5.0; SLCC1)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0; .NET CLR 3.0.04506; Media Center PC 5.0; SLCC1)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; FDM; Tablet PC 2.0; .NET CLR 4.0.20506; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 3.0.04506; Media Center PC 5.0; SLCC1; Tablet PC 2.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 1.1.4322; InfoPath.2)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.3029; Media Center PC 6.0; Tablet PC 2.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; FDM; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.40607)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.0.3705; Media Center PC 3.1; Alexa Toolbar; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
    'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; el-GR)',
    'Mozilla/5.0 (MSIE 7.0; Macintosh; U; SunOS; X11; gu; SV1; InfoPath.2; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)',
    'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)',
    'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)',
    'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; fr-FR)',
    'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; en-US)',
    'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; WOW64; .NET CLR 2.0.50727)',
    'Mozilla/4.79 [en] (compatible; MSIE 7.0; Windows NT 5.0; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)',
    'Mozilla/4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)',
    'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)',
    'Mozilla/4.0 (compatible;MSIE 7.0;Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0;)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; YPC 3.2.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; YPC 3.2.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; Media Center PC 5.0; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30618; .NET CLR 1.1.4322)',
]

'''深度'''
global pageNumber
'''用户数量，可以列表 多线程 互不干扰'''
global userNumber
'''每个线程使用页数'''
global numberPer
'''每页的数量，也可以不要，直接id使用序列'''
global numberPerPage

'''中文判断'''
zhPattern = re.compile(u'([\u4e00-\u9fa5]+)')

cx = sqlite3.connect("D:/own/tmp/test.db", check_same_thread=False)

pageNumber = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
userNumber = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numberPerPage = 24

global levelBo
levelBo = {}

'''解析所有满足的字段'''


def parseRe(data, reg):
    dataRe = re.compile(reg)
    dateList = dataRe.findall(data)
    return dateList
    pass

'''是否包含中文'''


def isContainZh(data):
    match = zhPattern.search(data)
    if match:
        return True
    return False
    pass

'''解析中文返回url编码'''


def parseZh(data):
    dateList = zhPattern.findall(data)
    curDate = ""
    #     urllib.parse.urlencode(params)
    if dateList is not None:
        curDate = urllib.parse.quote(dateList[0])
    return curDate
    pass

'''将地址中的中文转码'''


def getCurUrl(ip, url, page):
    # ip地址
    newIp = (ip + url + "&pn=" + str(page)).encode('utf-8').decode('utf-8')
    # 如果是含有中文，需要转为url码
    if isContainZh(newIp):
        zhEn = parseZh(newIp)
        newIp = zhPattern.sub(zhEn, newIp)
    return newIp

'''处理每个满足条件的数据的结果'''


def dealDataPer(dataurl, url, startIndex, cur):
     # global userNumber

    userUrl = dataurl[0]
    userName = dataurl[1]
    # print(dataurl)
    if (userUrl.encode('utf-8') == url.encode('utf-8')):
        return
    nameList = parseRe(userUrl, r'/home/main\?un=(.{1,50})\"')

    # print(nameList)
    if nameList and len(nameList) > 0:
        name = nameList[0].encode('utf-8').decode('utf-8')
        if not isContainZh(nameList[0]):
            name = urllib.parse.unquote(nameList[0])
            # print("name1:%s" % (name))
    # 当前用户排列
    if userNumber[startIndex] == 0:
        userNumber[startIndex] = numberPerPage * numberPer * startIndex
    userNumber[startIndex] += 1
    # print("name:%d,%d,%s,%d" % (startIndex, userNumber[startIndex], userName, int(dataurl[2])))
    da = (userNumber[startIndex], userName, userName, dataurl[2])
    print("data:%s,page:%s" % (da, pageNumber[startIndex]))
    if dataurl[2] in levelBo.keys():
        levelBo[dataurl[2]] += 1
    else:
        levelBo[dataurl[2]] = 1
    try:
        cur.execute("insert into baidu_tieba_users(user_id,user_name,user_code,level) values (?,?,?,?)", da)
        pass
    except Exception as e:
        # raise e
        print("insert data error:", e)
    finally:
        pass

'''获取用户'''


def GetUser(ip, url, reg, startIndex=0, oriIndex=0):
    try:
        # 游标
        cur = cx.cursor()
        user_agent_index = 0
        match = zhPattern.search(ip + url)
        # 页数
        if pageNumber[startIndex] == 0:
            pageNumber[startIndex] = (startIndex * numberPer + oriIndex)
        pageNumber[startIndex] += 1

        print("page:%d" % pageNumber[startIndex])
        newIp = getCurUrl(ip, url, pageNumber[startIndex])
        user_agent_index += 1
        user_agent_index %= len(user_agent_list)
        user_agent = user_agent_list[user_agent_index]
        headers = {'User-Agent': user_agent}
        reqData = urllib.request.Request(newIp, data=b'', headers=headers)
        req = urllib.request.urlopen(reqData)
        response = req.read()
        # response = zlib.decompress(response, 16+zlib.MAX_WBITS)
        try:
            response = response.decode('utf-8')
        except Exception as e:
            # print(response.decode('gbk', 'ignore'))
            response = response.decode('gbk')

        # print(response)
        dateList = parseRe(response, reg)
        for dataurl in dateList:
            dealDataPer(dataurl, url, startIndex, cur)
        cur.close()

        if pageNumber[startIndex] < (startIndex + 1) * numberPer:
            GetUser(ip, url, reg, startIndex, oriIndex)
            pass
        pass
    except Exception as e:
        # print("error:", e)
        # msg = traceback.format_exc()  # 方式1
        # print(msg)
        logging.exception(e)    # 方式2
        raise e
    finally:
        cur.close()
        pass

        '''结果处理'''


def dealResult(threads):
    while True:
        endNum = 0
        for i in range(threadNum):
            if threads[i].isAlive():
                break
            print("Thread %d is end." % i)
            endNum += 1
        if (endNum == threadNum):
            break
        time.sleep(3)
    print('result%s:' % userNumber)
    # cx.commit()
    print(levelBo)
    cx.close()

reg = r' href=\"(/home/main\?un=.{1,50}?=home)\" '
reg = r'<div class="name_wrap"><a href=\"(/home/main\?un=.{1,50}\") class=\"user_name\" title=\"(.{1,50})\">.{1,50}</a><span class="forum-level-bawu bawu-info-lv(\d*)"></span></div>'

numberPer = 11
threadNum = 1
if __name__ == '__main__':
    try:
        threads = [None, None, None, None, None, None, None, None, None, None]
        ip = "http://tieba.baidu.com"
        firstUrl = "/bawu2/platform/listMemberInfo?word=%B8%DF%BF%BC"

        # firstUrl = '/bawu2/platform/listMemberInfo?word=%BD%AD%CB%D5%B4%F3%D1%A7'
        for i in range(threadNum):
            threads[i] = threading.Thread(target=GetUser, args=(ip, firstUrl, reg, i))
            threads[i].start()
        # GetUser("http://tieba.baidu.com", "/bawu2/platform/listMemberInfo?word=%B8%DF%BF%BC", reg, startIndex=0)
        pass
    except Exception as e:
        raise e
    finally:
        dealResult(threads)
        sys.exit(0)
        pass
