# while循环
"""
while 条件语句:
	循环体

其他语句


while: 关键字
条件语句：结果是True,或者False
循环体: 重复执行的代码段

执行过程：判断条件语句是否为True,如果为True就执行循环体。
		执行完循环体，再判断条件语句是否为True,如果为True就再执行循环体....
		直到条件语句的值为False,循环结束，直接执行while循环后面的语句

注意：如果条件语句的结果一直都是True，就会造成死循环。所以在循环体要有让循环可以结束的操作



python中没有do-while循环
"""

# 死循环
# while True:
# 	print('aaa')

# 循环只执行一次
flag = True
while flag:
	print('aaa')
	flag = False


# 使用while循环计算1+2+3+...+100
number = 1  # 保存数字1-100
sum1 = 0  # 保存和
while number <= 100:
	print(number)
	sum1 += number

	# 每次循环让number值加1
	number += 1

print(sum1)


# 练习：计算2+4+6+...100
number = 2
sum2 = 0
while number <= 100:
	sum2 += number
	number += 2

print(sum2,number)








