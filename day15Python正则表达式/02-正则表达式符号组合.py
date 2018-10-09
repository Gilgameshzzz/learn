# Filename  : 02-正则表达式符号组合.py
# Date  : 2018/8/3

import re

if __name__ == '__main__':
    # 1、[]匹配[]中出现的任意一个字符，只匹配一个
    """匹配一个字符串，前三位是abc,第四位是字符1或者字符a"""
    re_str = r'abc[1a]'
    print(re.fullmatch(re_str, 'abca'))
    """第一位是数字或者下划线，后面是abc"""
    re_str = r'[\d _]abc'
    print(re.fullmatch(re_str, ' abc'))

    """
    [0-9]:匹配0到9中的任意一个数字字符
    [a-z]:匹配任意一个小写字母
    [A-Z]:匹配任意一个大写字母
    [a-zA-Z]：匹配任意一个字母（包括大小写）
    """



    # 2、[^]匹配不在[]中出现的任意一个字符
    """匹配一个字符串，前三位是abc,第四位不是数字也不是字符a"""
    re_str = r'abc[^\da]'
    print(re.fullmatch(re_str, 'abcU'))


    # 3、 *匹配0次或者多次
    """匹配一个字符串，前面是0个或者多个数字字符，然后是abc"""
    re_str = r'\d*abc'
    """判断一个字符串是数字字符串"""
    re_str = r'\d\d*'

    re_str = r'\d{1,3}'
    print(re.fullmatch(re_str, '4'))

    # 检测一个字符串是否是合格的字符串
    re_str = r'[_a-zA-Z][_a-zA-Z0-9]*'  # r'[_a-zA-Z]\w*'
    print(re.fullmatch(re_str, '__wdfs4__324'))

    # 4、 +：匹配一次或者多次
    """匹配一个字符串开头出现一次或者多个数字字符，然后再有0次或者多次数字、字母、下划线"""
    re_str = r'\d+\w*'
    print(re.fullmatch(re_str, '232o23sdw'))

    # 5、 ？：匹配0次或1次
    # 判断一个正整数字符串
    re_str = r'[+]?[1-9]\d*'

    # 6、{N} 匹配N次
    re_str = r'\d{5}abc'  # 前面5个数字，然后是abc

    # 7、{M,}匹配大于等于M次
    """前面至少三位数字，后面随意"""
    re_str = r'\d{3,}.*'

    #  8、{M,N}匹配至少M次，最多N次
    """password要求：数字、字母组成，并且8-16位"""
    re_str = r'[\da-zA-Z]{6,10}'

    # 9、 | 分之(或者)
    """ 匹配一个字符串，是三个数字字符或者是三个小写字符"""
    re_str = r'\d{3}|[a-z]{3}'
    print(re.fullmatch(re_str, 'qwe'))

    # 10、()匹配的时候是分组，让括号中的正则条件变成一个整体,进行整体操作
    """匹配一个字符串，abc整体重复3次"""
    re_str = r'(abc){3}'

    """===以下了解==="""
    # 尽可能少：在能够匹配到的前提下尽可能少
    # 10 、*？重复任意次，尽可能少的重复
    re_str = r'a*?'
    print(re.match(re_str, 'aaaaa'))


    pass