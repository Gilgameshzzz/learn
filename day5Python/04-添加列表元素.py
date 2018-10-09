# 添加列表元素
skills = []
# 1、append 函数
"""
列表.append(元素)
在列表的末尾添加一个元素
"""
skills.append('气体源流')
print(skills)

skills.append('拘灵遣将')
print(skills)

# 2、insert函数
"""
列表.insert(下标，元素)
在列表的指定的下标前插入一个元素，
注意：下标可以越界，越界后插入的元素要么最后，要么最前面，也可以为负数
"""
skills.insert(0, '通天箓')
print(skills)

# 3、+
"""
列表1+列表2
将列表2的元素和列表1中元素合并后创建一个新的列表
"""
new_skills = skills + ['丰厚气门', '阿威十八式']
print(new_skills)


# 练习：从控制台输入10个学生的成绩，然后保存在一个列表中
score = []
for i in range(10):
    sum1 = float(input('输入成绩:'))
    if sum1 > 0:
        score.append(sum1)
    else:
        sum1 = float(input('输入错误，请重新输入'))
print(score)
