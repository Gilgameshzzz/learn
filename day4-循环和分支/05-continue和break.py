"""
continue和break两个关键字，都是作用于循环当中，用来结束循环的。
continue:关键字，在循环体中遇到continue，就结束当次循环，直接进入下次循环的判断
如果是for循环，就让变量去取下一个值，如果是while循环就判断while后边的条件语句是否为true

"""
for x in range(10):
	print(x)
	continue   #不执行continue后面的语句，直接让x取下一个值
	print('---')


for x in range(10):
	if x%2:
		continue
	print(x)

"""
break:关键字，在循环体中遇到break,就直接结束整个循环。直接执行循环后面其他的语句
"""	

for x in range(10):
	print(x)
	break
	print('===')
print('!!!!')


# 使用break结束死循环
# num= 1
# while True:
# 	if num>100:
# 		break
# 	print(num)
# 	num+=1


# 练习：找出100-1000以内第一个能被3和17同时整除的数
for x in range(100,1001):
	if x%3 ==0  and x%17 ==0:
		print(x)
		# 找到第一个就不用再往下找了
		break


