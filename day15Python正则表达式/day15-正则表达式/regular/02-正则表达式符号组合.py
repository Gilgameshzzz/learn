"""__author__ = 余婷"""
import re
if __name__ == '__main__':
    # 1. [] 匹配[]中出现的任意一个字符
    """匹配一个字符串，前三位是abc,第四位是字符1或者字符a"""
    re_str = r'abc[1a,]'
    print(re.fullmatch(re_str, 'abca'))

    """第一位是数字或者下划线，后面是abc"""
    re_str = r'[\d_]abc'
    print(re.fullmatch(re_str, '9abc'))

    # 2. [^] 匹配不在[]中出现的任意一个字符
    """匹配一个字符串，前三位是anc,第四位不是数字字符也不是字符a"""
    re_str = r'abc[^\da]'
    print(re.fullmatch(re_str, 'abcl'))

    # 3. * 匹配0次或者多次
    """匹配一个字符串，前面是0个或者多个数字字符，然后是abc"""
    re_str = r'\d*abc'
    print(re.fullmatch(re_str, '19076abc'))

    """
    [0-9] : 匹配0，1，2，3，4，5，6，7，8，9中的任意一个字符
    [1-8] : 匹配1，2，3，4，5，6，7，8
    [a-z] : 匹配任意一个小写字母
    [A-Z] : 匹配任意一个大写字母
    [a-zA-Z]: 匹配所有的字母
    """
    print(re.fullmatch(r'[a-zA-Z]', 'B'))

    # 写一个正则表达式，判断一个字符串是数字字符串（不能空串）
    re_str = r'\d\d*'
    re_str = r'[0-9][0-9]*'
    print(re.fullmatch(re_str, '0'))

    # 写一个正则表达式，检测一个字符串是否是合格的标识符(字母数字下划线组成，数字不开头)
    """
    abc  -> 成功
    _a12h -> 成功
    __23a -> 成功
    1hj_ -> None
    a*h -> None
    """
    re_str = r'[a-zA-Z_]\w*'
    print(re.fullmatch(re_str, 'a*h'))

    # 4. + 匹配一次或者多次
    """匹配一个字符串开头出现一次或者多个数字字符，然后再有0次或者多次数字、字母、下划线"""
    re_str = r'\d+\w*'
    print(re.fullmatch(re_str, '16u78abc'))

    # 5.? 匹配0次或者1次
    re_str = r'[a-z]?123'
    print(re.fullmatch(re_str, 'z123'))

    # 判断是一个字符串是否是正整数字符串(除0) '123' -> 成功 '+1234' -> 成功 '0123' -> None '12012' ->  成功
    re_str = r'[+]?[1-9]\d*'
    print(re.fullmatch(re_str, '+1234'))

    # 5.{N} 匹配N次
    """前面5个数字，然后是abc"""
    re_str = r'\d{5}abc'

    re_str = r'[12ab]{3}abc'
    print(re.fullmatch(re_str, '11babc'))

    # 6.{N,} 匹配大于等于N次
    """字符串前面至少三位数字，后面随意"""
    re_str = r'\d{3,}.*'
    print(re.fullmatch(re_str, '151263jah92390..;'))

    # 7.{M,N} 匹配至少M次，最多N次
    """密码要求：数字、字母组成，并且8-16位"""
    re_str = r'[\da-zA-Z]{6,10}'
    print(re.fullmatch(re_str, 'uy2huy?28'))

    # 8. | 分之
    """匹配一个字符串，是三个数字字符或者是三个小写字符"""
    re_str = r'\d{3}|[a-z]{3}'
    print(re.fullmatch(re_str, 'hsu'))

    # 9.() 匹配的时候是分组，让括号中的正则条件变成一个整体,进行整体操作
    """匹配一个字符串，abc整体重复3次"""
    re_str = r'(abc){3}'
    print(re.fullmatch(re_str, 'abcabcabc'))

    re_str = r'(\d\w[0-3]){2}'
    print(re.fullmatch(re_str, '3o37h1'))

    """========以下了解========"""
    # 尽可能少：在能够匹配到的前提下尽可能少
    # 10. *? 重复任意次，尽可能少的重复
    re_str = r'ba*?b'
    print(re.match(re_str, 'baabaa'))

    # 11. +? 重复一次或多次，尽可能少的重复
    re_str = r'ba+?'
    print(re.match(re_str, 'baaaa'))

    # 12. ?? 重复0次或者1次， 尽可能少的重复
    re_str = r'b??'

    # 13. {N,}? 重复至少N次，尽可能少的重复
    # 14. {N, M}? 重复N到M次，尽可能少的重复























    # 写一个正则表达式能够匹配一个合格分数(0-100)






