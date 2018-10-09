# 1、输出函数 ： print()
"""
1、默认每一个print函数，输出完内容后输出一个换行
2、一个print函数输出多个内容的时候，内容之间是用空格隔开
3、内容后边加 end= 来设置结束标志，默认是 \n
4、通过设置sep的值来设置多个内容之间的间隔符，默认一个空格
"""
print('gasds', 100, end='\t', sep='^')
print('zhisdsa')

# 2、输入函数：input()函数
"""
1、input()函数可以接收从控制台输入的内容（以回车为结束标志）
2、input函数会阻塞线程，程序执行到input的时候会停下来，等待用户的输入，
输入完成后才会执行下面的内容
3、接收到的数据是以字符串的形式返回的(Python2.x中输入的数字时候，可能返回int类型或浮点型)
"""
value = input('输入一个整数：')
print('name', value, type(value))

# 练习：猜数字游戏
"""
随机产生一个1-100的整数，输入的数字如果和产生的随机数一样，就提示猜对了并结束
如果输入的数大于或小于随机数，就提示输入的数字偏大或偏小，然后重新输入
"""
# 产生一个随机数
import random
num = random.randint(1, 10)

while True:
    shu_ru = int(input('请输入一个数：'))
    if shu_ru < num:
        print('输小了')
    elif shu_ru > num:
        print('输大了')
    else:
        print('猜对了')
        break

