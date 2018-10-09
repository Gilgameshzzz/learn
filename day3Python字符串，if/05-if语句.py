# if语句
"""
结构：
1.
if 条件语句：
	条件语句结果为True执行的代码块
执行过程：先判断条件语句是否为true,如果为true，就执行if语句后：后面对应的一个缩进的所有代码
如果为false，就不执行冒号后面一个缩进后的代码块，直接执行后续的其他语句
条件语句：可以是任何有值得表达式，一般为布尔值

if：关键字

"""
# 练习：用一个变量保存时间（50米短跑），如果时间小于8秒，打印及格
import random
 
score = random.randint(0,9)
if score < 8:
	print('用时', score ,'及格')
"""
2.if条件语句：
    语句块1
  else：
    语句块2
 执行过程：先判断条件语句是否为True，如果为True就执行语句块1，否则执行语句块2

"""
score1 = random.randint(0,9)
if score1 < 8:
	print('用时', score1 ,'及格')
else:
	print('用时',score1,'不及格')

