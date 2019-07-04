import urllib.request
req = urllib.request.Request(url='http://www.cnblogs.com/cocoajin/p/3679821.html',
                             data=b'This data is passed to stdin of the CGI')

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
# Got Data: "This data is passed to stdin of the CGI"

# 基本的HTTP验证，登录请求
# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='http://www.cnblogs.com/cocoajin/p/3679821.html',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib.request.build_opener(auth_handler)
# # ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)
f = urllib.request.urlopen('http://www.cnblogs.com/cocoajin/p/3679821.html')
# print(f.read())
# 添加 http headers
req = urllib.request.Request('http://www.cnblogs.com/cocoajin/p/3679821.html')
req.add_header('Referer', 'http://www.python.org/')
r = urllib.request.urlopen(req)
# print(r.read())
# 添加 user-agent
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
opener.open('http://www.example.com/')

url = 'http://www.cnblogs.com/cocoajin/p/3679821.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
    'act': 'login',
    'login[email]': '..',
    'login[password]': '123456'
}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
