"""__author__ = 余婷"""

"""
(所有)文件操作流程: 打开文件 -> 操作文件(读/写) -> 关闭文件

1.打开文件: open(文件路径,打开的方式,编码方式)
文件路径(必填) ---> 决定打开哪个文件
打开方法(默认值是'r') ---> 决定打开文件后是进行什么样的操作
'r' - 读操作(读出来是字符串)
'rb'/'br' - 读操作(读出来的数据是二进制) 
'w' - 写操作(可以将文本数据写入文件中)
'wb'/'bw' - 写操作(可以将二进制数据写入文件中)
'a' - 写操作(追加)

编码方式 --> 主要针对文本文件的读写(不同的操作系统默认的文本编码方式不同，windows->gbk, mac->utf-8)



"""

if __name__ == '__main__':
    # 2.文本文件读操作
    """
    a.放在工程外面的文件,写绝对路径：/Users/yuting/Desktop/test.txt
    """
    # open('/Users/yuting/Desktop/test.txt')

    """
    (推荐)
    b.将文件放到工程目录下的某个位置，写相对路径(相对于工程目录)：./相对路径 或者 ../相对路径
    当py文件直接放在工程目录下，想要使用open打开工程中的其他文件使用'./'
    当py文件在工程目录的子目录下面，想要使用open打开工程中的其他文件使用'../'
    """
    # open('./test1.txt')
    # open('./files/test2.txt')
    # open('./files/text/test2.txt')
    # 1.打开文件
    # 打开文件，返回文件句柄(文件代言人)
    f = open('./test1.txt', 'r', encoding='utf-8')
    # 2.读文件(获取文件文件的内容)
    """
    文件.read() ： 获取文件内容，并且返回
    read(n) --> n 设置读的长度
    """
    content = f.read()
    print(content)
    # 3.关闭文件
    f.close()


    """3.文本文件的写操作"""
    # 1.打开文件
    """
    注意: 以读的方式打开文件，如果这个文件不存在，会报错FileNotFindError;
         以写的方式打开文件，如果这个文件不存在，就会创建这个文件
    """
    f = open('./test11.txt', 'a', encoding='utf-8')
    # 2.写操作
    """
    'w':在写的时候会清空文件中原来的内容，然后再往里面写数据
    'a':在原文件内容的最后添加新的数据
    """
    f.write('疑是地上霜')
    # 3.关闭文件
    f.close()

    """
    4.二进制文件的读写操作
    音频、视频、图片文件，都是二进制文件
    """
    f = open('./files/luffy.jpeg', 'rb')
    # 读文件
    image_data = f.read()
    # bytes: python中二进制数据对应的数据类型
    print(type(image_data),image_data)
    # 关闭文件
    f.close()

    """二进制文件的写操作"""
    f = open('./files/new.jpeg', 'wb')
    f.write(image_data)
    f.close()


    """
    4.通过with关键字去打开文件
    
    with open() as 文件变量名:
        文件操作
        
    在文件操作结束后会自动去关闭文件
    
    """
    # 读
    with open('./files/一人之下.mp4','rb') as file:
        mp4_data = file.read()

    # 写
    with open('./new.mp4', 'wb') as f:
        f.write(mp4_data)



