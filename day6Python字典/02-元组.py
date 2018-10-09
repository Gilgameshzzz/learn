# 1.什么是元组 元组就是不可变得列表，列表中除了可变的操作，其他的操作都适用于元组
"""
元组值：
a、使用（）将元素包含起来，多个元素用逗号隔开.比如:(1,2,'22cc')
b、元素的类型可以是任何类型

2、改、增、删相关操作不能作用于元组。查可以
"""
colors = ('red', 'green', 'yellow', 'blue')
# 1、查（和列表的查一模一样）
print(colors[0])
print(colors[0:2])
print(colors[2:0:-1])

# 2、len 可以
# 3、in ， not in可以
# 4、+和* 可以（会生成新的元组，不会对原来的元组进行操作）
colors = ()
print(colors)
# 5、元组补充（列表也可以用）：
"""1、获取元组的元素"""
names = ('name1', 'name2', 'name3')
x, y, z = names   # 通过多个变量分别获取元组的元素(变量个数和元组个数相同)
print(x, y, z)
names = ('name1', 'name2', 'name3', 'name4')
a, *b, c = names  # 通过变量名前加*可以把变量变成列表，获取多个元素
print(a, b, c)

*d, e = names
print(d, e)
f, *g = names
print(f, g)