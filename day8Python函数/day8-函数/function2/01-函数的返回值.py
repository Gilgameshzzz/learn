"""__author__ = 余婷"""
"""
1.函数的返回值:
    a.就是函数返回给调用者值
    b.就是return关键字后面的表达式的值
    c.就是函数调用表达式的值
    
python中每个函数都是有返回值的，返回值就是return后面的值。如果函数中没有return，那么函数的返回值就是None

***函数的调用：
    a.先回到函数调用的位置
    b.用实参给形参赋值(传参)
    c.执行函数体
    d.执行完函数体，将返回值返回给函数调用表达式
    c.回到函数调用的位置
***函数的函数体只有在调用后才会执行


2. return关键字
    a. 将return后面的值，返回给函数调用表达式
    b. 结束函数

3.函数调用表达式：
    python中每个函数调用表达式的都是有值

"""


def func1():
    print('aaaa')


a = func1()     # 函数调用表达式
print(a, func1())


def my_sum(x, y):
    # x = 10, y=20
    print('bbb')
    return x + y  # return 30


num = my_sum(1, 3)
print(my_sum(10, 20))


# 练习：写一个函数，判断指定的年龄是否属于成年人（返回结果）
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False


if is_adult(10):
    print('可以进网吧')
else:
    print('未成年人禁止进入')

person = {'name': '余婷', 'is_adult': is_adult(17)}
print(person)


"""
3.函数的结束:
    a. 函数体执行完
    b. 遇到return
"""
def func2():
    print('123')
    return 10
    print('321')

print(func2())

"""
写一个函数，下载指定地址对应的数据
def download(url):
    判断有没有网
    if 没有网:
        return None  
        
    写网络请求
    请求数据
    保存数据
"""


# 练习：写一个函数，求1+2+3+...+N，和不能大于10000
def my_sum2():
    sum1 = 0
    number = 1
    while True:
        if sum1 + number >= 10000:
            return sum1, number-1
            # python中函数可以有多个返回值，在return后面返回多个值，每个值之间用逗号隔开。返回值是一个元祖
        sum1 += number
        number += 1


print(my_sum2())