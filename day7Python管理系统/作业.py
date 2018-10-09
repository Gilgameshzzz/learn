# def funct1(nums):
#     """求从1加到nums的和"""
#     sum1 = 0
#     for num in range(1, nums+1):  # 使用循环遍历1到nums
#         sum1 += num
#     print(sum1)
#
# funct1(100)
#


# def max1(a, *numbers):
#     """求多个数中的最大值"""
#     num1 = a  # 定义第一个数
#     for num in numbers:
#         if num > num1:  # 将a去比较后面的数
#             num1 = num
#     print(num1)
#
# max1(12, 34, 545, 43, 435, 6)


#
# def shai_zi(N):
#     """实现摇色子功能，并求所有色子的点数和"""
#     import random  # 导入随机数模块
#     sum2 = 0
#     for x in range(N):
#         num = random.randint(1, 6)
#         print(num) # 打印每个色子的点数
#         sum2 += num
#     print(sum2)
#
#
# shai_zi(3)

#
# def change_dict(dict1):
#     """交换字典中键和值"""
#     dict2 = {}
#     for x in dict1:
#         value = dict1[x]  # 提取输入字典的值
#         dict2[value] = x
#     print(dict2)
#
# change_dict({'a': 1, 'b': 2})

# def max1(num1, num2, num3):
#     """比较三个数的大小，并求出最大的值"""
#     max_num = num1  # 假定第一个数最大
#     if max_num < num2:
#         max_num = num2
#     if max_num < num3:
#         max_num = num3
#
#     print(max_num)
#
# max1(52, 24, 4)
#
# def print_letter(string):
#     """提取字符串的字母，并拼接打印"""
#     str1 = ''  # 命名一个空的字符串
#     for x in string:
#         if x.isalpha() == True:
#             str1 += x  # 拼接字符串
#
#     print(str1)
#
# print_letter('d2eweds@!we')

# def average_value(*number):
#     """求平均数"""
#     many = len(number)  # 用于计数
#     sum1 = sum(number)  # 求和，结果为str数据类型
#     print('平均数为%.3f ' % float(sum1/many))
#
# average_value(1, 3, 5, 7, 9, 10, 11)

# def factorial(nums=10):
#     """计算一个数的阶乘"""
#     sum1 = 1  # 用于装阶乘的结果
#     for nums in range(1, nums+1):
#         sum1 *= nums
#
#     print(sum1)
#
# factorial(5)
def operation(symbol, *numbers):
    """多功能计算函数"""
    list1 = list(numbers)
    if symbol == '+':  # 判断运算符号是否是加号
        sum1 = sum(list1)

    if symbol == '-':  # 判断运算符号是否是减号
        sum1 = list1.pop(0)
        for num in list1:
            sum1 -= num

    if symbol == '*':  # 判断运算符号是否是乘号
        sum1 = 1
        for num in list1:
            sum1 *= num

    if symbol == '/':  # 判断运算符号是否是除号
        sum1 = list1.pop(0)
        for num in list1:
            sum1 /= num

    print('运算符号为%s,结果为%.3f' % (symbol, float(sum1)))

operation('/', 1000, 5, 18, 20)
