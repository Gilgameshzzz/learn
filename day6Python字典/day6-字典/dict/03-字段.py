"""__author__ = 余婷"""
"""
字典也是一种容器类型的数据类型(序列),存的数据是以键值对的形式出现的，字典中的元素全部都是键值对
字典是可变的(可是增删改)，但是是无序的(不能使用下标)
键是唯一的

键值对: 键:值（key:value）; 键值对中key是形式，值才是真正要存的内容
键：理论上可以是任何不可变的数据类型,但是实际开发的时候一般使用字符串作为key
值：可以是任意数据类型数据

"""

# 1.声明一个字典
"""a.创建一个字典变量"""
dict1 = {}  # 创建一个空的字典
print(type(dict1))

dict2 = {'a': 1, 'b': 'abc', 10: [1, 2, 3], ('a', 'b'): 'abc'}
print(dict2)

dict2 = {'a': 1, 'b': 'abc', 'a': 100}
print(dict2)

"""b.将其他数据类型转换成字典"""
dict3 = dict([(1, 2), (2, 3)])  # 了解
print(dict3)

# 2.字典的增删改查

"""a.查：获取字典的元素的值
字典获取元素的值是通过key来获取的
字典[key]
"""
person = {'name': '路飞', 'age': 17, 'face': 90}
print(person['name'], person['face'])
# print(person['aaa'])  # 如果key不存在，会报KeyError

"""
字典.get(key)
"""
print(person.get('name'))
print(person.get('aaa'))  # 如果key不存在，返回None

"""
注意：如果key值确定存在，使用[]语法去获取值。不确定key值是否存在才使用get方法去获取值
"""

"""b.增加元素\修改元素
通过key获取字典元素，然后赋值。当key本身就存在的时候，就是修改元素的值；不存在的时候就是给字典添加键值对
"""
person['height'] = 1.8
print(person)

person['age'] = 18
print(person)

"""c.删除: 删除的是键值对
del 字典[key]   ---- 注意：key如果不存在会报错
"""
del person['face']
print(person)

"""
字典.pop(key)  --- 会返回被删除的键值对对应的值
"""
age = person.pop('age')
print(person, age)

# 3.相关的数组属性（了解）
"""
字典.keys():获取字典所有的key，返回值的类型是dict_keys,但是可以把它当成列表来使用
字典.values():获取字典所有的值(value)
字典.items(): 将字典中所有的键值对转换成一个一个的元祖，key作为元祖的第一个元素，value作为元祖的第二个元素
"""
student_dict = {'name': '张三', 'study_id': "py1805001", 'scores': {'english': 60, 'math': 100}}
keys = student_dict.keys()
print(keys, type(keys))
# 遍历获取每个key
for key in keys:
    print(key)

print(student_dict.values())

print(student_dict.items())

# 4.遍历字典
# a.直接遍历字典获取到的是所有的key(推荐使用)
for key in student_dict:
    print(key, student_dict[key])

# b.遍历直接获取到key和value(不推荐使用)
for key, value in student_dict.items():
    print(key, value)

for value in student_dict.values():
    print(value)

# 5.列表中有字典、字典中有字典、字典中有列表
"""
声明一个变量，作用是用来存储一个班级的学生的信息。其中学生的信息包括姓名、性别、年龄、电话
至少存三个学生信息
"""
class1 = [
    {'name': '张三', 'age': 23, 'sex': '男', 'tel': '15300022777'},
    {'name': '李四', 'age': 25, 'sex': '女', 'tel': '12779922'},
    {'name': '王二麻子', 'age': 20, 'sex': '男', 'tel': '12553'}
]

class1 = {
    'name': 'py1805',
    'address': '19-1',
    'students':[
        {'name': '张三', 'age': 18},
        {'name': '李四', 'age': 28},
        {'name': '王五', 'age': 20},
    ]
}


# 6.其他操作
"""1.fromkeys()
dict.fromkeys(序列, value)：创建一个新的字典，序列中的元素作为key,value作为值
"""
# new_dict = dict.fromkeys('abc', '100')
# new_dict = dict.fromkeys(range(10), '100')
new_dict = dict.fromkeys(['abc', 'dcc', '123'], '100')
print(new_dict)

"""2.in
key in 字典: 判断字典中是否存在指定的key
"""
dog_dict = {'color': 'white', 'age': 3,  'type': '土狗'}
print('color' in dog_dict)  # 判断的是键是否存在
print('white' in dog_dict)

"""3.update
字典1.update(字典2): 使用字典2的键值对去更新字典1中的键值对。如果字典2中对应键值对在字典1中不存在，就添加。存在就更新
"""
dict1 = {'1': 'a', '2': 'b'}
dict1.update({'1': 'aaa', '3': 'bbb'})
print(dict1)










