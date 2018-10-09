# Filename  : 06-slots魔法.py
# Date  : 2018/7/31

class Person:
    """__slots__的功能：就是约束类中的对象的属性"""
    __slots__ = ('name', 'age')
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    # 自定义对象的打印格式
    """id():是python的内置函数，功能是获取变量的地址"""
    def __str__(self):
        return '人类'+' '+str(id(self))

if __name__ == '__main__':

    p1 = Person('小王', 20)
    p1.name = '老王'
    print(p1)