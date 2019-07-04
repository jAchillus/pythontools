# -*- coding:utf-8 -*-
#!D:/DevelopTools/softs/64/python35
#-*-coding = utf-8-*-
import os
import string
import sys
import time
import re
import math
import fileinput
import glob
import shutil
'''
创建新目录
'''


def mkdir(path):
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False
'''
去文件名，只保留路径
'''


def removeFileName(filePath):
    for x in filePath:
        if (filePath[len(filePath) - 1] != '/'):
            filePath = filePath[:-1]
        else:
            break
    return filePath


def dealFile(dealFileName, targetFileAllPath, splitStr, sourceFilePathFelx, sourceFilePathJava, needIndex=1):
    # 读取文件
    file = open(dealFileName)
    if file is None:
        return
    try:
        lines = file.readlines()
        # 每行
        for line in lines:
            strs = line.split(splitStr)
            # 获取出后面字段的路径
            if strs == '' or strs is None or len(strs) < 2:
                continue
            targetFilePath = strs[needIndex]
            # 去空格
            targetFilePath = targetFilePath.strip()
            # 不能是空
            if targetFilePath is not None and targetFilePath != '' and len(targetFilePath) > 1:
                # 不是路径的行
                if targetFilePath[len(targetFilePath) - 1] == '/':
                    continue
                # 去掉最后的文件名，新增目录
                if (targetFilePath[len(targetFilePath) - 1] != '/'):

                    # 去掉最后的文件名
                    mkdir(targetFileAllPath + removeFileName(targetFilePath))
                # print(targetFilePath)
                targetFileName = targetFileAllPath + targetFilePath
                # print(targetFileName)
                for key in svnPathBo:
                    if targetFilePath.find(key) != -1:
                        sourceFileNameRelative = targetFilePath.replace(key, svnPathBo[key])
                        sourceFileName = sourceFilePathJava + sourceFileNameRelative
                        if targetFilePath.find('flex\\') != -1 or targetFilePath.find('flex/') != -1:
                            sourceFileName = sourceFilePathFelx + sourceFileNameRelative
                        # sourceFileName = sourceFileName.replace('/', '//')
                        shutil.copyfile(sourceFileName, targetFileName)
        pass
    except Exception as e:
        print(e)
    finally:
        if (file):
            file.close()
        pass

svnPathBo = {"branches/main_branch/web/java/code/common": "maroc-common",
             "branches/main_branch/web/java/code/cc": "maroc-cc",
             "branches/main_branch/web/flex/bportal": "maroc-bportal",
             "branches/main_branch/web/flex/bclib": "maroc-bclib",
             "branches/main_branch/pdm": "maroc_pdm",
             "branches/main_branch/web/ZSMART_HOME": "zsmart_home_maroc"}
codePathBo = {"flex": r'D:/Projects/workspace_V8/workspace_Maroc_Flex/',
              "java": r'D:/Projects/workspace_V8/workspace_Maroc/'}

codePathBo_obw = {"flex": r'D:/Projects/workspace_V8/workspace_OBW_Flex/',
                  "java": r'D:\\Projects\\workspace_V8\\workspace_OBW\\'}


def dealConfig(configFile):
    file = open(configFile, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        if line.strip() == '' or line is None:
            continue
        strs = line.split('=')
        print(strs[0])
        if len(strs) == 2:
            svnPathBo[strs[0]] = strs[1]
    pass

# 创建目录，递归创建目录
# mkdir("D://tmp/a/e.test")
# 创建目录，只创建最后一级
dealConfig("D://own//tmp//config.properties")
# print(svnPathBo)
dealFile("D://own//tmp//file.txt", "D://own//tmp//1026420//", '   ', codePathBo['flex'], codePathBo['java'])
