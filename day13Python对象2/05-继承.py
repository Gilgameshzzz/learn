# Filename  : 05-继承.py
# Date  : 2018/8/1
"""
子类：继承者
父类(超类)：被继承者

1、怎么继承
Python中类是可以继承的，并且支持多继承

class类名（父类）：
    '''类的说明文档'''
    属性
    方法
说明：python中所有的类默认继承Python的基类：object

2、能继承那些内容
继承：直接拥有父类的属性和方法（继承后父类的属性和方法还是存在的）
a、对象的属性和方法、类和字段和类方法、静态方法都可以继承(私有的继承无意义--不能调用)
b、__slots__的值不会被继承
c、getter和setter会被继承

"""


class Person:
    """人类"""
    def __init__(self):
        self.name = ''
        self.age = 0
        self.sex = '男'
        self.__length = 0
        self._face = 0
    def eat(self):
        print('%s在吃饭' % self.name)

#     类字段
    number = 213

    @classmethod
    def get_number(cls):
        print('数量%s' % cls.number)

    @staticmethod
    def harm():
        print('harm moon')


class Student(Person):
    """学生类"""
    pass




if __name__ == '__main__':
    stu = Student()
    stu.name = '小伟'
    print(stu.name)
    stu.eat()
    print(stu.__dict__)
    stu.get_number()
    stu.harm()