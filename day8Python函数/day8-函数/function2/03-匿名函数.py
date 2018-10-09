"""__author__ = 余婷"""
"""
匿名函数：本质函数函数，以另外一种简单的方式来声明

匿名函数的声明：
函数名 = lambda 参数列表:返回值  --->  结果是一个函数变量

lambda：声明匿名函数的关键字
"""
# 写一个函数计算两个数的和
def my_sum1(x, y):
    return x+y

print(my_sum1(10, 20))

# 匿名函数
my_sum2 = lambda x, y=10: x+y

print(my_sum2(10, 20))

#
funcs = []
for i in range(5):
    funcs.append(lambda x: x*i)

"""
i = (0, 1, 2, 3, 4)
i = 0
[lambda x:x*i,lambda x:x*i,lambda x:x*i,lambda x:x*i,lambda x:x*i]
"""

# 4? 8?
# 6? 10?
# lambda 2:2*4
print(funcs[2](2))
print(funcs[4](2))
print(i)