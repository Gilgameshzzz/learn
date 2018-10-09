# Filename  : 作业.py
# Date  : 2018/7/26

import homework

new_files = homework.get_write('./test1.txt', '这是个测试，mayday')


new_files1 = homework.get_read('./test1.txt')
print(new_files1)