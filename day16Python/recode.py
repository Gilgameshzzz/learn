# Filename  : recode.py
# Date  : 2018/8/6
"""
1、pygame

2、面向对象
什么是类
什么是对象

a、怎么声明类
class 类名（父类）：
    类说明
    属性
    方法
b、通过类创建对象
对象名 = 类名（） -->构造方法
调用构造方法创建对象的时候，会自动调用类的init方法，来给对象的属性赋初值

c、__init__方法
不用自己调用：参数有哪些，参数需不需要默认值，全看在创建对象的时候是否需要给相应属性赋初值和是否必须赋初值

d、关于属性
对象属性：不同的对象对应的值可能不一样，这样的属性可以声明称对象属性
对象来使用
增删改查
类的字段：
类来使用
__slots__ :一旦给类设置了这个属性的值，对象的内置类属性（__dict__）就没有用了

内置类属性（对象\类.__dict__, 类.__name__,对象.__class__(获取对象的类), 类.__doc__）
私有属性和假的私有属性
getter\setter:想要在获取对象属性的值前，或者是给属性赋值前干点别的事情

@property
def 属性名（self）:
    return 值

@属性名.setter
def 属性名（self,value）:
    self.属性 = value

e、类的方法
对象方法
类方法
静态方法

f.继承（支持多继承,但是一般不使用）
让子类直接拥有父类的所有的属性和方法（私有的除外），__slots__值不会被继承

重写：
多态
运算符重载

3、正则表达式
a、符号（. \w \d \s \b \W \D \S \B [] [^]）
"""
class Animal:
    def __init__(self):
        self.name = ''
        self.age = 0

class Fly:
    def fly(self):
        print('can fly')

class Bird(Animal, Fly):
    pass

class Person:
    pass

class Cat:
    """定义了一个Cat类"""

    #初始化对象
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        return "%s的年龄是:%d"%(self.name, self.age)

    #方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("%s的年龄是:%d"%(self.name, self.age))
class Test(object):
    def __init__(self, world):
        self.world = world

    def __str__(self):
        return 'world is %s str' % self.world

    def __repr__(self):
        return 'world is %s repr' % self.world

t = Test('world_big')
print (t)
print (t.__repr__())
#创建一个对象
tom = Cat("汤姆", 40)

lanmao = Cat("蓝猫", 10)
class Test(object):
    def __init__(self, value='hello, world!'):
        self.data = value
class Test(object):
    def __init__(self, value='hello, world!'):
        self.data = value
t = Test()

class TestRepr(Test):
    def __repr__(self):
        return 'TestRepr(%s)' % self.data


# 重构__repr__方法后，不管直接输出对象还是通过print打印的信息都按我们__repr__方法中定义的格式进行显示了

# 重构__str__


if __name__ == '__main__':
    p = Person()
    # print(p.__class__, p.__class__.__name__)
    #
    # print(tom)
    # print(lanmao)