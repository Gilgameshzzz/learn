# Filename  : 04-getter和setter.py
# Date  : 2018/8/1

"""
属性假的私有化：声明对象属性的时候，在属性名前面加一个'_',来告诉别人这个属性不可以直接使用。
要通过getter和setter来获取属性的值和修改属性的值

1、getter：获取属性的值
@property
def 属性名（去掉下划线）（self）
    return 返回值(_属性名?)
如果在获取对象的某个属性前需要再干点儿别的事情，就给属性添加setter


2、setter:修改属性的值
一个属性必须要有getter，才能添加setter

@属性名(去掉下划线).setter
def 属性名去掉下划线（self,变量名）：
    给带下划线的属性赋值

如果在给对象的某个属性赋值前需要再干点儿别的事情，就给属性添加setter
"""
class Student:
    """学生类"""
    def __init__(self):
        # 声明属性的时候前面加一个'_'是为了告诉别人这个属性不能直接使用
        self._name = ''
        self._score = 0
        self._age = 0

    #  给属性_name添加getter
    @property
    def name(self):
        return self._name

    # 给属性_name添加setter
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


if __name__ == '__main__':
    stu1 = Student()
    stu1.score = 98
    print(stu1.score)

