# 需要重复执行某个过程，就可以使用循环。
# Python中的循环有For循环和while循环

#1、for循环：
"""
for 变量名 in  序列：
	循环体

for: 关键字
变量名：和声明变量时的变量名要求是一样的，功能是存储值
in ：关键字 ，在。。。里的意思
序列：容器类型的数据。字符串、列表、字典、元组、集合等
循环体：需要重复执行的代码块

执行过程：使用变量去序列中取数据，一个一个的取，取完为止，每取一个值，执行一次体。

""" 
for char in 'abc123':
	print(char)

# 2、range函数
"""
xrange是Python2.x中的函数，在Python3.x使用range函数代替了

range 功能是产生指定范围的数字序列。一般用在for循环中，控制循环次数。或者产生索引值。

range（n）:产生 0 ~ n-1的整数序列,n为负数，不产生整数序列
range (m,n):产生 m~n-1的整数序列,m<n才能产生整数序列
range(m,n,step):从m开始，每次加step产生下一个数字，直到n前面那一个为止,step为负数也不产生整数序列
"""
for x in range(-5,0,2):
	print(x)
print('---分割线---')
for x in range(0,10,3):
	print(x)
print('---分割线---')

num1=0
for num in range(1,101):
	num1+=num
print(num1)


# 练习只用一个循环计算1*2*3*。。*10
num2 =1;num3=1 
for x in range(1,11):
	num2 *=x
	if x%2 == 0:
		num3 *=x	
print(num2)
print(num3)

# 练习2：有一个字符串'abcdef',依次取出字符串中偶数位（下标值位偶数）的字符
sum=-1
for x in 'abcdef':
	sum+=1
	if sum%2 ==0:
		print(x)

print('---')
str1='abcdef'
for index in range(0,len(str1),2):
	print(str1[index])







