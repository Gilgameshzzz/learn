"""__author__ = 余婷"""

name = 10
print(name)


def func_other():
    global abc
    abc = 100
    print('~~~~')

# 打印当前模块的名字
print(__name__)