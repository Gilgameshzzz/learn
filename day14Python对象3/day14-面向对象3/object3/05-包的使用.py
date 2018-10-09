"""__author__ = 余婷"""
"""
封装：
对一个功能的封装 --> 用函数
对多个功能的封装 --> 模块和类
对多个数据进行封装 --> 类、字典  
对多个类进行封装  ---> 模块
对多个模块进行封装 ---> 包(文件夹)

"""
# 导入某个包中的某个模块
from package1 import my_math
# 导入某个包的某个模块中的某个函数和类
from package1.my_math import sum,Math

if __name__ == '__main__':
    # sum()
    # Math.sum()
    #
    # my_math.sum()
    # print(my_math.Math.pi)
    pass


