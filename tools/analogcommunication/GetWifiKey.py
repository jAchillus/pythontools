# coding=UTF-8
# python version 3.5
# os version  win10
import os
import sys


def getAllWifi():
    wifiAll = os.popen('netsh wlan show profiles').read()

    wifiResultArr = []
    infoArr = wifiAll.split('\n')
    for info in infoArr:
        if info.find('所有用户配置文件') > -1:
            wifiArr = info.split(':')
            if len(wifiArr) > 1:
                name = wifiArr[1].rstrip().lstrip()
                if name != '':
                    wifiResultArr.append(name)
    return wifiResultArr


def getKey(wifi=''):
    if wifi != '' and wifi is not None:
        wifiNameArr = [wifi]
    else:
        wifiNameArr = getAllWifi()
    if wifiNameArr is None:
        return
    for wifiName in wifiNameArr:
        if wifiName != '':
            cm = 'netsh wlan show profiles  name="%s"  key="clear"' % (wifiName)
            wifiInfo = os.popen(cm).read()
            wifiKeyArr = wifiInfo.split('关键内容')
            if len(wifiKeyArr) > 1:
                lineArr = wifiKeyArr[1].split('\n')
                if len(lineArr) > 0:
                    key = lineArr[0].lstrip()[1:]
                    print("%s 密码：%s" % (wifiName, key))
            else:
                print('no the wifi password,%s' % wifiName)


wifi = None
if len(sys.argv) > 1:
    wifi = sys.argv[1]
if __name__ == '__main__':
    getKey(wifi)
