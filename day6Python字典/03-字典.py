# 字典也是一种容器类型数据类型（序列），存的数据是以键值对的形式出现的，
# 字典是可变的（可以增删改），但是是无序的（不能使用下标）
# 字典中的元素全是键值对
# 键值对：键：值 （key:value）;键值对中key是形式，值才是真正要存的内容
# 键理论上是可以任何不可变的数据类，但是实际开发中一般使用字符串作为key
# 值：可以是任意数据类型的数据


# 1、声明一个字典
dict1 = {}  # 创建一个空的字典
print(type(dict1))
dict2 = {'a': 22, 'b': 'a31', ('a', 'b'): 1, 10: [1.3, 4, 5]}
print(dict2)
# a、其他类型数据转换成字典
dict3 = dict([('a', 12), (323, 'da')])
print(dict3)
# b、字典的键是惟一的，如果键有多个，后面的键会覆盖前面的

# 2、字典的增删改查
"""
a、查：获取字典的元素的值
字典获取元素的值是通过key来获取的
字典[key]
"""
person = {'name': 'luck', 'age': 13, 'height': 133}
print(person['name'], person['age'])
# 如果key值不存在，会报KeyError

# 字典.get(key)
print(person.get('name'))
print(person.get('aasda'))  # 如果key不存在，会返回none
# 注意：如果key确定存在，使用[]去获取，不确定key是否存在才使用get方法去获取


# b、增加元素、修改元素
# 通过key获取字典元素，然后赋值。当key存在的时候，就是修改元素的值，
# 如果key不存在的时候，就是给字典添加键值对
person['weight'] = 100
print(person)

person['age'] = 22
print(person)


# c、删除 :删除的是键值对
# del 字典[key]  ---key不存在会报错，报的还是KeyError
# 字典.pop(key) ---会返回删除的键值对对应的值

# 3、相关的数组属性
"""
字典.keys(): 获取字典所有的key,返回值得类型是dict_key,但可以把它当做列表使用
字典.values():获取字典所有的值(value)
字典.items():将字典中所有的键值对转换成一个一个的元组，key作为元组第一个元素，value作为元组第二个元素
"""
student_dict = {'names': '张三', 'student_id': 'Py1805002', 'scores': {'english': 32, 'math': 98}}
keys = student_dict.keys()
print(keys, type(keys))



# 4、遍历字典
# a、直接遍历字典获取到的是所有的key
for key in student_dict:
    print(key, student_dict[key])

# b、遍历直接获取key和value(不推荐使用)
for key, value in student_dict.items():
    print(key, value)


# 5、列表中有字典和字典中有字典，以及字典中有列表
# 声明一个变量，作用是用来存储一个班级的学生的信息，其中学生的信息，包括姓名，年龄，性别，电话
# 至少存三个学生信息

students = {'names': ['张三', '李四', '王五'], 'ages': [18, 19, 20], 'sex': ['fmale', 'male', 'famale'] }

# 6、其他操作
"""1、fromkeys()
dict.fromkeys(序列，value)：创建一个新的字典，序列中的元素作为key,value作为值
"""
dict4 = dict.fromkeys('abc', '1000')
print(dict4)

"""2、in 
key in 字典：判断字典中是否存在指定的key
"""

"""3、update
字典1.update(字典2)：使用字典2的键值对去更新字典1中的键值对。如果字典2中对应键值对在字典1中不存在，就添加，存在就更新。

"""
dict1 = {'1': 'a', '2': 'b'}
dict1.update({'1': 'aaa', '3': 'sdsa'})
print(dict1)