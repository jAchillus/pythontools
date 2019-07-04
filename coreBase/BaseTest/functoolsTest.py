# -*- coding:utf-8 -*-
#!D:/DevelopTools/softs/64/python35
import functools


def add(a, b):
    return a + b

add3 = functools.partial(add, 3)
add5 = functools.partial(add, 5)

print(add3(4))

print(add5(10))
