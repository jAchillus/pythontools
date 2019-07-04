from ftplib import FTP
import os
import thread
# os.system("pause")
from time import sleep, ctime
import thread


def loop0():
    print '111'
    sleep(4)
    print '22'


def loop1():
    print '333'
    sleep(3)
    print '5'


def main():
    loop0()
    loop1()


def main1():
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())

if __name__ == '__main__':
    main1()
