"""__author__ = 余婷"""
"""
子类：继承者
父类(超类)：被继承者
1.怎么继承
python中类是可以继承的，并且支持多继承

class 类名(父类):
    '''类的说明文档'''
    属性
    方法  
    
说明：python中所有的类默认继承python的基类：object

2.能继承哪些内容
继承：直接拥有父类的属性和方法（继承后父类的属性和方法还是存在的）
a. 对象的属性和方法、类的字段和类方法、静态方法都可以继承（私有的继承无意义--不能继承）
b. __slots__的值不会被继承
c. getter和setter会被继承
"""


class Person:
    """人类"""
    __slots__ = ('name', 'age', 'sex', '__length', '_face')

    def __init__(self):
        self.name = ''
        self.age = 0
        self.sex = '男'
        self.__length = 0
        self._face = 0

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, face):
        self._face = face

    def eat(self):
        print(self.__length)
        print('%s在吃饭' % self.name)

    # 类字段
    number = 61

    @classmethod
    def get_number(cls):
        print('人类数量:%d' % cls.number)

    @staticmethod
    def hurt_earth():
        print('人类破坏地球')


class Student(Person):
    """学生类"""
    def study(self):
        pass


if __name__ == '__main__':

    p1 = Person()
    # p1.name2 = 'abc'

    stu = Student()
    stu.name = '小明'
    print(stu.name, stu.age, stu.sex)

    stu.eat()
    print(stu.__dict__)
    stu.name2 = 'abc'
    print(stu._face)

    print(Student.number)
    Student.get_number()
    Student.hurt_earth()

    stu.face = 100
    print(stu.face)


