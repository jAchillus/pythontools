# -*- coding:utf-8 -*-
# -*- coding=utf-8 -*-
# coding=utf-8
import urllib
import urllib.request
import json
import logging
import traceback
import time
url = "http://10.45.62.250/ac_portal/login.php"
url = url.encode('utf-8').decode('utf-8')
print(url)
oridata = {"opr": "pwdLogin",
           "userName": "0027010408",
           "pwd": "jiang123",
           "rememberPwd": "1"
           }
data = urllib.parse.urlencode(oridata).encode('utf-8')
reqData = urllib.request.Request(url, data=data, headers={})


def requestLinknet():
    issuccess = False
    req = urllib.request.urlopen(reqData)
    ss = req.read()
    # ss = b"{'success':'false', 'msg':'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe6\x88\x96\xe5\xaf\x86\xe7\xa0\x81\xe9\x94\x99\xe8\xaf\xaf','action':'location','pop':0,'userName':'656','location':''}"
    ss = ss.decode('utf-8')
    ss = ss.replace('false', 'False')
    ss = ss.replace('true', 'True')
    # ss = json.loads(ss)
    ss = eval(ss)
    print('result:%s' % ss)
    isSus = ss['success']
    print(":%s" % type(isSus))
    # isSus.lower()
    if (isSus is not None and (str(isSus).lower() == 'true')):
        print('success connection!')
        issuccess = True
        pass
    pass
    return issuccess
import os

'''ping'''


def testPing():
    isconne = True
    try:
        exit_code = os.system('ping www.baidu.com')
        if exit_code:
            raise Exception('connect failed.')
        pass
    except Exception as e:
        # raise e
        isconne = False
        logging.exception(e)
    finally:
        pass
    print(isconne)
    return isconne


def getHourAndMinu():
    localtime = time.localtime(time.time())
    print(localtime)
    hour = time.strftime("%H", localtime)
    minu = time.strftime("%M", localtime)
    return hour, minu
    pass

if __name__ == '__main__':
    localtime = time.localtime(time.time())
    timecount = 3
    issuccess = False
    while True:
        isconne = testPing()

        if isconne:
            time.sleep(1*60*60)
            print('is connection!')
            continue
        if timecount <= 0 or issuccess:
            print(timecount)
            break
        hour, minu = getHourAndMinu()

        if int(hour) < 23 and int(hour) > 2:
            time.sleep(1 * 60)
            continue
        try:
            timecount = timecount - 1
            issuccess = requestLinknet()
            pass
        except Exception as e:
            print(e)
            # msg = traceback.format_exc()  # 方式1
            # print(msg)
            print('faild')
            logging.exception(e)
        finally:
            pass
