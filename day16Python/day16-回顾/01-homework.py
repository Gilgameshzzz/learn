"""__author__ = 余婷"""
"""
一.获取字符串中：  
a.所有的正整数  +12233 2776 
b.所有的负整数  
c.所有的浮点数  
d.所有的非负浮点数 
"""

import re

if __name__ == '__main__':
    """
    1.+-
    2.1263 r'[1-9]\d*'
    3.123.00, 237.98 r'[1-9]\d*\.\d+'
    4.0.2389 r'0\.\d+'
    """
    # 去一个字符串中所有的数字
    all_numbers = re.findall(r'[+-]?[1-9]\d*\.\d+|[+-]?0\.\d+|[+-]?[1-9]\d*', 'sh0.23j1-123klp-34.89pp278s+12kh89.0h-889jj')
    print(all_numbers)

    # a.取所有的正整数
    print('所有的正整数', end=':')
    for numer in all_numbers:
        if not('.' in numer or '-' in numer):
            print(numer, end='  ')

    # b.取所有的负整数
    print('\n所有的负整数', end=':')
    for numer in all_numbers:
        if '-' in numer and '.' not in numer:
            print(numer, end='  ')
    # c.取出所有的浮点数
    print()
    print(re.findall(r'[+-]?[1-9]\d*\.\d+|[+-]?0+\.\d+', 'sh0.23j1k0000.00-123klp-34.89pp278s+12kh89.0h-889jj'))

    # d.所有的非负浮点数
    for numer in all_numbers:
        if '.' in numer and '-' not in numer:
            print(numer,  end='  ')
    print()
    print(re.fullmatch(r'\w*\b-\b\w*|\w*','back-end'))





