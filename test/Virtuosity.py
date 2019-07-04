#! python3
# -*- coding: utf-8 -*-
#import http.server
# python  -m http.server 8012
# python  -m SimpleHTTPServer 8012
# 代码值互换
#a, b = 1, 2
#a, b = b, a
# FizzBuzz
# FizzBuzz问题：打印数字1到100, 3的倍数打印"Fizz", 5的倍数打印"Buzz", 既是3又是5的倍数的打印"FizzBuzz"
# for x in range(1, 101):
#    print("fizz"[x % 3 * 4:]+"buzz"[x % 5 * 4:] or x)

# Mandelbrot图像：图像中的每个位置都对应于公式N=x+y*i中的一个复数
#print('\n'.join([''.join(['*'if abs((lambda a: lambda z, c, n: a(a, z, c, n))(lambda s, z, c, n: z if n == 0 else s(s, z*z+c, c, n-1))(0, 0.02*x+0.05j*y, 40)) < 2 else ' ' for x in range(-80, 20)]) for y in range(-20, 20)]))
# 一行代码打印九九乘法表
#print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))

# 一行代码可以输出前100项斐波那契数列的值：
#print([x[0] for x in [(a[i][0], a.append((a[i][1], a[i][0]+a[i][1]))) for a in ([[1, 1]], ) for i in range(100)]])

# 打开浏览器
#import antigravity

# 自我
# import this
#
