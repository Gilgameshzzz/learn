"""__author__ = 余婷"""
"""
1.pygame应用

2.面向对象
什么是类
什么是对象

a.怎么声明类
class 类名(父类):
    类说明
    属性
    方法  
    
b.通过类创建对象
对象名 = 类名()  --> 构造方法
调用构造方法创建对象的时候，会自动调用类的init方法，来给对象的属性赋初值  

c. __init__方法
不用自己调用；参数有哪些，参数需不需要默认值，全看在创建对象的时候是否需要给相应属性赋初值和是否必须赋初值

d.关于属性
对象属性：（不同的对象对应的值可能不一样，这样的属性可以声明称对象属性）
对象来使用
增删改（查）
__slots__: 一旦给类设置了这个属性的值，对象的__dict__属性就没有用了
类的字段：
类来使用

内置类属性（对象\类.__dict__，类.__name__, 对象.__class__, 类.__doc__, 类.__bases__, 类.__module__）
私有属性和假的私有属性
getter\setter: 想要在获取对象属性的值前，或者是给属性赋值前干点儿别的事情

@property
def 属性名(self):
    return 值
    
@属性名.setter
def 属性名(self, value):
    self.属性 = value

e.类的方法
对象方法
类方法
静态方法

f.继承（支持多继承,但是一般不使用） 
让子类直接拥有父类的所有的属性和方法(私有的除外)， __storts__值不会被继承

重写:
（多态）
运算符重载

3.正则表达式
a.符号（. \w \d \s \b \W \D \S \B [] [^] + * ? {N} {N,} {N,M} () |等）
b.re模块中的方法：匹配、查找、切割、替换
"""


class Animal:
    def __init__(self):
        self.name = ''
        self.age = 0



class Fly:
    def fly(self):
        print('can fly')

# 让Bird类同时继承Animal类和Fly类
class Bird(Animal, Fly):
    pass


class Person:
    pass


import re

if __name__ == '__main__':
    p = Person()
    p1 = p.__class__()
    print(p1, p)
    print(p.__class__.__name__, type(p.__class__.__name__))

    b = Bird()
    b.name = 'abc'
    b.fly()

    # [^]
    re_str = r'\+?[^1]abc'
    print(re.fullmatch(re_str, 'dnabc'))

    print(re.findall(r'(\+?)[^0]\d*', '+0123'))  # re.fullmatch(r'[+]?[^0]\d*', '+0123')


