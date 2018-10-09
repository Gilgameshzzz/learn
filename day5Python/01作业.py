f1 = 1
f2 = 1
f3 = 0
month = 13  # int(input())
if month > 2:
    for i in range(3, month + 1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    print('第%d月有%d对兔子' % (month, f3))
else:
    print('第%d月有1对兔子' % month)

#  for循环中，如果for循环中的变量在循环体中不需要，这个变量名可以用"_"命名。

# 判断101 - 200 之间有多少个质数（素数），并输出所有的素数。
for num in range(101, 201):
    for num1 in range(2, num):
        if num % num1 == 0:
            # print(num, '不是素数')
            break  # 循环嵌套的时候，遇到break和continue结束的是包含break和continue最近的循环
    else:
        print(num, '是素数')

#  打印出所有的水仙花数,所谓水仙花数是指一个三位数，其各位数字立方和等于该数本身。
for num3 in range(100, 1000):  # 取出所有三位数
    ge_wei = num3 % 10
    shi_wei = num3 // 10 % 10
    bai_wei = num3 // 100
    if num3 == ge_wei ** 3 + shi_wei ** 3 + bai_wei ** 3:
        print('%d是水仙数' % num3)

# 有一分数序列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列的第20个分数（分子：上一个分数的分子加分母   分母: 上一个分数的分子
fen_zi = 2
fen_mu = 1
for x in range(1, 21):
    fen_zi, fen_mu = fen_zi + fen_mu, fen_zi
print('%d/%d' % (fen_zi, fen_mu))

# 给一个正整数，要求：1、求它是几位数 2.逆序打印出各位数字
number = int(input())
wei_shu = len(str(number))
print('%d是%s位' % (number, wei_shu))
print('逆序打印：%s' % str(number)[::-1])
