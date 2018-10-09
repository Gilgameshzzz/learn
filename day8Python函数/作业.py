# def ni_list(list1):
#     list2 = []
#     for item in list1[::-1]:
#         list2.append(item)
#     return list2

#
# print(ni_list([1, 2, 3]))

# def find_str(string):
#     str1 = ''
#     for item in string:
#         if item.isalpha():
#             str1 += item
#
#     return str1
#
# print(find_str('sdawe2133da!!'))

#
# def find_years(years):
#     if years % 100 == 0 and years % 400 == 0:
#         print('%s是闰年' % years)
#
#     elif years % 100 != 0 and years % 4 == 0:
#         print('%s是闰年' % years)
#     else:
#         print('%s不是闰年' % years)
#
#
# find_years(2019)
#
#
# year = lambda x: ('%s是闰年' % x) if x % 100 == 0 and x % 400 == 0 or x % 100 != 0 and x % 4 == 0 else ('%s不是闰年' % x)
#
# print(year(2020))
#

#
# def print_star(n, m=0):
#     s = '@' * (n * 2 - 1)
#     if n == 0:
#         return
#     print_star(n-1, m+1)
#     print(' ' * m, end='')
#     print(s)
#
#
# print_star(5)

# def check_list(list1):
#     list2 = []
#     if len(list1) >= 2:
#         list2.append(list1[0])
#         list2.append(list1[1])
#     return list2
#
# print(check_list([1, '3224d', '!!!!', 4]))


# def sum2(n=10):
#     if n == 1 or n == 2:
#         return 1
#     return sum2(n-1) + sum2(n-2)
#
#
# print(sum2())

#
# def get_score(scores):
#     sum1 = 0
#     return sum(scores)/len(scores), max(scores)
#
# print(get_score([13, 435, 54, 233]))