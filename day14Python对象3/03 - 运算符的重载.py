# Filename  : 03 - 运算符的重载.py
# Date  : 2018/8/2
"""
重载：一个类中可以有多个名字相同的方法，但是参数不一样，就叫重载，python中不支持

"""
class Student:
    # Python不支持方法的重载
    # def run(self):
    #     print('人在跑')

    def run(self, name):
        print('%s在跑' % name)

"""
2、运算符重载（重新定义运算符运算的过程）
>、<
大于和小于符号只需要重载其中的一个，另外一个的结果，直接是重的结果取反
+、-
"""
class Student2:
    def __init__(self):
        pass


    def __gt__(self, other):
        # 比较对象1>对象2的时候是比较他们的height属性
        return self.height > other.height

if __name__ == '__main__':
    pass