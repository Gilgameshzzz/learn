"""
匿名函数本质还是函数，以另外一种简单的方式来声明

匿名函数的声明：
函数名 = lambda 参数列表：返回值 --->结果是一个函数变量
lambda :声明匿名函数的关键字
"""


#  写一个函数计算两个数的和

def sum1(x, y):
    return x + y


# 匿名函数
sum2 = lambda x, y: x + y

print(sum1(10, 23))
print(sum2(12, 32))
