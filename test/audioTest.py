# D:\DevelopTools\Softs\64\Python\Python35
# coding=UTF-8
#-*-coding: UTF-8 -*-
##import wav
# wav.play("E:\Music\1.mp3")
##import time
##import sys
##
##soundFile = 'E:\Music\08.���֮��.wav'
##not_executed = 1
##
# def soundStart():
# if sys.platform[:5] == 'linux':
##        import os
##        os.popen2('aplay -q' + soundFile)
# else:
##        import winsound
##        winsound.PlaySound(soundFile, winsound.SND_FILENAME)
##
# while(not_executed):
##    dt = list(time.localtime())
##    hour = dt[3]
##    minute = dt[4]
# if hour != 17 and minute != 38: # ����5��33�ֵ�ʱ��ʼ��ʾ
# soundStart()
##    not_executed = 0
##import mp3play
##filename = r'E:\Music\08.���֮��.wav'
##mp3 = mp3play.load(filename)
##
# mp3.play()
##
# Let it play for up to 30 seconds, then stop it.
##import time
##time.sleep(min(30, mp3.seconds()))
# mp3.stop()
import winsound
filename = r'E:\Music\08.���֮��.wav'
winsound.PlaySound(filename, 1)
