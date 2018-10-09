# Filename  : 练习.py
# Date  : 2018/8/9
import re

a = '123四川省成都市abc'
re_str = r'([\u4e00-\u9fa5]{1,})'
match1 = re.search(re_str,a)
print(match1,type(match1))
if __name__ == '__main__':
    pass