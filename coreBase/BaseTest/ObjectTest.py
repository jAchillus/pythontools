#D:\DevelopTools\Softs\64\Python\Python35
#coding=UTF-8

"python对象"
class ObjectTest(object):
    def __init__(self):
        print(type(self))
        pass

    "切片"
    def testChip(self):
        foost = 'asdfghj'
        #负数步长从后往前
        print(foost[::-1])
        print(foost[::-2])
        #sequenst[start: end: step]
        #不包含结束
        print(foost[0:7:2])
        #结尾第二个结束，不包含结尾第二个
        print(foost[:-2])
        
        pass

    def testEquals(self):
        #缓存string和int，id相同。其它类型不会
        
        a = 'a'
        a = 1.1
        b = a
        a = 2.1
        a is b
        a is not b
        啊 = 1
        print(b + 啊)
        #equal
        cmp(a, b)
        #return string
        repre(a)
        #return for read string
        str(a)
        pass
    pass
if __name__ == '__main__':
    objct = ObjectTest()
    objct.testEquals()
    #print('main')
    pass
