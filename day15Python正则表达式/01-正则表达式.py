# Filename  : 01-正则表达式.py
# Date  : 2018/8/3
"""
正则表达式：用来做字符串查找、匹配、切割用的一种工具

Python对正则表达式的支持：提供了re模块（python内置模块），包含字符串匹配、
查找、切割等相关方法
fullmatch(正则表达式，字符串)：用正则表达式来和字符串进行匹配，看是否能够匹配成功
正则表达式：是一个符合正则规范的字符串
"""

import re

if __name__ == '__main__':

    # 注意：正则表达式的字符串，前面一般要加r来阻止转义。因为正则表达式的符号中有很多带'\'的
    # 符号，其功能不是转义，而是表示特殊的意义
    # 1、 .:匹配一个任意的字符
    """匹配两个任意字符的字符串"""
    re_str = r'..'
    """匹配第一个字符是a第二个字符是b的字符串"""
    re_str = r'ab'
    """匹配第一个字符是a，第二个字符是任意字符的字符串"""
    re_str = r'a.'
    print(re.fullmatch(re_str, 'ab'))

    # 2、\w 匹配一个字符是字母、数字或者下划线
    re_str = r'\w'
    print(re.fullmatch(re_str, 'o'))

    # 3、 \s匹配一个空白字符（空格、换行、制表符）
    """匹配第一个字符是a,第二个字符是空白，最后一个是字符b的字符串"""
    re_str = r'a\sb'
    print(re.fullmatch(re_str, 'a\tb'))

    # 4、 \d匹配一个数字字符
    re_str = r'\d\d\d'
    print(re.fullmatch(re_str, '334'))

    # 5、 \b检测边界(字符串结束，字符串开头,单词边界---一般的符号都可以作为单词的边界)
    print(re.match(re_str, '0133'))

    """匹配三个任意字符的前面和后面都是单词边界的字符串"""
    re_str = r'\b...\b'
    print(re.match(re_str, 'wdw.we'))

    # 6、 ^匹配字符串开始（^The --匹配以The开头的字符串）
    re_str = r'^The'
    print(re.findall(r'^The', 'Thewsd The23dsad'))

    # 7、 $匹配字符串结束（Tqe$ --匹配以Tqe结束的字符串）
    re_str = r'Tqe$'
    print(re.findall(re_str, 'ThweqewsdThe  eewTqe'))

    # 8、\W(大写W)匹配非字母、数组、下划线
    re_str = r'\W\w'
    print(re.fullmatch(re_str, '$s'))

    # 9、 \S匹配非空白符
    re_str = r'\S\d'
    print(re.fullmatch(re_str, 'p8'))

    # 10、 \D 匹配非数字字符
    """匹配第一个字符是非数字字符，第二字符是字母、数字、下划线"""
    re_str = r'\D\w'

    # 11、 \B 检测非边界
    re_str = r'abc\B'
    print(re.fullmatch(re_str, 'abc'))
