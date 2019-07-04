# -*- coding: cp936 -*-
# 网络客户端
from ftplib import FTP
import os
f = FTP('ftp.pku.edu.cn')
f.login('anonymous', '-help@python.org')
f.dir()
##f.retrlines('RETR open')
f.quit()
print('exit')
os.system("pause")
