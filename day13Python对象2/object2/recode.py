"""__author__ = 余婷"""
"""
1.生成式和生成器
(i for i in range(10))
def func():
    for i in range(10):
        yield i

(i+100 for i in range(10))
(i for i in range(10) if i%2==0)  


2.面向对象
类和对象：
类：拥有相同属性和功能的对象的集合（抽象的）
对象：类的实例（具体的）

类的声明：
class 类名(父类):
    属性
    方法

创建对象：
对象名 = 类名()

属性：
对象的属性：通过对象来使用；声明init方法，self.属性名 = 值
类的字段：通过类来使用；类里面函数的外面，属性名=值
属性的增删改查

init方法：
a.用来初始化对象的属性
b.通过类创建对象的时候，系统自动调用init方法。(创建对象的时候要保证init中每个参数都要有值)

方法：
对象方法：自带一个self参数；通过对象来调用
类方法：@classmethod,自带一个cls参数；通过类来调用
静态方法：@staticmethod;通过类来调用

"""

if __name__ == '__main__':
    pass