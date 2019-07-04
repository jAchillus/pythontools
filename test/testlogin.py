#! D:\Programs\Python\Python35\python.exe
# python3
# -*- coding: utf-8 -*-
#import tesserocr
from PIL import Image
import pytesseract
import requests
from pytesseract import image_to_string
from PIL import Image, ImageEnhance
import re
import time

session = requests.Session()
login_url = 'xxxxxxxxxxxx'  # 登录url
random_url = 'xxxxxxxxxxxxx'  # 验证码url
tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'
loginname = '63001800'

# 账号密码等
data = {
    'username': 'root',
    'password': '123456'
}


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    }
    response = session.get(url, headers=headers)
    request = response.content
    with open('code.png', 'wb') as f:
        f.write(request)


def post_url(url, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    }
    response = session.post(url, data=data)
    home = session.get('#登录成功后访问某个url', headers=headers)
    print(home.text)


def binaryzation(threshold=140):  # 二值化
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


def sum_9_region_new(img, x, y):
    '''确定噪点 '''
    cur_pixel = img.getpixel((x, y))  # 当前像素点的值
    width = img.width
    height = img.height

    if cur_pixel == 1:  # 如果当前点为白色区域,则不统计邻域值
        return 0

    # 因当前图片的四周都有黑点，所以周围的黑点可以去除
    if y < 3:  # 本例中，前两行的黑点都可以去除
        return 1
    elif y > height - 3:  # 最下面两行
        return 1
    else:  # y不在边界
        if x < 3:  # 前两列
            return 1
        elif x == width - 1:  # 右边非顶点
            return 1
        else:  # 具备9领域条件的
            sum = img.getpixel((x - 1, y - 1)) \
                + img.getpixel((x - 1, y)) \
                + img.getpixel((x - 1, y + 1)) \
                + img.getpixel((x, y - 1)) \
                + cur_pixel \
                + img.getpixel((x, y + 1)) \
                + img.getpixel((x + 1, y - 1)) \
                + img.getpixel((x + 1, y)) \
                + img.getpixel((x + 1, y + 1))
            return 9 - sum


def collect_noise_point(img):
    '''收集所有的噪点'''
    noise_point_list = []
    for x in range(img.width):
        for y in range(img.height):
            res_9 = sum_9_region_new(img, x, y)
            if (0 < res_9 < 3) and img.getpixel((x, y)) == 0:  # 找到孤立点
                pos = (x, y)
                noise_point_list.append(pos)
    return noise_point_list


def remove_noise_pixel(img, noise_point_list):
    '''根据噪点的位置信息，消除二值图片的黑点噪声'''
    for item in noise_point_list:
        img.putpixel((item[0], item[1]), 1)


def image_identification(img):
    im = Image.open(img)
    image = im.convert('L')
    image = image.point(binaryzation(), '1')
    noise_point_list = collect_noise_point(image)
    remove_noise_pixel(image, noise_point_list)
    image.show()
    content = image_to_string(image, lang='eng', config=tessdata_dir_config)
    print(content, 'content')
    return content


def random_code(img):
    # get_url(random_url)  # 获取验证码并保存图片
    code = image_identification(img)
    code = re.sub(r"[a-z.A-Z |+-]+", '', code)  # 过滤验证码
    return code


if __name__ == "__main__1":
    flag = True
    while flag:
        code = random_code('Snipaste_2019-07-02_22-57-14.png')
        print('-----------------')
        print(code, type(code), len(code))
        if len(code) == 4:
            data['randomCode'] = code
            post_url(login_url, data)  # 登录
            print(data)
            flag = False

im = Image.open('Snipaste_2019-07-02_22-57-14.png')
print(pytesseract.image_to_string(im))
# im.show()
image = Image.open(r'Snipaste_2019-07-02_22-57-14.png')
image.show()
in1 = input()
print(in1)
#result = tesserocr.image_to_text(image)
# print(result)
