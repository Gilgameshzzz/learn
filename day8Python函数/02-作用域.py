"""
作用域：一个变量可以使用的范围，就是这个变量的作用域
（函数和类可以影响变量的作用域）
Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
全部变量：从声明开始，到文件结束都可以使用
局部变量：在函数或是类中声明的变量是局部变量。作用域是从声明开始到函数结束
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
"""
# 1、全局变量
a = 10  # 这是一个全局变量
print(a)


def func1():
    print(a)


for x in range(3):
    print(a)


for x in range(2):
    b = 100   # 这也是一个全局变量
    print(b)
    print(a)

print('===', b)


# 2、局部变量
def func3():
    aaa = 100  # 这是一个局部变量
    print(aaa)


func3()
# print(aaa) 会报错 NameError： name: 'aaa' is not defined

# 3、global 和 nonlocal
"""
global: 在函数中声明一个全局变量
格式：
global 变量名
变量名 = 值

"""
abc = 'abc'  # 全局变量
bcd = 'bcd'


def func4():
    abc = 'aaa'  # 局部变量，如果全局变量和局部变量名相同，在函数中使用的是局部变量
    print(abc)
    global bcd  # 说明bcd是一个全局变量
    bcd = 200
    print(bcd)


func4()
print(abc)
print(bcd)

# 练习：声明一个变量，统计一个函数调用的次数
count = 0

def cunt1():
    global count
    count += 1
    print('===')


cunt1()
cunt1()
print('dds')
a = 2
cunt1()
print(count)

"""
nonlocal  在函数中声明函数的时候，才需要使用
"""
def func11():
    a_11 = 10
    print('外部：', a_11)

    # Python中函数里面可以声明函数
    def func12():
        nonlocal a_11
        a_11 = 100
        print('内部：', a_11)
        print('内部函数')

    func12()
    print('外部：', a_11)


func11()