"""__author__ = 余婷"""
"""
1.函数的声明
def 函数名(形参列表):
    '''函数说明'''
    函数体
    
2.怎么声明函数
参数的作用：从函数外面给函数传值

3.函数的调用：
    a.回到函数声明的地方
    b.将实参的值赋给形参
    c.执行函数体  
    
    
4.函数的参数
# 调用
位置参数和关键字参数

# 声明
给参数赋默认值（有默认值的参数放到后边）
参数个数不定
"""


""" 9. 写 个函数，可以对多个数进  同的运算"""
def operation(char, *numbers):
    if char == '+':
        sum1 = 0
        for item in numbers:
            sum1 += item
        print('和为:',sum1)

    elif char == '-':
        if len(numbers):
            sum1 = numbers[0]
            for index in range(len(numbers)):
                # 如果下标不是0，就减
                if index:
                    sum1 -= numbers[index]
            print('差为:', sum1)
        else:
            print('没有可操作的数字')


operation('-', 10, 20, -40)







