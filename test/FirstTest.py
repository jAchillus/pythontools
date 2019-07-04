#!
# -*- coding: cp936 -*-
"First Test"
import os,Tkinter,Image

from os import *
from Image import *
from Tkinter import *
from PIL import Image, ImageTk 
##from time import sleep
class Test(Frame):
    def resize(self,b):
        self.label.config(font = 'Helvetica -%d bold' % \
                    self.scale.get())
    
    def __init__(self, initdir=None):
##        Frame.__init__(self)
        self.top = Tk()
        self.top.bg = 'red'
        self.top.title = 'as'
        self.top.geometry('450x650+0+0')
        self.label = Tkinter.Label(self.top,text = 'hello World')
##        self.label.pack()
        self.scale = Tkinter.Scale(self.top,from_ = 1, to = 100,\
                    orient = HORIZONTAL,
                    command = self.resize
                                   )
        self.scale.set(12)
        self.scale.pack(fill = Y, expand = 1)
        self.quit = Tkinter.Button(self.top,text = 'HW',command = quit)
##        self.quit.pack();
        self.draw = Canvas(self.top, width="5i", height="5i", \
                           bg='white')
        self.draw.pack(side=LEFT)
        self.infile = 'E:\\Book\\Pictures\\照片\\WeChatImage635556958678397043.jpg'
        self.im = Image.open(self.infile)
        self.filename = ImageTk.PhotoImage(self.im)
        self.image1 = self.draw.create_image(50, 50, image=self.filename)
        self.ball = self.draw.create_oval("0.10i", "0.10i", \
                                          "0.50i", "0.50i",
                                          fill="red")
        
        self.draw.pack()  
    def say(self):
        print 'hello'
def main():
    
    test = Test()
####test.say()
    mainloop()
if __name__ == '__main__':
    main()
##urlopen("www.baidu.com")


