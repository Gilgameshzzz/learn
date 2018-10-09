"""__author__ = 余婷"""
"""
对象属性的声明
class 类名:
    def __init__(self):
        self.属性名 = 初值
        self.属性名2 = 初值2
"""


class Person:
    """人类"""
    """
    1.init方法是系统自带的一个方法，这个方法不能直接调用，通过类创建对象的时候系统会自动调用这个方法
    init方法的作用是对对象的属性进行初始化
    2.通过构造方法创建对象的时候，一定要保证，init方法中除了self以外，其他的每个参数都必须有值
    """
    def __init__(self, name1='', age1=0, sex='女'):
        # 在这个地方声明对象的属性
        # 在init方法中声明对象的属性
        """
        name、age和sex就是Person这个类的对象属性。类的对象属性，需要通过对象来使用
        """
        self.name = name1
        self.age = age1
        self.sex = sex

    def run(self, n):
        print(self.name)
        print(n)


if __name__ == '__main__':
    # 注意：构造方法中的参数，实质是传给init方法的参数的
    p1 = Person('yuting', 18)

    p1.run(100)

    # 通过对象使用对象属性
    print(p1.name, p1.age, p1.sex)

    p2 = Person('骆昊', 30)
    print(p2.sex, p2.name)

    """通过不同的方式创建对象"""
    # 创建对象的时候不给属性赋值
    p3 = Person()

    p4 = Person('王海飞')

    Person(sex='男', name1='yuting')

