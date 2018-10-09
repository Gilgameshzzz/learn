# Filename  : recode.py
# Date  : 2018/8/10

"""
# 1
1、Python：脚本语言，不可以加密（胶水语言）
2、语句（一条语句后面不需要分号，如果一行写多条语句，语句之间加分号）、
注释（CTRl+/）、多行显示（\）、缩进（同一个缩进属于同一代码块）

# 2基本数据类型（python中所有的数据类型都是类）
整型（int）、浮点型（float）、布尔（bool）、复数（complex）、字符串（string）、
列表（list）、字典（dict）、元组（tuple）、集合（set)、字节（bytes）等。
类型名（值）--->可以将指定的值转换成指定的类型（通过指定的值创建指定类型的对象）
python 中的字面量分为两大类：值类型（给变量赋值的时候变量直接存值）--整型、浮点型、布尔、复数、字符串等
引用类型（给变量赋值的时候变量存的值是值在内存中的地址）。

不同的类型，在计算机中存储的内存大小不一样

type(值/变量)-->获取类型

# 3、变量(python是动态语言)
声明变量就是在内存中开辟空间存储数据

变量名 = 值（a = 10）
(其他语言：类型名 变量名 = 值 如：int a = 10)

# 4 运算符（+，-，*，/，%，//，**；>,<,>=,<=等）
某个类型的数据之所以可以支持某个运算符，是因为数据对应的类型中，实现相应的运算符重载方法

# 5、字符串（str）
'abc',"sd12 " (三个双引号或三个单引号括起来的字符，也是字符串，这种字符串叫多行字符串)

Unicode码：用16位对一个字符进行编码（一个字符是2个字节）
字符串获取字符（获取单个、获取部分）--->下标（0~~字节长度-1或-1~~-长度）、切片（下标1：下标2：步进）

转义字符：\
r/R：阻止转义

# 6、容器类型（列表、字典、集合、元组）
类型名
字面量的样式（[1,2],{'aq':33},{1,3,'w'},('1dw',)）
特点：是否有序，是否可变
获取单个元素：列表->下标  字典->key
元素的增删改查
容器相关方法（列表和字典）

# 7、if结构、循环结构
结构和执行过程
break 和 continue

# 8、函数（函数体只有在调用的时候才会执行）
函数的声明结构
怎么声明函数：
    看实现函数功能是否需要其他的数据，需要就添加参数
    看实现完函数的功能，会不会产生新的数据，如果产生就将这个数据返回

函数的调用（位置参数和关键字参数）
    a、回到函数声明的位置
    b、用实参给形参赋值（传参：保证每个参数都有值）
    c、执行函数体
    d、返回返回值
    e、回到函数调用的位置（函数调用表达式就是返回值）

返回值和return

匿名函数：lambda 参数列表：返回值

声明一个函数，实质就是声明一个类型是function变量

# 类和对象（封装、继承和多态）
类怎么声明
类的内容：属性（类的字段和对象的属性）和方法（对象方法、类方法、静态方法）

类的继承、重写

# 正则表达式（记符号）
记re模块中的方法

# 文件操作
打开文件（打开方式：r,rb/br,w,wb,a）
读写操作：read(),write()
json文件 load，dump

# 异常捕获（try - except - finally）

# python3和python2的区别
"""
# import random
# if __name__ == '__main__':
#     list1 = list(range(50))
#     print(list1)
# while list1:
#     a = random.randint(list1)
#     print(a)
#     list1.remove(a)

a = ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint',
'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex',
'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec',
'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash',
'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list',
'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord',
'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr',
'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


import re


c  = re.findall(r'"(.*)"','"hello"  ,Jack said,   "yeah, hello ,nice to meet you."  ,lucefu said,"me too."')

print(c)

re_str= r'(\d+)'
re_str1 = r'(\d+?)'
e = re.findall(re_str,'22b3213c24121')
d = re.match(re_str1,'22b3213c24121')

print(e)
print('d',d,type(d))


# print(sum(int(a) for a in d))
# b= {'a':1,'b':2,'c':3};c = dict((k,y) for y,k in b.items());print(c)

a = {3:3}
print(a)
print(sum([9,9,334]))
