# -*- coding: cp936 -*-
from Tkinter import * 
 
master = Tk() 
 
w = Canvas(master, width=200, height=100) 
w.pack() 
 
w.create_line(0, 0, 200, 100) 
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4)) 
 
w.create_rectangle(50, 25, 150, 75, fill="blue") 
 
mainloop() 
 
##tk 默认处理图片格式为gif 处理其他格式的图片，否则需要下载image的mod，这个大家百度下。
# -*- coding:utf-8 -*- 
# file: TkinterCanvas.py 
# 
import Tkinter         # 导入Tkinter模块 
from PIL import Image, ImageTk 
 
root = Tkinter.Tk() 
canvas = Tkinter.Canvas(root, 
    width = 500,      # 指定Canvas组件的宽度 
    height = 600,      # 指定Canvas组件的高度 
    bg = 'white')      # 指定Canvas组件的背景色 
#im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片 
image = Image.open("E:\\Book\\Pictures\\照片\\WeChatImage635556958678397043.jpg") 
im = ImageTk.PhotoImage(image) 
 
canvas.create_image(300,50,image = im)      # 使用create_image将图片添加到Canvas组件中 
canvas.create_text(302,77,       # 使用create_text方法在坐标（302，77）处绘制文字 
   text = 'Use Canvas'      # 所绘制文字的内容 
   ,fill = 'gray')       # 所绘制文字的颜色为灰色 
canvas.create_text(300,75, 
   text = 'Use Canvas', 
   fill = 'blue') 
canvas.pack()         # 将Canvas添加到主窗口 
root.mainloop() 
