"""
1、声明一个函数就是在声明一个变量。函数名可以当成变量使用
可以打印，可以赋值，可以查看类型，可以作为函数的参数。
"""
#  函数名func1可以当成变量使用
def func1(a):
    print(a)


print(func1, type(func1))

#  将函数func1赋给变量a，这个时候a就是一个函数
a = func1
a('sad')

# 将函数func1作为列表的元素
functions = [func1, func1(10)]
functions[0]('sdsasdczxz')

# 1、将函数作为参数
# def my_sum(*numbers):
#     sum1 = 0
#     for item in numbers:
#         sum1 += item
#     return sum1

def my_mul(*numbers):
    sum1 = 1
    for item in numbers:
        sum1 *= item
    return sum1

def operation(method, x, y):
    return method(x, y)


result = operation(my_mul, 10, 31)
print(result)

"""
Python中三目运算符
值1 if 表达式 else 值2 --->判断表达式是否为true,为True整个表达式
的结果值为1，否则值为2
"""
# 判断10是否大于20
result3 = operation(lambda x, y: x > y, 19, 31)

# 找出两个数中的最大值
result4 = operation(lambda x, y: x if x > y else y, 32, 432)

print(result3, result4)
print('======')
"""3、将函数作为函数的返回值"""
#  写一个函数有个参数，要求传入一个运算符号(+ - * < >),返回符号对应的功能

def get_method(func):
    if func == '+':
        return lambda x, y: x + y
    if func == '>':
        return lambda x, y: x > y


result5 = get_method('+')(32, 45)
print(result5)

sun = []
def sss():
    for x in range(5):
        sun.append(lambda y: y*x)
sss()
print(sun[2](2))
print(sun[4](2))