"""__author__ = 余婷"""

"""
数据本地化: 将数据保存到本地文件中(文本、json、数据库)

json文件(文本)，就是文件后缀是.json的文件。内容必须是json格式的内容

json格式:
1.内容是字符串
2.最外层是字典，字典里面就必须是键值对
3.最外层是数组(列表),数组里面内容必须是数组数组


"""

# json是python中内置的一个模块，专门用来处理json数据的
import json

if __name__ == '__main__':
    """1.json文件的读操作"""
    # 打开json文件
    with open('./files/test.json', 'r', encoding='utf-8') as f:
        # 直接使用read()去读，获取到的是字符串数据，包含了json文件中的所有的内容(包括注释部分)
        # conten = f.read()
        # print(conten, type(conten))
        """
        load(文件对象): 获取指定json文件中的内容,返回值的类型是json文件最外层的对应的数据类型
        dict ---> dict
        array ---> list
        string ---> str
        number ---> int/float
        true/flase --> True/Flase
        null ---> None
        """
        content = json.load(f)
        print(content, type(content), content['成绩'][1])


    """2.json文件的写操作"""
    # 打开文件
    with open('./files/new.json', 'w', encoding='utf-8') as f:
        # 写数据
        """
        dump(写的内容, 文件对象)
        """
        # w_content = 'abc'
        w_content = [
            {'name': 'a1', 'age': 18},
            {'name': 'a2', 'age': 20}
        ]
        json.dump(w_content, f)


    """
    3.json模块的其他操作
    loads(字符串,编码方式) ---> 将指定的字符串(json字符串)，转化成json数据
    将字符串转换成字典\将字符串转换成列表
    """
    # {"a": true, "b": 2}
    #
    content = json.loads('["a",100, false,{"a":1, "abc":"100"}]', encoding='utf-8')
    print(content, type(content))

    """
    dumps(对象)
    将对象转换成json字符串
    字典/列表转换成json字符串
    """
    content = json.dumps(['aaa', 1, True])
    # content = '["aaa", 1, true]'
    content2 = str(['aaa',1, True])
    # content2 = '['aaa', 1, True]'
    print(content,content2, type(content))



