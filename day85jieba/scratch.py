import re
from collections import Counter

import jieba

# 打开文件
path = r'C:\Users\Administrator\Desktop\santi.txt'
with open(path, 'r', encoding='utf-8') as f:
	string = f.read()

replce_str = re.sub(r"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，啊呀嗯的“”：①。？、~@#￥%……&*（）]+", "",string)

result = jieba.cut(replce_str)

result1 = [i for i in result]
result1.pop(0)


print(Counter(result1))