#D:/DevelopTools/softs/64/python35
#-*-coding = utf-8-*-
"测试数字"
class NumberTest:
    def __init__(self):
        pass

    def testNumber(self):
        aInt = 1
        del aInt
        #删除的是引用
        #print(aInt)
        aInt = 2
        print(aInt)
        #复数
        af = 3.3 + 1j
        print(af)
        #除
        ac = 1 / 2
        print(ac)
        # 地板除，取整
        ac = 1 // 2
        print(ac)
        
        ac1 = 1.0 / 2.0
        print('%f ,%f' % (ac, ac1))
    #位运算
    def testBit(self):
        #不循环
        a = 3 >> 1
        print(a)
        a = 3 & 2
        print(a)
        a = 3 | 2
        print(a)
        #异或，相同为0，不同为1
        a = 3 ^ 3
        print(a)
        #3.5不支持了
        #print(cmp(1, 2))
        #转换，第二参数设置进制
        a = int(3)
        print(a)
        #asc码
        print(ord('a'))
        print(chr(12))#数字转字符

        #进制转换
        print(hex(12))#16
        oct(12)#八进制
    def testOther(self):
        #对象没有__nonzero__()的为true
        bool(1)
        #注意，和2.7不同
        True,False == False, True
        print(bool(True))
        print(bool(False))
        
if __name__ == '__main__':
    num = NumberTest()
    num.testOther()
