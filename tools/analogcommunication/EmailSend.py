# D:\DevelopTools\Softs\64\Python\Python35
# coding=UTF-8
#-*-coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

import logging
# 通过下面的方式进行简单配置输出方式与日志级别
# logging.basicConfig(filename='logger.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("-----mail send-----")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler('../../mail.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)

':name<:addr>'


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


class EmailSend:

    # 添加附件: 可以发送包括英文txt, jpg , mp3, 注意不能发送pdf doc excel ppt
    def add_attachment(filepath):
        ctype, encoding = mimetypes.guess_type(filepath)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        attachment = None
        if maintype == 'text':
            with open(filePath, 'rb') as fb:
                attachment = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'image':
            with open(filePath, 'rb') as fb:
                attachment = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'audio':
            with open(filePath, 'rb') as fb:
                attachment = MIMEAudio(fp.read(), _subtype=subtype)
                fb.close()
        else:
            attachment = MIMEBase(maintype, subtype)
            with open(filePath, 'rb') as f:
                attachment.set_payload(f.read())
                fb.close()
            encoders.encode_base64(attachment)

        baseName = os.path.basename(filepath)
        attachment.add_header('Content-Disposition', 'attachment', filepath=filepath,  filename=baseName)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        msg.attach(attachment)

    '''
    发送列表
    主体
    文本
    '''

    def send_mail(self, to_list, sub, content):
        fromA = mail_user + "@" + mail_postfix
        fromAddr = format_addr(mail_user < %s > % fromA)
        msg = MIMEText(content, _subtype='plain', _charset='gb2312')
        msg['Subject'] = Header(sub, 'utf-8').encode()
        msg['From'] = fromAddr
        msg['To'] = ";".join(to_list)
        msg['Cc'] = ";".join(to_list)
        msg['BCc'] = ";".join(to_list)
        # msg.add_header('Cc', cc)
        # msg.add_header('BCc', bcc)
        try:
            server = smtplib.SMTP()
            # server.set_debuglevel(1)
            server.connect(mail_host)
            server.login(mail_user, mail_pass)
            server.sendmail(fromAddr, to_list, msg.as_string())
            server.close()
            return True
        except Exception as e:
            logger.error(e)
            logger.exception(e)
            return False
        finally:
            pass
    pass
mailto_list = ['']
mail_host = "smtp-mail.outlook.com"  # 设置服务器
mail_user = "zhang."  # 用户名
mail_pass = ""  # 口令
mail_postfix = "iwhalecloud.com"  # 发件箱的后缀
mail = EmailSend()
if __name__ == '__main__':
    logger.info('start send!')
    if mail.send_mail(mailto_list, "hello", "hello world！"):
        logger.info('send sucess!')
    else:
        logger.info('send fail!')
