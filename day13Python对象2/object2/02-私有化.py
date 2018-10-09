"""__author__ = 余婷"""

"""
python中类中的属性和方法的私有化：直接在属性名或者方法名前加__(命名的以'__'开头)
属性或者方法私有：在外部不能直接使用, 可以在类的内部使用

"""

class Person:
    # 私有的类字段
    __number = 61

    """人类"""
    def __init__(self, name='', age=0):
        self.name = name
        self.__age = age

    def show_age(self):
        print('%d' % (self.__age - 10))
        self.__run()

    # 私有的对象方法，只能在类的内部调用
    def __run(self):
        print('%s在跑' % self.name)

    # 私有的类方法
    @classmethod
    def __get_number(cls):
        print(cls.__number)


import random
class Student:
    def __init__(self, name):
        self.name = name
        self.study_id = ''


    def __creat_id(self):
        return 'py1805'+ str(random.randint(1, 50)).rjust(3, '0')

    def creat(self, name):
        stu = Student(name)
        stu.study_id = self.__creat_id()
        return stu



if __name__ == '__main__':
    p1 = Person('张三', 30)
    p1.name = '李四'
    # p1.age = 28
    # print(p1.name, p1.__age)
    p1.show_age()

    # print(Person.__number)

    # Person.__get_number()

    # 私有化的原理：在内部在私有的名字前加了前缀'_类名'
    print(p1.__dict__['_Person__age'])
