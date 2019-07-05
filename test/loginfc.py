#! D:\Programs\Python\Python35\python.exe
# python3
# -*- coding: utf-8 -*-
import requests
import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 登录时需要POST的数据
data = {'cmd': 'already-registered',
        'tabs1': 'already-registered',
        'login': 'finelycup0012@fc.com',
        'omfjfedpxf_password': '123',
        'verifyCode': 'jqdu'}

# Request URL:http://bojun.fannikabo.com:2831/c/portal/login
#
# 设置请求头
headers = {'Host': 'bojun.fannikabo.com:2831',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate',
           'Connection': 'keep-alive',
           'Cookie': 'JSESSIONID=hn6s8z82e5on; GUEST_LANGUAGE_ID=en_US; COOKIE_SUPPORT=true',
           'Upgrade-Insecure-Requests': '1',
           'Cache-Control': 'max-age=0'}

# 登录时表单提交到的地址（用开发者工具可以看到）

headers2 = {
    'Host': 'bojun.fannikabo.com:2831',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://bojun.fannikabo.com:2831/c/portal/login',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': 116,
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=hn6s8z82e5on; GUEST_LANGUAGE_ID=en_US; COOKIE_SUPPORT=true',
    'Upgrade-Insecure-Requests': 1,
    'Cache-Control': 'max-age=0'
}


# 构造Session
session = requests.Session()

# 在session中发送登录请求，此后这个session里就存储了cookie
# 可以用print(session.cookies.get_dict())查看

login_url = 'http://bojun.fannikabo.com:2831/c/portal/login'
img = 'http://bojun.fannikabo.com:2831/servlets/vms'

resp = session.get(login_url, headers=headers)
#resp = session.post(login_url, data)

resp = session.post(login_url, headers=headers, data=json.dumps(data))

print(resp.content.decode('utf-8'))
# 登录后才能访问的网页
url = 'http://bojun.fannikabo.com:2831/html/nds/portal/portal.jsp'

# 发送访问请求
resp = session.get(url)


# print(resp.text)
