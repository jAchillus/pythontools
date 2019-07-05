#D:\DevelopTools\Softs\64\Python\Python35
#coding=UTF-8
#-*-coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

"邮件类，保存发送的一些基本数据"
class Mail:
    MSG_SUBJECT = 'Subject'
    MSG_FROM = 'From'
    MSG_TO = 'To'
    MAIL_SEPARATOR = ';'
    MAIL_SUB_TYPE_PLAIN = 'plain'
    MAIL_SUB_TYPE_HTML = 'html'
    MIAL_CONTENS_CHAR_UTF8 = 'UTF-8'
    MIAL_CONTENS_CHAR_GBK = 'gb2312'

    "服务器"
    mail_host="smtp.sina.com"
    #用户名
    mail_user="tsrjwwdz@sina.com"
    #口令 
    mail_pass=""
    #发件箱的后缀  
    #mail_postfix="sina.com"
    "发送对象"
    mail_to_list=['zhangdongjiangyx@163.com']
    # 邮件信息
    mail_info = MIMEMultipart()
    mail_subject = ''
    #邮件内容
    mail_message = {}
    #附件
    mail_attachmentFileList = []
    #附件
    mail_attachment = MIMEMultipart()
    #图片
    mail_pic = MIMEMultipart()
    
    def __init__(self):
        #self.mail_info.attach(self.mail_message)
        #self.mail_info.attach(self.mail_attachment)
        #self.mail_info.attach(self.mail_pic)
        pass
    
    #设置用户
    def setUser(self, user):
        self.mail_user = user
        self.mail_info[self.MSG_FROM] = '<' + self.mail_user + '>'
        setMsgFrom(self.mail_user)

    def getUser(self):
        return self.mail_user

    #设置服务器
    def setHost(self, host):
        self.mail_host = host

    def getHost(self):
        return self.mail_host
        
    #设置密码
    def setPWD(self, pwd):
        self.mail_pass = pwd

    def getPWD(self):
        return self.mail_pass

    #设置发送邮件
    def setToList(self, toList):
        self.mail_to_list = toList
        self.mail_info[self.MSG_TO] = self.MAIL_SEPARATOR.join(self.mail_to_list)
        #设置信息中的地址
        self.setMsgToList(self.mail_to_list)

    def getToList(self):
        return self.mail_to_list

    #设置主题
    def setSubject(self, sub):
        self.mail_subject = sub
        self.mail_info[self.MSG_SUBJECT] = sub

    def getSubject(self):
        return self.mail_subject
        
    #增加发送邮件
    def addTo(self, toAdd):
        length = len(self.mail_to_list)
        self.mail_to_list[length] = toAdd

    def getMailInfo(self):
        return self.mail_info
    
    #设置邮件内容，外部组装好
    def setMessage(self, msg):
        self.mail_message = msg
    #不需要
    def setMsgToList(self, toList):
        if self.MSG_TO in self.mail_message:
            self.mail_message[self.MSG_TO] = self.MAIL_SEPARATOR.join(toList)

    #不需要
    def setMsgFrom(self, fromAdd):
        if self.MSG_FROM in self.mail_message:
            self.mail_message[self.MSG_FROM] =self.mail_message[self.MSG_SUBJECT] \
                                       + '<' + fromAdd + '>'

    def getSubType(self, subtype):
        if subtype.strip():
            return subtype
        else:
            return self.MAIL_SUB_TYPE_PLAIN
        
    def getEncode(self, encode):
        if encode.strip():
            return encode
        else:
            return 'base64'
        
    def getCharset(self, charset):
        if charset.strip():
            return charset
        else:
            return self.MIAL_CONTENS_CHAR_UTF8
        
    #设置基本信息返回生成的msg,不需要发送信息
    def setMessage(self, content, subtype, charset):
        subtype = self.getSubType(subtype)
        charset = self.getCharset(charset)

        msg = MIMEText(content,_subtype=subtype,_charset=charset)
        self.mail_message = msg
        self.mail_info.attach(self.mail_message)
        return self.mail_message
        
    #设置基本信息返回生成的msg
    def setMessage1(self, sub, content, subtype, charset):
        subtype = self.getSubType(subtype)
        charset = self.getCharset(charset)
        
        msg = MIMEText(content, _subtype=subtype, _charset=charset)
        msg[self.MSG_SUBJECT] = sub
        msg[self.MSG_FROM] = sub + '<' + self.mail_user + '>'
        msg[self.MSG_TO] = self.MAIL_SEPARATOR.join(self.mail_to_list)
        self.mail_message = msg
        return msg

    #设置附件
    def setAttachmentList(self, attachFileList, encode, charset, fileShowNameList):
        self.mail_attachmentFileList = attachFileList
        # 重置
        self.mail_attachment = MIMEMultipart()
        i = 0
        for file in attachFileList:
            if not fileShowNameList:
                fileShowName = fileShowNameList[i]
            else:
                fileShowName = file

            #添加
            self.setAttach(file, encode, charset, fileShowName)
            i += 1
        
        self.mail_info.attach(self.mail_attachment)
    def addAttachment(self, attachFile, encode, charset, fileShowName):
        length = len(self.mail_attachmentFileList)
        self.mail_attachmentFileList[length] = attachFile
        #添加
        self.setAttach(attachFile, encode, charset, fileShowName)
        
    #附件文件转为邮件使用的
    def setAttach(self, fileName, encode, charset, fileShowName):
        #构造附件1
        attach = MIMEText(open(fileName, 'rb').read(), self.getEncode(encode),\
                          self.getCharset(charset))
        attach["Content-Type"] = 'application/octet-stream'
        #这里的filename可以任意写，写什么名字，邮件中显示什么名字
        attach["Content-Disposition"] = fileShowName

        self.mail_attachment.attach(attach)

    #添加图片
    def setPic(self, text, picFile, encode, charset):
        #构造附件1
        txt = MIMEText(text, self.getEncode(encode), self.getCharset(charset))
        self.mail_pic.attach(txt)
        image = MIMEImage(open(picFile,'rb').read())
        image.add_header('Content-ID','<image1>')
        self.mail_pic.attach(image)

        
        self.mail_info.attach(self.mail_pic)
    
if __name__ == '__main__':
    mail = Mail()
    
    #msg = mail.setMessage('hell', 'asd', 'a', 'utf-8')
    #print(msg)
    if '2' in mail.mail_message:
        print('1' + mail.mail_message['2'])
    mail.setToList(['tsrjwwdz@sd.com'])#=['tsrjwwdz@sd.com']
    #print(msg)
    print('2' + str(mail.mail_message))
