"""__author__ = 余婷"""
"""
继承后，子类可以拥有除父类继承的内容以外的其他的内容

1.关于方法
1）.在子类中可以直接添加其他的方法
2）.重写：
a.完全重写
重新实现从父类继承下来的方法，重写后，子类再调用这个方法的时候，就调用子类的
b.保留父类实现的功能，再添加新的功能

对象和类调用方法的过程：先看当前类是否存在这个方法，没有才看父类有没有这个方法；
                    如果父类没有就看父类的父类有没有，直到找到基类(object)为止

"""


class Animal(object):
    """动物类"""
    def __init__(self):
        self.age = 0
        self.color = ''

    def eat(self):
        print('吃东西')

    def shout(self):
        print('叫唤')

    @classmethod
    def get_number(cls):
        return 100


class Dog(Animal):
    """狗类"""
    def look_after(self):
        print('看家')

    #  重写父类的shout
    def shout(self):
        print('汪汪汪~')

    # 重写父类eat方法
    def eat(self):
        # 保留父类eat的功能
        super().eat()
        print('吃骨头')

    @classmethod
    def get_number(cls):
        # 保留父类的类方法的功能的时候，还是super().类方法
        print(super().get_number())


if __name__ == '__main__':
    dog = Dog()
    dog.age = 3
    print(dog.color)
    dog.shout()
    dog.look_after()
    dog.eat()

    an = Animal()
    # 继承后，父类不能使用在子类中添加的属性和方法
    # an.look_after()
    an.eat()

    Dog.get_number()

