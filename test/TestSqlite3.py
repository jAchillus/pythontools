import sqlite3
import sys
import urllib
import urllib.request
import re


def createTable(cur, tableName, *cloums):
    strSql = "create table " + tableName + "("
    for x in range(0, len(cloums)):
        strSql += cloums[x]
        if x < len(cloums) - 1:
            strSql += ","
            pass
        pass
    strSql += ")"
    print(strSql)
    cur.execute(strSql)
    pass


def parseRe(data, reg):
    dataRe = re.compile(reg)
    dateList = dataRe.findall(data)
    return dateList
    pass

cx = sqlite3.connect("D:/own/tmp/test.db")
cur = cx.cursor()
# for t in[(0, 10, 'abc'), (1, 20, 'cba')]:
#    cx.execute("insert into TestSqlLit values (?,?,?)", t)
# createTable(cur, "baidu_tieba_users", "user_id integer primary key",
#             "user_name varchar(20) UNIQUE", "user_code varchar(10)", "level integer")
# createTable(cur, "baidu_tieba_users_addgroup", "user_id integer", "group_id integer")
cur.execute("delete from baidu_tieba_users")
# cur.execute("insert into baidu_tieba_users(user_id,user_name,user_code,level) values (?,?,?,?)", (217, '心念念谁o', '心念念谁o', '3'))
cx.commit()

cur.execute("select * from baidu_tieba_users")
out = cur.fetchall()

print(out)
# req = urllib.request.urlopen("http://tieba.baidu.com/home/main?un=%E4%B8%80%E4%B8%96%E7%9A%84%E5%AE%BF%E5%91%BD&ie=utf-8&fr=pb&ie=utf-8")
# response = req.read()
# response = response.decode('UTF-8')
# print(response)
# reg = r' href=\"(/home/main\?un=.*=home)\" locate'

# dateList = parseRe(response, reg)
# print(dateList)
# for dataurl in dateList:
#     urlData = dataurl[0]
#     print("%s" % (urlData))
#     di = urlData.split('.')
#     break

cx.close()
sys.exit(0)
