"""__author__ = 余婷"""
# 增、删、改、查

# 1.修改列表元素
"""
通过下标获取元素，然后重新赋值： 列表名[下标] = 新的值

注意: 这儿的下标不能越界
"""
names = ['周星驰', '张家辉', '刘德华', ' 黄渤', '杨洋']
names[4] = '陈奕迅'
# names[-1]
print(names)

name = names[-1]
name = ''


# 2.列表的其他操作
"""
1.len(列表): 获取列表的长度(元素的个数)
2.列表1 + 列表2: 让列表1和列表2的元素组合在一起产生一个新的列表
3.列表 * 数字：让列表中的元素重复N次，产生一个新的列表
"""
# print(len([1, 2, 3, 4, 5]))
print(len(names))

new_names = names + ['周杰伦', '王力宏']
print(new_names)

print([1,2]*3)

"""4.in, not in操作
元素 in 列表: 判断指定的元素是否在指定的列表中
"""
result = '高以翔' not in names
print(result)


# 3.获取列表中的最大的元素和最小元素
"""
max(列表)
min(列表)
"""
print(max([1, 34, 67, 8]))
print(max(['a', 'hj', 'uio', 'z']))
print(min([1, 45, 89, 0, -1, 8]))

# 获取一个数字列表中的最大值
numbers = [-1, -23, -56, -2, 445, -1]
max1 = numbers[0]
for item in numbers:
    if item > max1:
        max1 = item
print(max1)

# 4.其他方法
"""1.count：获取指定元素在列表中出现的次数"""
print(numbers.count(-1))

"""2.列表.extend(序列): 将序列中的每一个元素，添加到列表中"""
names.extend(['王祖贤'])
print(names)

"""3.列表.index(元素):获取指定元素在指定列表中的索引(如果元素有多个，取第一个)"""
print(names.index('张家辉'))

"""4.列表.reverse(): 反向列表中的元素(直接操作的原列表，不会产生新的列表)"""
numbers = [1, 22, 3, 4, 89]
numbers.reverse()
print(numbers)

"""5.列表.sort():对列表元素进行排序(默认是从小到大排序 - 升序)"""
numbers = [1, 42, 45, 6, 90]
numbers.sort()  # 升序
print(numbers)

numbers.sort(reverse=True)  # 降序
print(numbers)

"""6.列表.clear(): 清空列表中的元素"""
numbers.clear()
# numbers = []  # 效果同上
print(numbers)

"""***7.列表.copy(): 将列表中的元素全部拷贝一份创建一个新的列表"""
names = ['张三', '李四']
# new_names1 = names.copy()
new_names1 = names[:]
print(new_names1)

# 注意: 通过一个列表变量给另一个列表变量赋值的时候，赋的是地址；两个列表对元素进行操作的时候会相互影响。
# 想要避免这个问题就使用copy或者切片












