# Filename  : 04 - 对象的属性.py
# Date  : 2018/7/31
"""
对象属性的声明
class 类名：
    def __init__(self):
        self.属性名 = 初值
        self.属性名2 = 初值2
"""
class Person:
    # 1、init方法是系统自带的一个方法，这个方法不能直接调用，通过类
    # 创建对象的时候系统会自动调用这个方法
    # init方法的作用是对对象的属性进行初始化
    # 2、通过构造方法创建对象的时候，一定要保证，init方法中除了self以外，
    # 其他的每个参数都必须有值

    def __init__(self, name1, age1):
        # 在这里声明对象的属性
        print('====')
        print(name1)
        # 在init方法中声明对象的属性
        """
        name, age 和sex就是Person这个类的对象属性，类的对象属性，需要通过对象来使用
        """
        self.name = name1
        self.age = age1
        self.sex = '女'



if __name__ == '__main__':
    # 注意;构造方法中的参数，实质是传给init方法的参数的
    p1 = Person('赌圣', 18)

    # 通过对象使用对象属性
    print(p1.name, p1.age, p1.sex)