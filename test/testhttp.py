import os
import time
import sys
#import httplib


def get_ci_resp(host, port, url):
    httpClient = None
    httpClient = httplib.HTTPConnection(host, port, timeout=30)
    httpClient.request('GET', url)
    response = httpClient.getresponse()
    return response.read()


def test():
    rslt = get_ci_resp('10.45.4.10', 9089, '/ZCIP/api/zcip/queryTodayFlowState?flowId=1146')
    print(rslt)
    if rslt.find("NOTFOUND") > -1 or rslt.find("FAILED") > -1:
        print('a')
    else:
        print('b')
import os
dirs = os.listdir("C:\\Users\\ZDJ\\Desktop\\runtime")
strs = ""
for dirc in dirs:
    strs = strs + ";" + dirc
    pass
print(strs)
