"""
1、什么是递归
递归函数：在函数的函数体中，调用函数本身
理论上，循环能做的事情，递归函数也能做

对递归的要求：能不用就不用
函数调用的过程是一个压栈的过程（每调用一次函数，系统都要
为其分配内存空间，用来存储函数中声明变量和参数等，
这个内存在函数调用结束后会自动销毁）

2、怎么写一个递归函数
a、找临界值（跳出循环 -->return）
b、找关系： 假设当前函数对应的功能已经实现，找到f(n)和f(n-1)的关系
c、使用f(n-1)与前面找到的关系去实现f(n)的功能

"""
#  求1+2+3+4+...+N
#  递归函数
def nums(n):
    # 1、找到临界值
    if n == 1:
        return 1
    #  2、找nums(n)和nums(n-1)的关系：
    """
    nums(n): 1+2+3+...+n-1+n
    nums(n-1):1+2+3+...+n-1
    关系：nums(n) = nums(n-1)+n
    """
# 3、使用nums(n-1)去实现nums(n)的功能
    return nums(n-1)+n


def sum2(n):
    if n == 1 or n == 2:
        return 1
    return sum2(n-1) + sum2(n-2)


print(sum2(5))


# 用递归求2*4*6...*n(n是偶数)
def nums(n):
    # 找临界值
    if n == 2:
        return 2
    # 找关系 “f(x) = f(x-2)*2 ”
    return nums(n-2)*n


print(nums(10))


def my_print(n):
    print('*'*n)
    if n == 1:
        return
    return my_print(n-1)


my_print(4)

def print_star(n):
    if n == 1:
        print('*')
        return
    print_star(n-1)
    print('*'*n)


print_star(5)