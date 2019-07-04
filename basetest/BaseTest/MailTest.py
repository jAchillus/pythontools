# D:\DevelopTools\Softs\64\Python\Python35
# coding=UTF-8
#-*-coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
mailto_list = ['tsrjwwdz@sina.com']
mail_host = "smtp.sina.com"  # 设置服务器
mail_user = "tsrjwwdz"  # 用户名
mail_pass = ""  # 口令
mail_postfix = "sina.com"  # 发件箱的后缀
import logging


class MailTest:

    def send_mail(self, to_list, sub, content):
        me = "hello"+"<"+mail_user+"@"+mail_postfix+">"
        msg = MIMEText(content, _subtype='plain', _charset='gb2312')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP()
            server.connect(mail_host)
            print("hello")
            server.login(mail_user, mail_pass)
            print("hello")
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception as e:
            print(e)
            logging.exception(e)
            return False
        finally:
            pass
    pass
li = [2, 3, 4]


def sd(se):
    msg = {}
    msg['w'] = li
    return msg
if __name__ == '__main__':
    mail = MailTest()
    if mail.send_mail(mailto_list, "hello", "hello world！"):
        print("发送成功")
    else:
        print("发送失败")
    s = [1, 2, 3]
    md = sd(s)
    print(md['w'])
    li[1] = 12
    print(md['w'])
