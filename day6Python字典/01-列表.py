# 增、删、改、查
# 1、修改列表元素
"""
通过下标获取元素，然后重新赋值：列表名[下标]=新的值
注意： 这儿的下标不能越界

"""
names = ['周星驰', '张家辉', '张学友', '洋洋']
names[-1] = '陈奕迅'
print(names)

# 2、列表的其他操作
"""
1、len():获取列表的长度（元素的个数）
2、列表1 + 列表2 ：让列表1和列表2的元素组合在一起，产生一个新的列表
3、列表 * 数字：让列表中的元素重复N次，产生一个新的列表
"""
print([1, 3] * 2)
"""
4、in， not in操作
元素 in 列表：判断指定的元素是否在指定的列表里
"""
result = 'sd' in names
print(result)

# 3、获取列表中的最大元素和最小元素
"""
max(列表)
min(列表)
"""
numbers = [1, 23, 43, 211, 7, 1]
max1 = numbers[0]
for x in numbers:
    if x > max1:
        max1 = x
print(max1)


# 4、其他方法
# 1、 count: 获取指定元素在列表中出现的方法
# 2、 extend: 格式： 列表名.extend(序列)：将序列中的每一个元素，添加到列表中
names.extend(['王祖贤'])
names.extend('王祖贤')
print(names)
# 3、列表.index(元素)：获取指定元素在指定列表中的索引(如果有多个元素，就取第一个)
# 4、列表.reverse():反向列表中的元素，对原来的列表进行操作
num = [1, 212, 3, 454, 23, 9, 23]
nnum = num.reverse()
print(num, nnum)

# 5、列表.sort():对列表元素进行排序（默认是从小到大排序）
num.sort()
print(num)
num.sort(reverse=True)
print(num)

# 6、列表.clear():清空列表中的元素
# num.clear()  相当于 num = []

# 7、列表.copy():将列表的元素全部拷贝一份创建新的列表
# 注意:通过一个列表变量给另一个列表变量赋值的时候,赋的是地址:两个列表对元素进行操作会相互影响
# 要想避免这个问题就使用copy,或[:]
