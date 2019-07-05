#D:\DevelopTools\Softs\64\Python\Python35
#coding=utf-8

'''测试基本功能'''
globalVar = 'global'
class BaseTest(object):
    def __init__(self):
        print('hello\
              world')
        pass

    "赋值测试"
    def testAssign(self):
        y = y = 1 + 2
        #不可以,赋值不会返回值的
        #不支持自增自减
        #y = (y = 1 + 2)
        #多元赋值
        v1, v2, v3 = y, 1, 2
        (v1, v2, v3) = (y, 1, 2)
        pass
    
    "测试标识符"
    def testIdentifier(self):
        print(self.testAssign().__doc__)
        #断言
        assert 1 < 2
        #特殊变量加_,前后都行
        #_xxx,不用from module import *导入
        #__xxx__系统定义名字
        #__xxx类中私有变量
        pass

    "内存测试"
    def testMemory(self):
        s = '1'
        print(id(s))
        #删除
        del s
        print(s)
        pass
def test():
    print('test')
    pass

print('HI')

test()

"name是模块名或者main，看模块是执行的，还是被导入"
if __name__ == '__main__':
    print('start')
    base = BaseTest()
    base.testMemory()
   
