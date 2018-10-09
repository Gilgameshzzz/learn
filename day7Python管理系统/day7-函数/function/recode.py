"""__author__ = 余婷"""
"""
列表：[1, 3, 'a', '12bc']
元素 in  列表
+，* 

元祖：不可变，有序
(1, 'yu')
注意：当元祖的元素个数是一个的时候，需要在元素的后面加一个逗号，表示这个值是一个元祖

字典：{key:value, key1:value}
增删改查
del 字典[key]
字典.pop(key)
for key in 字典:
for key,value in 字典.items:

key in 字典 
字典.update(字典2)

集合：{1,'ss'},无序，可变，不会重复
增删查
集合.add(元素)
集合.update(集合)
集合.remove(元素)
集合.pop()
数学集合运算：1.包含(>=,<=) 2.并集(|)，交集(&),差集(-),补集(^)
"""
for x in [{'a':100}, {'a':1}]:
    print(x['a'])


a = (1, 2)
print(a, type(a))

b = (10,)
print(b, type(b))
