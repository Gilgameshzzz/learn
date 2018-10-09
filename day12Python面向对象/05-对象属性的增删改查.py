# Filename  : 05-对象属性的增删改查.py
# Date  : 2018/7/31

class Dog:
    """狗类"""
    def __init__(self, age=0, color='blue'):
        self.age = age
        self.color = color

if __name__ == '__main__':
    dog1 = Dog(3, 'white')
    # 1、查（获取属性）
    """方法一：对象.属性（如果属性不存在，会报错）"""
    print(dog1.age, dog1.color)
    """方法二：对象.__getattribute__(属性名)和getattr(对象，属性名，默认值)"""
    dog1.__getattribute__('age')
    getattr(dog1, 'age')

    #如果设置了default的值， 那么当属性不存在的时候不会报错，并且返回默认值
    # 2、改（修改对象属性的值）。
    """方法一：对象.属性 = 新值"""
    dog1.age = 4
    print(dog1.age)
    """方法二： 对象.__setattr__(属性名，新值)"""
    dog1.__setattr__('color', 'black')
    print(dog1.color)
    setattr(dog1, 'color', 'red')
    print(dog1.color)


    # 3、增加
    """
    对象.属性 = 值（属性不存在）
    注意：属性是添加给对象的，而不是类的
    """
    dog1.name = '千户'
    dog1.__setattr__('type', '哈士奇')
    print(dog1.type)

    setattr(dog1, 'sex', '公')
    print(dog1.sex)
    # 4、删（删除对象的属性）
    """
    del 对象.属性（属性要存在，才能删除）
    注意：删除属性也是删的具体某个对象的属性。不会影响这个类其他对象
    """
    del dog1.age


    dog1.__delattr__('sex')
    delattr(dog1, 'color')

    # 练习：声明一个学生类，拥有属性：姓名，性别、年龄、方法：学习
    # 1、声明学生类的对象，声明的时候就给姓名、性别和年龄赋值
    # 2、通过三种方式分别获取姓名、性别和年龄，并且打印
    # 3、给学生对象添加一个属性，电话
    # 4、修改学生的年龄
    # 5、删除学生的性别

    class Student:
        def __init__(self, name='', sex='男', age='13'):
            self.name = name
            self.sex = sex
            self.age = age

        def study(self):
            print('%s正在学习' % self.name)


    student1 = Student('Luck', '女', '18')
    print(student1.name, student1.sex, student1.age)
    student1.age = '21'
    student1.__setattr__('tel', '324')
    print(student1.tel)


