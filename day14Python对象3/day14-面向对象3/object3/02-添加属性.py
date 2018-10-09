"""__author__ = 余婷"""

"""
对象属性的继承：是通过继承init方法来继承的对象属性

给当前类添加对象属性: 重写init方法。
                   注意：如果要保留父类的对象属性，需要使用super()去调用父类的init方法

多态：同一个事物有多种形态。
方法的多态：子类继承父类的方法，可以对方法进行重写，一个方法就有多种形态（多态的表现）
类的多态：继承产生多态
"""

class Person(object):
    """人类"""
    def __init__(self, name, age=0, sex=''):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('人在吃饭')


class Staff(Person):
    # init方法的参数：保证在创建对象的时候就可以给某些属性赋值
    def __init__(self, name='', age=0, salary=0):
        super().__init__(name, age)
        self.salary = salary

    def eat(self):
        print('员工在吃饭')

class Scientist(Person):
    def eat(self):
        print('科学家在吃饭')


if __name__ == '__main__':
    p1 = Person('李四',sex='女')
    p1.eat()

    s1 = Staff(age=18)
    s1.sex = '男'
    print(s1.name)
    s1.salary = 10000
    print(s1.salary)
    s1.eat()


# 练习：
"""
声明人类，有属性，名字、年龄、性别、身高
要求创建人的对象的时候可以给名字、性别、年龄赋初值

再创建学生类继承自人类，拥有人类的所有的属性，再添加学号、成绩、电话属性
要求创建学生对象的时候可以给名字、年龄和电话赋初值
"""
class Person2:
    """人类"""
    a = 10

    def __init__(self, name, sex, age):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = 0


class Student(Person2):
    """学生类"""
    b = 100

    def __init__(self, name='', age=0, tel='00'):
        super().__init__(name, age=age, sex='女')
        self.study_id = '00'
        self.score = 0
        self.tel = tel


stu = Student('李四')
stu.sex = '男'
print(stu.age)

p1 = Person2('张三', '男', 18)





