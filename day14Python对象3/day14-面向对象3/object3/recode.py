"""__author__ = 余婷"""
"""
1.内置属性
__name__
__doc__

__dict__
注意：当我们通过__slots__去约束对象的属性后，对象__dict__属性不能使用。
     如果父类设置了__slots__，子类对象也不能使用__dict__  
 
__module__

__bases__  

2.私有化
命名的时候前面加'__', 不能类的外面去使用。不能被继承  

3.getter和setter(假的私有化) ----> 对象属性
a.在给对象的属性赋值前或者获取属性值前要干点儿别的事情，我们就给属性添加setter或getter
b. 命名属性的时候名字前加一个'_'

    @property
    def 属性名去掉下划线(self):
        返回一个值
    
    @属性名去掉下划线.setter
    def 属性名去掉下划线(self,value):
        给属性赋值
        

4.继承
继承就是让子类直接拥有父类的属性和方法

class 子类(父类):
    属性
    方法
    
能继承什么：
所有的属性和方法都可以继承(除了私有的)
__slots__的值不能继承
   

"""

class Person(object):
    __slots__ = ('name', 'age', '__dict__')
    def __init__(self):
        self.name = 'aaa'
        self.age = 10






if __name__ == '__main__':
    p1 = Person()
    print(p1.__dict__)

