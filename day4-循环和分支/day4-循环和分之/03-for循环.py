# 需要重复执行某个过程，就可以使用循环。
# python中的循环有for循环和while


# 1.for循环：
"""
for 变量名 in 序列:
	循环体


for: 关键字
变量名: 和声明变量时的变量名要求是一样的，功能是存储值
in: 关键字，在。。。里的意思
序列: 容器类型的数据。字符串、列表、字典、元祖、集合等
循环体: 会重复执行的代码块

执行过程：使用变量去序列中取数据，一个一个的取，取完为止。每取一个值，执行依次循环体
"""

for char in 'abcd123':
	print(char)
	print('!')

print('=====')



# 打印20次‘abc’
# 2.range函数
"""
xrange是python2.x中的函数，在python3.x使用range函数代替了

range功能是产生指定范围的数字序列。一般用在for循环中，控制循环次数。或者产生索引值

range(n): 产生 0 ~ n-1的整数序列
range(m,n): 产生 m ~ n-1的整数序列
range(m,n,step):从m开始，每次加step产生下一个数字，直到n前面那一个为止
"""

# range(10):产生数字0，1，2，3，4，5，6，7，8，9
for x in range(10):
	print(x)

print('=======')

# range(10,20):产生数字：10~19
for x in range(10,20):
	print(x)

print('+++++++')

# range(0,10,2):产生数字：0，2，4，6，8
for x in range(0,10,2):
	print(x)



# 练习：计算1+2+3+...+100
sum1 = 0   # 声明一个变量来存和
for x in range(1,101):
	sum1 += x

print(sum1)

"""
sum1 = 0

x 在 （1-100）
x = 1  sum1 += 1 = 0+1
x = 2  sum1 += 2 = 1+2
x = 3  sum1 += 3 = 1+2+3
...
x = 100 sum1 += 100 = 1+2+3+..+99 + 100

"""

# 练习：只使用一个循环
# 计算1*2*3*..*10
# 计算2*4*6*...*10
mul1 = 1  # 声明一个变量来存乘积
mul2 = 1

# 遍历取出1-10中所有的数字
for x in range(1,11):
	mul1 *= x  # mul1 = mul1*x

	# 判断x是否是偶数
	if x % 2 == 0:
		mul2 *= x

print(mul1)
print(mul2)


# 练习2：有一个字符串‘abcdef’,依次取出字符串中偶数位(下标值是偶数)上的字符
# 0 ~ len-1
str1 = 'abcdef'

# 方法一：
# 循环取出字符串所有的偶数下标
# index = 0,2,4
for index in range(0,len(str1),2):
	print(str1[index])


# 方法二：
# 循环取出字符串中每个字符的下标
for index in range(0,len(str1)):
	# 判断下标是否是偶数
	if index % 2 == 0:
		print(str1[index])
	
print('======')

# 方法三：
index = 0
for char in str1:
	if index % 2 ==0:
		print(char)
	index += 1

"""
index = 0

char = (abcdef)
char = a   index = 0   print('a')  index = 1
char = b   index = 1   index = 2
char = c   index = 2   print('c')   index = 3
...

"""





