# 注意： 不管是添加元素还是删除元素，都会重新分配下标
# 删除列表元素
films = ['肖申克的救赎', '阿甘正传', '摔跤吧爸爸', '赌神', '英雄本色']
# 1、 del语句
"""
del可以删除任何数据

del 列表[下标]：删除列表中指定下标的元素
注意：下标不能越界
"""
del films[1]
print(films)

# 2、remove方法
"""
列表.remove(元素):删除列表中的指定元素(如果同一个元素有多个，只删除最前面的那一个元素)：

注意：如果要删除的元素不在列表中，会报错ValueError
"""
films.remove('摔跤吧爸爸')
print(films)

# 3、pop方法
"""
列表.pop()： 将列表中的最后一个元素取出来
列表.pop（下标）：将列表中指定下标的元素取出来
注意：下标不能越界
"""
print(films)
film = films.pop()
print(films, film)

# scores = [23,45,54,75,98,54,78],删除所有小于60
scores = [23, 45, 54, 75, 98, 54, 78, 100, 32]
scores1 = scores[:]
for i in scores1:
    if i < 60:
        scores.remove(i)
print(scores)
