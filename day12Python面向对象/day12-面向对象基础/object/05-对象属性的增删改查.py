"""__author__ = 余婷"""

class Dog:
    """狗类"""
    def __init__(self, age=0, color='yellow'):
        self.age = age
        self.color = color



if __name__ == '__main__':

    dog1 = Dog(3,'white')


    # 1.查（获取属性）
    """
    方法一：对象.属性 (如果属性不存在，会报错)
    方法二：对象.__getattribute__(属性名) 和 getattr(对象, 属性名, 默认值)
    """
    print(dog1.age, dog1.color)

    print(dog1.__getattribute__('age'))
    print(getattr(dog1, 'age'))

    # 如果设置了default的值，那么当属性不存在的时候不会报错，并且返回默认值
    print(getattr(dog1, 'abc', '无名氏'))

    # 2.改（修改属性的值）
    """
    方法一： 对象.属性 = 新值
    方法二：对象.__setattr__(属性名,新值) 和  setattr(对象，属性名，新值)
    """
    dog1.age = 4
    print(dog1.age)

    dog1.__setattr__('color', 'black')
    print(dog1.color)

    setattr(dog1, 'color', 'blue')
    print(dog1.color)



    # 3.增加（增加对象属性）
    """
    对象.属性 = 值（属性不存在）
    注意：属性是添加给对象的，而不是类的
    """
    dog1.name = '大黄'
    print(dog1.name)

    dog1.__setattr__('type', '哈士奇')
    print(dog1.type)

    setattr(dog1,'sex', '公')
    print(dog1.sex)

    # dog2 = Dog()
    # print(dog2.name)

    # 4.删（删除对象的属性）
    """
    方法一： del 对象.属性
    
    注意：删除属性也是删的具体某个对象的属性。不会影响这个类的其他对象
    """
    # del dog1.age
    # print(dog1.age)  # AttributeError: 'Dog' object has no attribute 'age'

    # dog1.__delattr__('age')
    # print(dog1.age) # AttributeError: 'Dog' object has no attribute 'age'

    delattr(dog1, 'color')
    # print(dog1.color)  # 'Dog' object has no attribute 'color'


"""
练习：声明一个学生类，拥有属性：姓名、性别、年龄。方法：学习
1.声明学生类的对象，声明的时候就给姓名、性别和年龄赋值
2.通过三种方式分别获取姓名、性别和年龄，并且打印
3.给学生对象添加一个属性，电话
4.修改学生的年龄
5.删除学生的性别
"""
class Student:
    def __init__(self, name='', age=0, sex=''):
        self.name = name
        self.sex = sex
        self.age = age

    def study(self):
        print('%s学习' % self.name)


stu1 = Student('小明', 30, '男')

print(stu1.name)
print(stu1.__getattribute__('age'))
print(getattr(stu1, 'sex'))

stu1.tel = '123333'

stu1.age = 35

del stu1.sex

stu1.study()

