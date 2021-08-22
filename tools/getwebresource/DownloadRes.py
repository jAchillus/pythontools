# -*- coding: utf-8 -*-

import time
import sys
import urllib
import urllib.request
import re
import os
import traceback
import NetworkUtils


def getWebByUrlIp(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
 
        'Host':'',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        #'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=i5a2tp5oji86v417a6t0is4ee2',
        'Upgrade-Insecure-Requests': 1
    }
    page = urllib.request.Request(url, headers=headers,method="GET")
    req = urllib.request.urlopen(page)

    #req = urllib2.urlopen(req1)
    return req


def getFullPath(base, path):
    url = path

    if NetworkUtils.isPathUrl(path):
        url = base + path
    return url


def parseRe(data, reg):
    imgre = re.compile(reg)
    imglist = re.findall(imgre, data)
    return imglist
    pass


def getPageDataByRsp(rsp, reg, isPrint=True):

    dataList = parseRe(rsp, reg)
    if isPrint:
        print("%s" % (dataList))
    return dataList


'''处理图片 '''


def getPageData(url, reg, isPrint=False):
    print("当前处理的 url:%s, 规则： %s" % (url, reg))
    response = getWebByUrlIp(url).read()
    response = response.decode('UTF-8')
    if isPrint:
        print(response)

    imglist = parseRe(response, reg)
    print("parse dataList:%s" % (imglist))
    return (response, imglist)


def dealIframByRsp(rsp, reg):
    urlList = getPageDataByRsp(rsp, reg)
    if urlList is not None and len(urlList) > 0:
        for url in urlList:
            ll = url.split("?")[1].split('&')
            for var in ll:
                keyValue = var.split('=')
                tet = 'var %s ="(.+?)";' % keyValue[1].replace('"', '').replace('+', "").strip()
                data = getPageDataByRsp(rsp, tet, False)
                url = url.replace(keyValue[1], data[0])
                pass
            pass
            print("ifram URL: %s" % url)
            return url
    pass


def dealIfram(url, reg):
    rsp, dataList = getPageData(url, reg)
    return dealIframByRsp(rsp, reg)


def loadIframeRes():
    pass


'''
url是当前页面
resRegruleFlag规则，命名规则，暂时只有0
resReg  匹配出的下载资源url规则
isCirculate:是否需要翻页下载
nextPageRule:翻页时候的下一页规则
index：当前页面深度
downloadFlag: 0代表直接匹配出来的下载，1是需要进行进入下载页面再下载
downloadReg：下载页面的资源url匹配规则
'''


def dealImg(url, resRegRuleFlag=0, resReg=None, isCirculate=False, nextPageRule='', index=0, downloadFlag=0, downloadReg='', realName=''):

    reg = resReg

    # t = GetWebPic(url)
    response, imglist = getPageData(url, reg)
    if imglist is None or len(imglist) == 0:
        if (response.find('<iframe') > -1):
            regIfram = r"<iframe height='480' width='100%' src='(.+?)'frameborder"

            iframUrl = dealIframByRsp(response, regIfram)

            dealImg(getFullPath(baseUrl, iframUrl), resRegRuleFlag=0, resReg=resReg, realName=realName, index=index)
            return
    for imgurl in imglist:
        urlData = str(imgurl)
        if resRegRuleFlag == 1:
            urlData = imgurl[0]
        import random
        name = random.randint(0, 9000)
        if resRegRuleFlag == 1 and len(imgurl) > 1:
            name = imgurl[1]
        if realName is not None and realName != '':
            name = realName
        name = name.replace(" ", "_")

        urlData = getFullPath(baseUrl, urlData)
        suffix = urlData.split('.')
        if suffix:
            suffix = suffix[len(suffix) - 1].split("?")[0].replace(" ", "_")
        #print("后缀" + suffix)

        try:
            # 直接处理
            if downloadFlag == 0:
                print("下载资源url:%s, name:%s" % (urlData, name + suffix))
                newPath = path + str(index) + "//"
                import os
                if not os.path.exists(newPath):
                    os.makedirs(newPath)

                urllib.request.urlretrieve(urlData, newPath + '%s.%s' % (name, suffix))
                # 下个页面下载
            elif downloadFlag == 1:
                print("进入下载页")
                newUrl = getFullPath(baseUrl, urlData)

                dealImg(newUrl, resRegRuleFlag=0, resReg=downloadReg, index=index, realName=name)
            print('')
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            time.sleep(1)
            pass
        print("%s : %s" % (name, urlData))
    if isCirculate and index < 10:
        dealNextPage(response, nextPageRule, index, resRegRuleFlag, reg, isCirculate, downloadFlag, loadPageRule)
    pass


def dealNextPage(response, nextPageRule, index, resRegRuleFlag, reg, isCirculate, downloadFlag, loadPageRule):
    print("deal next page data")
    nextPage = parseRe(response, nextPageRule)
    if nextPage is not None and len(nextPage) > 0:
        newUrl = ''

        newUrl = getFullPath(baseUrl, nextPage[0])

        try:
            dealImg(newUrl, resRegRuleFlag, reg, isCirculate, nextPageRule, index + 1, downloadFlag, loadPageRule, '')
        except Exception as e:
            print(e)
            print(traceback.format_exc())

            time.sleep(3)
            try:
                dealImg(newUrl, resRegRuleFlag, reg, isCirculate, nextPageRule, index + 1, downloadFlag, loadPageRule, '')
            except Exception as e:
                print(e)
                print(traceback.format_exc())
        finally:
            pass


def test():
    loadPageRule = r'<source src="(https://.+?)" type="video/.+?" />[\s\S]+?</video>'

    rsp, urlList = getPageData('', loadPageRule, True)

    pass


path = 'D://share//img//'
baseUrl = ''
if __name__ == '__main__':
    try:
        print(sys.version)

        url = 'http://music.163.com/api/playlist/detail?id=3779629'
        url = baseUrl + '/art-type-id-8-pg-34.html'
        url = baseUrl + '/vod-type-id-1-pg-6.html'
        # 0代表直接取，自定义命名
        # 1代表正则里面第一个是url，第二个是路径
        resRegRuleFlag = 1
        resReg = r'"mp3Url":"(http:.+?\.(mp3))",'
        #resReg = r'<img .+? src="(.+?\.gif)">[\s\S]+?<div class="citemtxt">[\s\S]+? title="(.+?)">[\s\S]+?</div>'
        resReg = r'<a class="citemtitle".* href="(/.+?\.html)".* title="(.{1,30})">.{1,30}</a>'

        nextPageRule = r'<a .+?href="(/.{1,20}\.html)" .{1,20}>下一页</a>'
        nextPageRule = r'<a target="_self" href="(/.{1,20}\.html)" class="pagelink_a">下一页</a>'

        loadPageRule = r'<source src="(https://.+?)" type="video/.+?" />[\s\S]+?</video>'

        # test()

        dealImg(url, resRegRuleFlag, resReg, True, nextPageRule, 6, 1, loadPageRule)
        pass
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise
    else:
        pass
    finally:
        os._exit(0)
        pass
