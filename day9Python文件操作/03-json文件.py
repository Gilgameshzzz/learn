"""
json文件（文本），就是文件后缀是.json的文件。内容必须是json的格式

json格式：
1、内容是字符串
2、最外层是字典，字典里面就必须是键值对
3、最外层也可以是数组（列表），数据里面的内容必须是数组数据

"""
# 1、json是Python中内置的一个模块，专门用来处理json数据的
import json

"""1、json文件的读操作"""
# 打开json文件
with open('./test.json', 'r', encoding='utf-8') as f:
    #  直接使用read去读，获取到的是字符串数据，包含json所有的内容（包括注释）
    """
    load(文件对象):获取指定json文件中的内容,返回值最外层的对应数据类型
    dict--->dict
    array--->list
    string -->str
    number --->int/float
    true/false-->True/False
    null --->none
    """

    content = json.load(f)
    print(content, type(content), content['name'])


# 2、json文件的写操作
with open('./new.json', 'w', encoding='utf-8') as f:
    # 写数据
    """
    dump(写的内容，文件对象)
    """
    w_content = 'abc'
    json.dump(w_content, f)

# 练习：输入学生的姓名和电话，保存到本地（要求再次启动的，再添加学生信息的时候，之间添加的信息还在）


# name = input('名字：')
# tel = input('电话：')
# student = {'name': name, 'tel': tel}
# old_data = []
# with open('./students.json', 'r', encoding='utf-8') as g:
#     old_data = json.load(f)
#     old_data.append(student)
#
# with open('./students.json', 'w', encoding='utf-8') as g:
#     json.dump(old_data, g)


"""3、json模块的其他操作
loads(字符串，编码方式)-->将指定的字符串(json字符串)，转化成json数据
将字符串转换成字典\将字符串转换成列表
"""
content1 = json.loads('"abcde"', encoding='utf-8')
print(content1, type(content1))

"""
dumps(对象)
dumps:将json对象转换成json字符串
字典/列表转换成json字符串
"""
content3 = json.dumps(['abcde', 1, True, [1, 2, 3]])
# content3 = '["abcde", 1, true, [1, 2, 3]]'
print(content3, type(content3))
