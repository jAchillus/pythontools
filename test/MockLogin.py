# -*- coding:utf-8 -*-
#!D:/DevelopTools/softs/64/python35

import os
# os.chdir("C:\\Users\\J\\Desktop\\test")
# print(os.getcwd())
#p = os.popen("ipconfig")
#p = os.popen("svn info")
# f = open("test.java", 'w')
# os.popen("svn add testproject")
# p = os.popen("svn commit -m 'first' --username j --password 123wss456")
# print(p.read())
#data = input()
#print(data + ' 你好')


a = -12321321

b = 'a' + str(abs(float(a)) / 1000)
# print(b)
# print(float(10/3))
# p = open('Test3.py', 'r')
# print(p.read())
# p.close()

import requests
userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "95",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "aliyungf_tc=AQAAAMNkSiWlmQwAYI7fKZwsIU9cEOYj; _user_behavior_=1a171db8-e39c-481d-833b-e4c043c5b9f8; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1540998805; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1541168962; _reg_key_=2sTAhd2EZLuL5clCnGhJ",
    "Host": "www.oschina.net",
    "Origin": "https://www.oschina.net",
    "Referer": "https://www.oschina.net/home/login?goto_page=https%3A%2F%2Fwww.oschina.net%2F",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

import urllib
import urllib.request


def Login(account, password):
    # 马蜂窝模仿 登录
    print("开始模拟登录")
    sess = requests.session()
    sess.auth = ('auth', 'passwd')
    getUrl = "https://www.oschina.net/action/user/before_login?email=tsrjwwdz@outlook.com"
    responseRes = sess.get(getUrl)
    print("statusCode =" + str(responseRes.status_code))
    print("text = " + responseRes.text)
    print("end 1")
    postUrl = "https://www.oschina.net/action/user/hash_login?from="
    postData = {
        "email": account,
        "pwd": password,
        "verifyCode": "",
        "save_login": '1'
    }

    responseRes = sess.post(postUrl, data=postData, headers=header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print("statusCode =" + str(responseRes.status_code))
    print("text = " + responseRes.text)
    print(responseRes.cookies)
    print(sess.cookies)
    # responseRes = sess.get("https://gitee.com/ldcsaa/HP-Socket/repository/archive/master.zip", cookies=responseRes.cookies)
    # print(responseRes)
    # print("statusCode =" + str(responseRes.status_code))
    # print("text = " + responseRes.text)
    # # print("text = " + responseRes.content.decode('UTF-8'))
    # # ff = open("D://demo2.zip", "wb")
    # # ff.write(responseRes.content)
    # with open("D://demo2.zip", 'wb') as f:
    #     f.write(responseRes.content)
    #     f.close()
    #     print("D://demo2.zip" + ' 文件保存成功')
    # urllib.request.urlretrieve("https://gitee.com/ldcsaa/HP-Socket/repository/archive/master.zip", 'D://xxx')

    # print("content = " + responseRes.content)
    print()
if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    #Login("tsrjwwdz@outlook.com", "efa44b422e2e50b42b199b7b5cd76f9517f83e30")
    a = '2'
    b = '2'
    c = '3'
    if a == '2' or a == '1' and b == '1' or c == '4':
        print(a)
