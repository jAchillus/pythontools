# -*- coding: cp936 -*-
# version 2
import Image
##from Image import *
infile = 'E:\\Book\\Pictures\\照片\\WeChatImage635556958678397043.jpg'
outfile = 'E:\\Book\\Pictures\\照片\\2.jpg'
im = Image.open(infile)
##im = Image.load(infile)
# im.show()
(x, y) = im.size  # read image size
x_s = 640  # define standard width
y_s = 526  # calc height based on standard width
out = im.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
out.save(outfile)

print('original size: ', x, y)
print('adjust size: ', x_s, y_s)

'''
OUTPUT:
original size:  500 358
adjust size:  250 179
'''
