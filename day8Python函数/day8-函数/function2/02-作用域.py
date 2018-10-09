"""__author__ = 余婷"""
"""
作用域:一个变量可以使用的范围，就是这个变量的作用域（函数和类可以影响变量的作用域）

全局变量: 从声明开始，到文件结束都可以使用 
局部变量: 在函数(类)中声明的变量是局部变量。作用域是从声明开始到函数结束
"""
# 1.全局变量
a = 10  # 这是一个全局变量

print(a)


def func1():
    print(a)


for x in range(10):
    b = 100    # 这个变量是全局
    print(b)
    print(a)

print('===', b)

def func2():
    print(b)
func2()

# 2.局部变量
def func3():
    aaa = 200   # 局部变量，作用域是函数
    print(aaa)

func3()

# print(aaa)  # 报错: NameError: name 'aaa' is not defined

# 3.global和nonlocal
"""
global: 在函数中声明一个全局变量
格式:
global 变量名
变量名 = 值

"""

abc = 'abc'  # 全局变量
bcd = 'bcd'
def func4():
    abc = 'aaa'  # 局部变量，如果全局变量名和局部变量名相同，在函数中使用的是局部变量
    print(abc)

    global bcd   # 说明bcd是一个全局变量
    bcd = 200
    print(bcd)

func4()
print(abc)
print(bcd)

# 练习：声明一个变量，统计一个函数调用的次数
count = 0


def my_func():
    global count
    count += 1
    print('====')


my_func()
my_func()
print('0----')
a = 10
my_func()
print(count)

"""
nonlocal:在函数中声明函数的时候，才需要使用
"""
def func11():
    a_11 = 10
    print('外部:', a_11)

    # python中函数里面可以声明函数
    def func12():
        nonlocal a_11  # 使用nonlocal修饰后的变量还是局部变量
        a_11 = 100
        print('内部:', a_11)
        print('内部函数')

    func12()
    print('外部:', a_11)


func11()
# print(a_11)

