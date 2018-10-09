"""
1、函数返回值：
    a、就是函数返回给调用者的值
    b、就是return关键字后面的表达式的值
    c、就是函数调用表达式的值

python中每个函数都是有返回值的，返回值就是return后面的值，
若没有return，函数返回值就是None。

>>函数的调用：
    a、先回到函数调用的位置
    b、用实参给形参赋值（传参）
    c、执行函数体
    d、执行完函数体，将返回值返回给函数调用表达式
    e、回到函数调用的位置
>>函数的函数体只有在调用后才会调用执行

2、return关键字
    a、将return后面的值，返回给函数调用表达式
    b、结束函数

3、函数调用表达式：
    python每个函数调用表达式的都是有值

"""


#  练习：写一个函数，判断指定的年龄是否属于成年人
def ages(num):
    if num >= 18:
        return '是成年人'
    else:
        return '不是成年人'


age = ages(34)
print(age)

"""
4、函数的结束：
    a、函数体执行完
    b、遇到return
"""


def func2():
    print('123')
    return 10
    print('321')


print(func2())


# 练习：写一个函数，求1+2+3+..和不能大于10000
def sum1():
    num = 0
    for x in range(10001):
        num += x
        if num > 10000:
            num -= x
            return num, x - 1  # Python函数中可以返回多个值，每个之间用逗号隔开，最后返回的是一个元组


s = sum1()
print(s)
