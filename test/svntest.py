# -*- coding:utf-8 -*-
# -*- coding=utf-8 -*-
# coding=utf-8
# python version 3.5
import os
import re
import time
import datetime
import copyFileToSvnPath
os.getcwd()
os.chdir('D:\\tmp\\svn')
# exit_code = os.system('svn co http://10.45.5.222:9050/svn/ZSmart8_Proc/trunk/ZSmart_CRM_V8.1C_主分支/ \
# --username zhang.dongjiang2 --password jiang123')

# logList = os.system('svn log http://10.45.5.222:9050/svn/ZSmart8_Proc/trunk/ZSmart_CRM_V8.1C_主分支/ \
# --username zhang.dongjiang2 --password jiang123')
# print('---------------')
# print(logList)
reg = r'1251004.{0,500}'
dataRe = re.compile(reg)

'''获取当前的任务列表'''


def getCurTaskFileList(url, username, password, beginData=None, endDate=None):
    if endDate is None:
        endDate = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    if beginData is None:
        beginData = (datetime.datetime.now() + datetime.timedelta(days=-30)).strftime("%Y-%m-%dT%H:%M:%S")
    svncons = 'svn log -r{' + beginData + '}:{' + endDate + '} -v ' + url + ' \
 --username ' + username + ' --password ' + password
    logInfo = os.popen(svncons)
    logInfo = logInfo.read()
    logList = logInfo.split('-----------------------------------------------------------------\n')
    fileList = []

    # 所以提交的记录循环
    for log in logList:
        log = log.split('\n')
        # print(x)
        if len(log) < 2:
            continue
        isCurTask = False
        # 本次提交的内容提取出文件
        tmpFileList = []
        for i in range(0, len(log)):
            if i < 2:
                continue
            tmp = log[i].strip()
            # 存储文件
            if tmp.split(' ')[0].strip() == 'M' or tmp.split(' ')[0].strip() == 'A' or tmp.split(' ')[0].strip() == 'D':
                tmpFileList.append(tmp.split(' ', 1)[1].strip())
                # print(tmpFileList)
            match = dataRe.match(tmp)
            if match:
                # print(x)
                isCurTask = True
                break

        if isCurTask:
            for i in tmpFileList:
                fileList.append(i)
    # print(fileList)
    new_list = list(set(fileList))
    print(new_list)
    return new_list
    pass


def dealTaskFileList(fileList, url, username, password):
    for x in fileList:
        st = 'svn export ' + url + x + ' --username ' + username + ' --password ' + password
        svnInfo = os.popen(st)
        fileList = svnInfo.read()
        fileList = fileList.split('-----------------------------------------------------------------\n')
        print(fileList)
    pass

dealTaskFileList(
    getCurTaskFileList('http://10.45.7.140:9050/svn/ZSmart_CRM_V8.1C/branches/main_branch', 'zhang.dongjiang2', 'jiang123'),
    'http://10.45.7.140:9050/svn/ZSmart_CRM_V8.1C/', 'zhang.dongjiang2', 'jiang123')
