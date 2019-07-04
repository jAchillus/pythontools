# -*- coding:utf-8 -*-
# -*- coding=utf-8 -*-
# coding=utf-8
# python version 3.5
''' 简单算法 '''


def bubbleSort():
    print('maopao start:')
    lists = [23, 43, 65, 12, 54]
    for x in range(0, len(lists)):
        for x1 in range(0, len(lists) - x - 1):
            if lists[x1] > lists[x1 + 1]:
                tmp = lists[x1]
                lists[x1] = lists[x1 + 1]
                lists[x1 + 1] = tmp

        print(str(x) + ':' + str(lists))
        pass
    print(lists)
    pass


def selectSort():
    print('selectSort start:')
    lists = [23, 43, 65, 12, 54]
    for x in range(0, len(lists)):
        for x1 in range(x + 1, len(lists)):
            if lists[x1] > lists[x]:
                tmp = lists[x1]
                lists[x1] = lists[x]
                lists[x] = tmp
        print(str(x) + ':' + str(lists))
        pass
    print(lists)
    pass


def inputsort():
    print('inputsort start:')
    lists = [23, 43, 65, 12, 54]
    for x in range(1, len(lists)):
        tmp = lists[x]
        ind = x
        for x1 in range(x - 1, -1, -1):
            print(str(x1) + ':' + str(lists[x1]))
            if lists[x1] > tmp:
                print("change:%s %s" % (lists[x1], tmp))
                lists[x1 + 1] = lists[x1]
                ind = x1
        lists[ind] = tmp
        print("curr:" + str(x) + str(lists[x]) + ':' + str(lists))
        pass
    print(lists)
    pass


def selectSort1():
    print('selectSort1 start:')
    lists = [23, 43, 65, 12, 54]
    for x in range(0, len(lists)):
        k = x
        for x1 in range(x + 1, len(lists)):
            if lists[x1] > lists[k]:
                k = x1
        if k != x:
            tmp = lists[x]
            lists[x] = lists[k]
            lists[k] = tmp
        print(str(x) + ':' + str(lists))
        pass
    print(lists)
    pass
# inputsort()


n = 10
m = (1, 2, 3)
t = 1
import sys
arr = [[]]*n
# 爬楼梯


def paolouti(curFloor, ar=[]):
    #global t
    # print('cur' + str(t))
    for j in m:
        # arr[t][]
        if curFloor + j == n:
            print(curFloor, end='  ')
            print(ar + [j], end='')
            print(' succ', t)
            #t = t + 1
            continue
        if curFloor + j > n:
            #print('guol', str(j))
            continue
        #print(j, end='')
        #print('->', end='')
        paolouti(curFloor + j, ar + [j])
    pass
paolouti(0)
