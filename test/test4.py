# -*- coding: cp936 -*-
from Tkinter import * 
 
master = Tk() 
 
w = Canvas(master, width=200, height=100) 
w.pack() 
 
w.create_line(0, 0, 200, 100) 
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4)) 
 
w.create_rectangle(50, 25, 150, 75, fill="blue") 
 
mainloop() 
 
##tk Ĭ�ϴ���ͼƬ��ʽΪgif ����������ʽ��ͼƬ��������Ҫ����image��mod�������Ұٶ��¡�
# -*- coding:utf-8 -*- 
# file: TkinterCanvas.py 
# 
import Tkinter         # ����Tkinterģ�� 
from PIL import Image, ImageTk 
 
root = Tkinter.Tk() 
canvas = Tkinter.Canvas(root, 
    width = 500,      # ָ��Canvas����Ŀ�� 
    height = 600,      # ָ��Canvas����ĸ߶� 
    bg = 'white')      # ָ��Canvas����ı���ɫ 
#im = Tkinter.PhotoImage(file='img.gif')     # ʹ��PhotoImage��ͼƬ 
image = Image.open("E:\\Book\\Pictures\\��Ƭ\\WeChatImage635556958678397043.jpg") 
im = ImageTk.PhotoImage(image) 
 
canvas.create_image(300,50,image = im)      # ʹ��create_image��ͼƬ��ӵ�Canvas����� 
canvas.create_text(302,77,       # ʹ��create_text���������꣨302��77������������ 
   text = 'Use Canvas'      # ���������ֵ����� 
   ,fill = 'gray')       # ���������ֵ���ɫΪ��ɫ 
canvas.create_text(300,75, 
   text = 'Use Canvas', 
   fill = 'blue') 
canvas.pack()         # ��Canvas��ӵ������� 
root.mainloop() 
