# Filename  : 03-正则表达式.py
# Date  : 2018/8/3
"""

正则中： . \ [] {} () * + ? ^ & |,这些字符有特殊意义，所以在正则表达式中
如果想要单纯表达这些字符，需要在前面加“ \ ”；
注：1、-， []， ^， \， 在中括号中可能是特殊符号,需要加\
2、 .， {}， ()， *， +， ?， $， |， 在中括号中可以不用加\，来表示字符
re_str = r'[\^]' #匹配 字符^
re_str = r'[\\]' #匹配 字符\

"""

import re

#  1、\N --->匹配前面第N个组中匹配到的内容 （匹配括号里的）
re_str = r'([1-9][a-z]{2})n(\d)\1\2'
print(re.fullmatch(re_str, '9hjn09hj0'))

if __name__ == '__main__':

    #  验证输入用户名和qq号是否有效并给出对应的信息
    re_str1 = r'\w{6,20}'
    re_str2 = r'[1-9][0-9]{4,11}'

    #   练习 IP是否合法
    re_str3 = r'(([1-9]|[1-9]\d|2[0-4]\d|1\d\d|25[0-5])\.){3}([1-9]|[1-9]\d|2[0-4]\d|1\d\d|25[0-5])'
    print('====', re.fullmatch(re_str3, '255.255.54.234'))


