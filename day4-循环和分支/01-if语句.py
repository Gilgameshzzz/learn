
"""
1.if
if 条件语句：
    代码块
其他语句

执行过程：先判断条件语句是否为True，如果是True就执行代码块，执行完代码块在执行其他语句。
      如果是False，就直接执行其他语句。

2.if--else
if条件语句：
   代码块1
else：
   代码块2
其他语句
执行过程：先判断条件语句是否为true,如果为true就执行代码块1，再执行其他其他语句。
如果是False，执行代码块2，再执行其他语句。

3.if-elif-...else
if 条件语句1：
  代码块1
elif 条件语句2
   代码块2
else：
    代码块3

其他语句

执行过程：先判断条件语句1是否为true,如果为true就执行代码块1，执行完后再执行其他语句
如果条件语句1是False，就判断条件语句2是否为true:
如果条件语句2为true就执行代码块2，执行完后再执行其他语句
如果条件语句2为False就执行代码块3，执行完后再执行其他语句
"""
import random

score = random.randint(0,101)
if 90<=score<=100:
	print(score,'优秀')
elif 70<=score<=89:
	print(score,'良好')
elif 60<=score<70:
	print(score,'及格')
elif 60>score>=0:
	print(score,'不及格')
else:
	print(score,'成绩输入有误')



# 4.if语句可以嵌套使用
"""
if 条件语句1：
    if条件语句2：
        执行语句块2
    else：
    	执行语句块3
else：
	执行语句块4
"""
#练习 ：给一个数字，如果是偶数就打印“xx是偶数”是偶数并且还能被4整除，就打印‘xx是4的倍数’，否则就打印"xx是奇数“

num1 = 32
if num1%2==0:
	if num1%4==0:
		print(str(num1)+'是4的倍数')#print('%d是偶数' % num1)
	else:
		print(str(num1)+'是偶数')
else:
	print(str(num1)+'是奇数')

# 5.判断数据的类型
# isinstance(值，类型名) -->判断指定的值是否是指定的类型，结果是就是True,不是就是False
print(isinstance(10,int))
