"""__author__ = 余婷"""

# 1.写一个函数将一个指定的列表中的元素逆序(例如[1, 2, 3] -> [3, 2, 1])(注意：不要使用列表自带的逆序函数)
"""
[1, 2, 3]

"""


def reverse_list(list1):
    for index in range(len(list1)):
        # 取出对应的元素
        item = list1.pop(index)
        # 插入到最前面
        list1.insert(0, item)


old_list = [1, 2, 3]
reverse_list(old_list)
print(old_list)


# 2.写一个函数，提取出字符串中所有奇数位上的字符
def get_char(str1):
    # 声明一个空串用来保存提取出来的字符
    new_str = str1[0::2]
    return new_str


print(get_char('1name'))

# 3.写一个匿名函数，判断指定的年是否是闰年
"""
不能被100整除要能被4整除。能被100整除的要能被400整除
"""

is_leap_year = lambda year: (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

print('aaa',is_leap_year(2013))


# 4.使用递归打印：
def my_print(n, m=0):
    if n == 0:
        return None  # return 和 return None效果是一样的

    my_print(n-1, m+1)
    print(' '*m, end='')
    print('@'*(2*n-1))


my_print(4)


# 6.写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。
"""1,1,2,3,5,8,13,21...."""
def get_number(n):
    if n == 1 or n == 2:
        return 1

    return get_number(n-1) + get_number(n-2)


print(get_number(10))


# 7.写一个函数，获取列表中的成绩的平均值，和最高分
"""
sum(): 系统内置函数，求一个数字序列的和
max(): 系统内置函数，求一个序列中元素的最大值
"""


def get_score(scores):
    sum1 = 0
    return sum(scores)/len(scores), max(scores)


ave, max1 = get_score([1, 23, 50, 12])
print(ave, max1)

# 8.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新的列表返回给调用者
print(get_char([1, 2, 3, 4, 5]))

list1 = [[1,2,3,4],[5,6,7],[7,8,9]]
print(list1[0][1])