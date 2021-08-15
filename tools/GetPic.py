# -*- coding: utf-8 -*-

import time
import sys
import urllib
import urllib.request
import re
import os
import traceback
'''
获取网络图片
'''


class GetWebPic(object):
    # 地址
    url = None
    # 请求的数据
    postDict = {}
    requst = None
    cookie = None
    opener = None
    """docstring for GetWebTest"""

    def __init__(self, url, postData=None):
        super(GetWebPic, self).__init__()
        self.url = url
        self.postDict = postData
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))

    def log(self, msg):
        print(msg)
        pass

    # 获取请求

    def getReq(self):
        if self.requst is None:
            self.requst = urllib.request.Request(url=self.url, data=self.postDict)
        return self.requst

    # 获取网页

    def getWebByBuild(self):
        result = self.opener.open(self.getReq())
        return result

    def getWebByUrl(self):
        req = urllib.request.urlopen(self.getReq())
        return req


def getWebByUrlIp(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib.request.urlopen(url)

    #req = urllib2.urlopen(req1)
    return req


def isPathUrl(url):
    if url is not None and url.startswith('http'):
        return False

    return True


def getFullPath(base, path):
    url = path

    if isPathUrl(path):
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

    if resReg:
        reg = resReg
    else:
        reg = r'src="(http:.+?\.(jpe{0,1}g|gif|png))" '
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
        urlData = getFullPath(baseUrl, urlData)
        suffix = urlData.split('.')
        if suffix:
            suffix = suffix[len(suffix) - 1].split("?")[0].replace(" ", "_")
        #print("后缀" + suffix)
        import random
        name = random.randint(0, 9000)
        if resRegRuleFlag == 1 and len(imgurl) > 1:
            name = imgurl[1]
        if realName is not None and realName != '':
            name = realName
        name = name.replace(" ", "_")
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
        break
    if isCirculate and index < 20:
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

    # http://www.320yd.com:66/kan.php?id=72252&typeid=1&from=porn&url=468470
    rsp, urlList = getPageData('http://www.320yd.com:66/kan.php?id=72407&typeid=1&from=porn&url=468531', loadPageRule, True)

    pass


path = 'D://share//img//'
baseUrl = 'http://www.320yd.com:66'
if __name__ == '__main__':
    try:
        print(sys.version)
        baseUrl = 'http://www.320yd.com:66'

        url = 'http://music.163.com/api/playlist/detail?id=3779629'
        url = baseUrl + '/art-type-id-8-pg-34.html'
        url = baseUrl + '/vod-type-id-1-pg-2.html'
        # 0代表直接取，自定义命名
        # 1代表正则里面第一个是url，第二个是路径
        resRegRuleFlag = 1
        resReg = r'"mp3Url":"(http:.+?\.(mp3))",'
        resReg = r'<img .+? src="(.+?\.gif)">[\s\S]+?<div class="citemtxt">[\s\S]+? title="(.+?)">[\s\S]+?</div>'
        resReg = r'<a class="citemtitle".* href="(/.+?\.html)".* title="(.{1,30})">.{1,30}</a>'

        nextPageRule = r'<a .+?href="(/.{1,20}\.html)" .{1,20}>下一页</a>'
        nextPageRule = r'<a target="_self" href="(/.{1,20}\.html)" class="pagelink_a">下一页</a>'

        loadPageRule = r'<source src="(https://.+?)" type="video/.+?" />[\s\S]+?</video>'

        # test()

        dealImg(url, resRegRuleFlag, resReg, True, nextPageRule, 0, 1, loadPageRule, '')
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

