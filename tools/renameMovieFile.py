# -*- coding: utf-8 -*-
import os
import sys

path='D:\\share\\xx'

repalceNameArr = ('[电影天堂www.dytt89.com]', '阳光电影www.ygdy8.com.')

def replaceName(oriName):
    tmp = oriName
    for name in repalceNameArr:
        if oriName.find(name) != -1:
            oriName = oriName.replace(name, '')
        pass
    flag = False
    if tmp != oriName :
        flag = True
    if oriName == '':
        oriName = tmp
    return flag, oriName


excludeSufArr = ['.py', '.torrent']
def excludeFile(fileName):

    for suff in excludeSufArr :
        if fileName.endswith(suff):
            return True
    return False

for i in os.listdir(path):
    #print("name=%s" % i)
    newName = i
    if not i.endswith('.py'):
        flag, newName=replaceName(i)
        print('---当前处理文件的判断结果: %s,%s' % (flag, newName))
        if flag:
            oldName = os.path.join(path, i)
            newName = os.path.join(path, newName)
            com='mv %s  %s' % (oldName, newName)
            #os.system(com)
            os.rename(oldName, newName)
            print(com)
    sonDir = os.path.join(path, newName)
    if os.path.isdir(sonDir):
        for sonFile in os.listdir(sonDir):
            print("子目录:%s" % sonFile)
            if not excludeFile(sonFile) :
                flag, newName=replaceName(sonFile)
                print('-----当前子目录处理文件的判断结果: %s,%s' % (flag, newName))
                if flag:
                    oldName = os.path.join(sonDir, sonFile)
                    newName = os.path.join(sonDir, newName)

                    com='mv %s  %s' % (sonFile, newName)
                    #os.system(com)
                    os.rename(oldName, newName)
                    print(com)

