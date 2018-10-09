"""__author__ = 余婷"""
"""
1.声明一个电脑类：
属性：品牌、颜色、内存大小
方法：打游戏、写代码、看视频
"""
class Computer:
    """电脑类"""
    def __init__(self, brand='', color='black', memory=0):
        self.brand = brand
        self.color = color
        self.memory = memory

    @staticmethod
    def play_game(game):
        print('打%s游戏' % game)

    @staticmethod
    def coding(code_type):
        print('写%s程序' % code_type)

    @staticmethod
    def watch_video(video):
        print('在看%s' % video)

"""
2.声明一个人的类和狗的类：
狗的属性：名字、颜色、年龄 狗的方法：叫唤
人的属性：名字、年龄、狗 人的方法：遛狗
a.创建人的对象小明，让他拥有一条狗大黄，然后让小明去遛大黄
"""
class Dog:
    """狗类"""
    def __init__(self, name='', color='', age=0):
        self.name = name
        self.color = color
        self.age = age

    def shout(self):
        print('%s：汪汪汪！！' % self.name)


class Person:
    """人类"""
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
        # None来表示对象的零值
        self.dog = None

    def walk_dog(self):
        """遛狗"""
        if self.dog == None:
            print('没🐶，遛自己吧!')
            return

        print('%s牵着%s在散步' % (self.name, self.dog.name))

"""
3.声明一个矩形类：
属性：长、宽 方法：计算周长和面积
a.创建不同的矩形，并且打印其周长和面积
"""
class Rectangle:
    """矩形类"""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        """求周长"""
        return (self.length + self.width)*2

    def area(self):
        """求面积"""
        return self.length * self.width


"""
4.创建一个学生类：
属性：姓名，年龄，学号 方法：答到，展示学生信息 
创建一个班级类：
属性：学生，班级名 方法：添加学生，删除学生，点名
"""
from random import randint

class Student:
    """学生类"""
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
        self.study_id = 'py1805'+str(randint(0, 50))

    def answer(self):
        print('%s，到！' % self.name)

    def show(self):
        print('姓名:%s 年龄:%d 学号:%s' % (self.name, self.age, self.study_id))


class Class:
    """班级类"""
    def __init__(self, name=''):
        self.name = name
        self.students = []

    def append_student(self, student=None):
        """添加学生"""
        self.students.append(student)

    def del_student(self, name):
        """删除学生"""
        for student in self.students[:]:
            if student.name == name:
                self.students.remove(student)

    def call_names(self):
        """点名"""
        for student in self.students:
            # 点名
            print(student.name)
            # 答到
            student.answer()


"""
5.写一个类，封装所有和数学运算相关的功能（包含常用功能和常用值，例如：pi,e等）
"""
class Math:
    """数学类"""
    pi = 3.1415926
    e = 2.718

    @staticmethod
    def sum(*number):
        """求和"""
        sum1 = 0
        for x in number:
            sum1 += x
        return sum1

    @classmethod
    def cricle_area(cls, radius):
        """求圆的面积"""
        return radius**2*cls.pi



if __name__ == '__main__':
    """第一题"""
    cm = Computer()
    cm.memory = 512
    cm.brand = '惠普'
    Computer.play_game('贪吃蛇')
    # 添加属性
    # cm.price = 998
    setattr(cm, 'price', 998)
    print(cm.price)

    # 删除属性
    # del cm.color
    cm.__delattr__('price')

    # 修改属性
    # cm.memory = 258
    cm.__setattr__('memory', 1024)

    """第二题"""
    p1 = Person('小明', 18)
    p1.dog = Dog('大黄', 'yellow', 3)
    p1.walk_dog()

    """第三题"""
    rect1 = Rectangle(10, 20)
    print(rect1.area(), rect1.perimeter())

    rect2 = Rectangle(100, 30)
    print(rect2.perimeter())

    """第四题"""
    stu1 = Student('张三', 20)
    stu2 = Student('aa', 18)
    stu3 = Student('bb', 30)

    class1 = Class('py1805')
    class1.append_student(stu1)
    class1.append_student(stu2)
    class1.append_student(stu3)
    class1.call_names()


    # 注意：如果函数的参数是对象(列表、字典、类的对象)，传参的时候传的是地址，如果函数中需要对象的内容进行修改，
    #      传参的时候传对象的拷贝(如果是列表可以切片)
    def func1(list1):
        list1.append(10)
        print(list1)

    def func2(lista):
        lista.append(20)
        print(lista)

    list11 = [1, 2, 3, 4]
    func1(list11[:])
    func2(list11[:])
    print(list11)

    print(Math.sum(10, 2, 3))
    print(Math.cricle_area(3))
    print(Math.pi)






