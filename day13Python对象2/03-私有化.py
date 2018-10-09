# Filename  : 03-私有化.py
# Date  : 2018/8/1

"""
python中类中的属性和方法的私有化，直接在属性名或方法名前加__(命名的以'__'开头)
属性或方法私有：在外部不能直接使用，可以在类的内部使用
"""


class Person:
    # 私有的类字段
    __number = 23

    def __init__(self, name='', age=9):
        self.name = name
        self.__age = age

    def show_age(self):
        print('%d' % (self.__age -10))
        self.__run()

    #     私有的对象方法，只能在类的内部调用
    def __run(self):
        print('%s在跑' % self.name)

#     私有的类方法
    @classmethod
    def __get_number(cls):
        print(cls.__number)


if __name__ == '__main__':
    p1 = Person()

