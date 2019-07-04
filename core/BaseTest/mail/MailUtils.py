#D:\DevelopTools\Softs\64\Python\Python35
#coding=UTF-8
#-*-coding: UTF-8 -*-
import smtplib
import Mail

class MailUtils:
    def sendMail(self, mail):
        try:  
            server = smtplib.SMTP()
            server.connect(mail.getHost())
            server.login(mail.getUser(),mail.getPWD())
            print(mail.mail_info)
            server.sendmail(mail.getUser(), mail.getToList(),\
                           mail.mail_info.as_string())
            print('success')
            return True  
        except Exception as e:
            print('fail')
            raise e
        finally:
            server.close()
        return False
if __name__ == '__main__':
    mail = Mail.Mail()
    mail.setMessage('HELLOID', '', '')
    mail.setSubject('test')
    lists = ['D:\\DevelopTools\\Projects\\python\\coreBase\\BaseTest\\BaseTest.py', \
             'D:\\DevelopTools\\Projects\\python\\coreBase\\BaseTest\\opjectTest.py']
    listnames = ['2BaseTest.py', \
             '3pjectTest.py']
    mail.setAttachmentList(lists, '', '', listnames)
    mail.setPic('test PIC', 'D:\\DevelopTools\\ORG\\WEBPictrues\\1.jpg', '', '')
    mailsend = MailUtils()
    mailsend.sendMail(mail)
    pass
