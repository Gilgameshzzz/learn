"""__author__ = 余婷"""

"""
创建一个名为User 的类，其中包含属性firstname 和lastname ，
还有用户简介通常会存储的其他几个属性。在类User 中定义一个名 为describeuser() 的方法，
它打印用户信息摘要;再定义一个名为greetuser() 的方法，它向用户发出个性化的问候。

管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承User类。
添加一个名为privileges 的属性，
用于存储一个由字符串(如"can add post"、"can delete post"、"can ban user"等)组成的列表。
编写一个名为sho
"""

import re

if __name__ == '__main__':
    print(re.fullmatch(r'a*[^0]\d*', 'a0123'))  # re.fullmatch(r'[+]?[^0]\d*', '+0123')