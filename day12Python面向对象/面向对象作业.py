# Filename  : 面向对象作业.py
# Date  : 2018/7/31

# class Pc:
#     def __init__(self, brand, color, size):
#         """电脑属性：品牌、颜色、内存大小"""
#         self.brand = brand
#         self.color = color
#         self.size = size
#     #  方法 打游戏
#     def play_game(self):
#         print('%s电脑被用来打游戏' % self.brand)
#     # 方法 写代码
#     def write_code(self):
#         print('%s电脑被用来写代码' % self.brand)
# #     方法 看视频
#     def watch_movies(self):
#         print('%s电脑被用来看电影' % self.brand)
#
#
#
# if __name__ == '__main__':
#     computer = Pc('Asus', 'red', '16G')
#     print(computer.brand, computer.color, computer.size)
#     computer.color = 'blue'
#     print(computer.color)
#     del computer.brand
#     computer.price = '$1000'
#     print(computer.price)
#
#     computer.__setattr__('brand', 'acer')
#     print(computer.brand)
#     print(getattr(computer, 'color'))
#     """delattr"""
#     """__getattr__"""
#     """__delattr__"""
#     """setattr"""

# class Dog:
#     def __init__(self, name='大黄', color='red', age=3):
#         self.name = name
#         self.color = color
#         self.age = age
#     def dog_way(self):
#         print('%s正在叫唤' % self.name)
#
# class Person:
#
#     def __init__(self, name='小明', age=24, had_dog=[]):
#         self.name = name
#         self.age = age
#         self.had_dog = had_dog
#     def person_way(self, name, color, age):
#         had_dog = Dog(name, color, age)
#         print('%s拥有条狗，叫%s然后他要去遛狗了' % (self.name, had_dog.name))
#
# if __name__ == '__main__':
#    man = Person('小明', 19)
#    man.person_way('小黄', 'blue', 4)
#
# class Rect:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def sum_area(self,):
#         print('面积为', self.length * self.width)
#     def sum_perimeter(self):
#         print('周长为', (self.length+self.width)*2)
#
#
#
# list1 = [x for x in range(10, 15)]
# list2 = [y for y in range(20, 25)]
# for i in list1:
#     for j in list2:
#         rect = Rect(i, j)
#         rect.sum_area()
#         rect.sum_perimeter()


class Student:
    def __init__(self, name, age, id_num):
        self.name = name
        self.age = age
        self.id_num = id_num
    def dadao(self):
        print('到！')
    def show_info(self):
        print('名字：%S  年龄：%d  学号：%d' % (self.name, self.age, self.id_num))

class Class:
    def __init__(self, student, class_name):
        self.student = student
        self.class_name = class_name

