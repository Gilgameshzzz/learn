"""
break和continue两个关键字，都是作用域循环当中，用来结束循环的。

continue: 关键字，在循环体中遇到continue，就结束当次循环，直接进入下次循环的判断
		(如果是for循环，就让变量去取下一个值。如果是while循环就去判断while后边的条件语句是否为True)
"""

for x in range(10):
	print(x)
	continue   # 不执行continue后面的语句，直接让x取下一个值
	print('====')

print('=====')


for x in range(10):
	if x % 2:
		continue
	print(x)  


"""
break：关键字，在循环体中遇到break,就直接结束整个循环。直接执行循环后边的其他语句
"""
for x in range(10):
	print(x)
	break
	print('======')
print('!!!!')


# 通过改变条件语句的值，来结束循环
numer = 1
while numer <= 100:
	print(numer)
	numer += 1


# 使用break结束死循环
numer = 1
while True:
	if numer > 100:
		break
	print('==:',numer)

	numer += 1


# 练习:找出100-1000以内第一个能够被3整除同时能够被17整除的数
for x in range(100,1001):
	if x%3==0 and x%17==0:
		print(x)
		# 找到第一个就不用再往下找了
		break



