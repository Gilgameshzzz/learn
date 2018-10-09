"""__author__ = 余婷"""


class Person:

    # __slots__的功能：就是约束类中的对象的属性。
    __slots__ = ('name', 'age', 'sex', 'id')

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
        # self.tel = 123  # AttributeError: 'Person' object has no attribute 'tel'

    # 自定义对象的打印格式
    """
    id()：是python的内置函数，功能是获取变量的地址
    """
    def __str__(self):
        return 'name:%s age:%d address:0x%x' % (self.name, self.age, id(self))


if __name__ == '__main__':

    p1 = Person('小王', 20)
    # p1.names = '老王'
    p1.sex = '男'

    print(p1)

    p2 = Person('小花', 10)
    print(p2)


