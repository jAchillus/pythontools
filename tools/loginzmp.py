# -*- coding:utf-8 -*-
# -*- coding=utf-8 -*-
# coding=utf-8
# python version 3.5
import urllib
import urllib.request
import json
import logging
import traceback
import time
import os
url = "http://10.45.62.250/ac_portal/login.php"
url = url.encode('utf-8').decode('utf-8')
print(url)
oridata = {"opr": "pwdLogin",
           "userName": "",
           "pwd": "",
           "rememberPwd": "1"
           }
data = urllib.parse.urlencode(oridata).encode('utf-8')
reqData = urllib.request.Request(url, data=data, headers={})


def requestLinknet():
    issuccess = False
    req = urllib.request.urlopen(reqData)
    ss = req.read()
    ss = ss.decode('utf-8')
    ss = ss.replace('false', 'False')
    ss = ss.replace('true', 'True')
    # ss = json.loads(ss)
    ss = eval(ss)
    print('login result:%s' % ss)
    isSus = ss['success']
    print(":%s" % type(isSus))
    # isSus.lower()
    if (isSus is not None and (str(isSus).lower() == 'true')):
        print('success connection!')
        issuccess = True
        pass
    pass
    return issuccess


'''ping'''

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def testPing():
    isconne = True
    try:
        exit_code = os.system('ping www.baidu.com')
        if exit_code:
            raise Exception('connect failed.')

        import urllib.request
        reqData = urllib.request.Request('https://cn.bing.com/')
        req = urllib.request.urlopen(reqData)

        rsp = req.read().decode(encoding="utf-8", errors='ignore')
        # print(rsp)
        if rsp.find('微软') <= -1:
            isconne = False
        print('ping end')
        pass
    except Exception as e:
        # raise e
        isconne = False
        logging.exception(e)
        print(e)
    finally:
        pass
    print(isconne)
    return isconne

"""get hour and minu"""


def getHourAndMinu():
    localtime = time.localtime(time.time())
    print(localtime)
    hour = time.strftime("%H", localtime)
    minu = time.strftime("%M", localtime)
    return hour, minu
    pass

if __name__ == '__main__':
    #localtime = time.localtime(time.time())
    timecount = 3
    issuccess = False
    timeout = 5 * 60
    while True:
        isConne = testPing()
        if isConne:
            print('is connection!')
            time.sleep(timeout)
            timecount = 3
            # timeout = 1 * 60
            continue
        if timecount <= 0:
            # print(timecount)
            # timeout = 1 * 60  # * 60 * 60
            # timecount = 3
            time.sleep(1 * 60 * 60)

            # break
        hour, minu = getHourAndMinu()

        # if int(hour) < 23 and int(hour) > 2:
        #   time.sleep(1 * 60)
        #    continue
        try:
            print(timecount)
            timecount = timecount - 1
            issuccess = requestLinknet()
            if (issuccess):
                time.sleep(1 * 60 * 60)
            pass
        except Exception as e:
            print(e)
            # msg = traceback.format_exc()  # 方式1
            # print(msg)
            print('faild')
            logging.exception(e)
        finally:
            pass
