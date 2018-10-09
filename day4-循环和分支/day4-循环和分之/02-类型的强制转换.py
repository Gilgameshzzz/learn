# 数据类型转换: 类型名(被转换的数据)
# int  float  bool  str

# 1.其他的数据类型转换成整型:int()
"""
浮点型：只保留整数部分
布尔类型：True -> 1  False -> 0
字符串：去掉字符串的引号后，剩下的部分本身就是一个整型数据的字符串才能转换成整数。
"""
print(int(12.9))
print(int(False))
print(int('+12'))



# 2.其他的数据类型转换成浮点型: float()
"""
整型:在整数后面加一个'.0'
布尔类型: True -> 1.0   False -> 0.0
字符串：去掉字符串的引号后，剩下的部分本身就是一个整型或者浮点型数据的字符串才能转换成浮点型数据
"""
print(float(123))
print(float(False))
print(float('+100.23'))


# 3.其他类型的数据转换成布尔类型：bool()
"""
不管什么类型的数据都可以转换成布尔值

整数中，除了0会转换成False其他的都会转换成True

总结：所有为0为空的值都会转换成False,其他的值都是True

"""
print(bool({}))


if 0:
	print('====')
else:
	print('!!!')

# 判断一个字符串是否是空串(字符串长度是0)
# 空串就是:'',""
str1 = '12'

# 方法1
if str1 == '':
	print('空串')
else:
	print('不是空串')

# 方法2
if len(str1) == 0:
	print('空串')
else:
	print('不是空串')

# 方法3
if str1:
	print('不是空串')
else:
	print('空串')



# 判断一个数字是否是0
number = 10

# 方法1
if number == 0:
	print('是零')
else:
	print('非零')


# 方法2
if number:
	print('非零')
else:
	print('零')




# 4.其他类型的数据转换成字符串：str()
"""
不管什么类型的数都可以转换成字符串

其他数据转换成字符串的时候，就是直接在数据的外层加引号

"""
print(str(120))







