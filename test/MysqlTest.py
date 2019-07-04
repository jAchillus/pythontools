# D:/Dev/python
# coding=UTF-8
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='j', passwd='jiang123', db='test',
                           port=3306)
    cur = conn.cursor()
    cur.execute('select * from table1')
    value = [1, '1', 'hi rollen']
    #cur.execute('insert into table1 values(%s, %s, %s)',value)
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error as e:
    print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
file1 = open('MysqlTest.py', 'r')
for line in file1.readlines():
    print(line)
file1.close()
file1.delect()
if __name__ == '__main__':
    pass
