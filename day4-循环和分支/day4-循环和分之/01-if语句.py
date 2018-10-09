
"""
1.if
if 条件语句:
	代码块

其他语句

执行过程:先判断条件语句是否为True,如果是True就执行代码块，执行完代码块再执行其他语句。
		如果是False,直接执行其他语句


2.if--else
if 条件语句:
	代码块1
else:
	代码块2

其他语句  


执行过程：先判断条件语句是否为True,如果为True就执行代码块1，执行完代码块1再执行其他语句。
		如果是False,执行代码块2，执行完代码块2，再执行其他语句


3.if-elif-elif-...-else
if 条件语句1:
	代码块1
elif 条件语句2:
	代码块2
else:
	代码块3

其他语句


执行过程: 先判断条件语句1是否为True,如果为True就执行代码块1，执行完代码块1再执行其他语句。
		如果条件语句1是False,就判断条件语句2是否为True:
		如果条件语句2为True就执行代码块2，执行完代码块2再执行其他语句
		如果条件语句2为False就执行代码块3，执行完代码块3再执行其他语句

"""
# 给一个学生的成绩，判断成绩是优秀(90-100)、良好(70-89)、及格(60-69)、不及格(0-59)
score  = -40
if 90<=score<=100:
	print('优秀')

elif 70<=score<90:
	print('良好')

elif 60<=score<70:
	print('及格')

elif 0<=score<60:
	print('不及格')
else:
	print('成绩有误!!')

print('======')




# 4.if语句可以嵌套使用
"""
if 条件语句1:
	if 条件语句2:
		执行语句块2
	else:
		执行语句块3
else:
	执行语句块4

"""

# 练习:给一个数字(整数)，如果是偶数就打印‘xxx是偶数’，是偶数并且还能被4整除就打印‘xxx是4的倍数’，否则打印‘xxx是奇数’
"""
是偶数 ---> 打印‘xxx是偶数’--->如果还能被4整除，打印‘xxx是4的倍数‘
是奇数 ---> 打印’xxx是奇数‘
"""
numer = 12
if numer%2 == 0:
	print('%d是偶数' % (numer))

	if numer % 4 == 0:
		print('%d是4的倍数' % (numer))
else:
	print('%d是奇数' % (numer))



# if numer%2:
# 	print('奇数')
# else:
# 	print('偶数')
if isinstance(numer, int):
	print('是整数')
	if numer % 2:
		print('奇数')
	else:
		print('偶数')
		if not (numer % 4):
			print('是4的倍数')

print('=====')




# 5.判断数据的类型
# isinstance(值,类型名) --> 判断指定的值是否是指定的类型，如果是结果是True，否则结果是False
print(isinstance(10, int))  # 判断10是否是int类型
print(isinstance(12.0, int))











