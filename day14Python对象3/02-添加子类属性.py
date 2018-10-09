# Filename  : 02-添加子类属性.py
# Date  : 2018/8/2
"""
对象属性的继承：是通过继承init方法来继承的对象属性
给当前类添加对象属性：重写init方法，如果需要保留父类的对象属性，需要使用
super()去调用父类的init方法

多态：同一个事物有多种形态，子类继承父类的方法，可以对方法进行重写，
一个方法就有多种形态（多态的表现）
类的多态：继承产生多态
"""

class Person:
    def __init__(self, name='', age=2):
        self.name = name
        self.age = age

class Staff(Person):
    # init方法的参数：保证在创建对象的时候就可以给某些属性赋值
    def __init__(self, name):
        super().__init__(name)
        self.salary = 0

if __name__ == '__main__':
    s1 = Person()
    s1.__init__('wd', 12)
    print(s1.name, s1.age)


# 练习
"""
声明人类，有属性，名字、年龄、性别。身高
要求创建人的对象的时候可以给名字、性别、年龄赋初值

再创建学生类继承自人类，拥有人类的所有的属性，再添加学号、
成绩、电话属性
要求创建学生对象的时候可以给名字、年龄和电话赋初值
"""

class Human:
    def __init__(self,   name, age=0, sex='男'):
        self.name = name
        self.height = 0
        self.age = age
        self.sex = sex

class Student(Human):
    def __init__(self, name, age, tel):
        super().__init__(self, name, age)
        self.score = 0
        self.id_num = 0
        self.tel = 13
