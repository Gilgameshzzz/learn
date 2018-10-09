"""__author__ = 余婷"""
"""
生成器：a.可以看成是一个可以存储多个数据的容器。需要里面的数据的时候就生成一个，里面的数据只能从前往后一个一个的生成，
       不能跳跃，也不能从后往前。生成的数据，不能再生成了
      b.获取生成器里面的数据，需要使用__next__()方法  
      c.只要函数声明中有yield关键字，函数就不再是一个单纯的函数，而变成一个生成器
      
和列表比较: 列表存数据，数据必须是实实在在存在的数据，一个数据会占一定的内存空间。
          生成器存数据，存的是产生数据的算法，没有数据去占内存空间
      
      

"""

# 1,1,2,3,5,8,13,21.....
def xu_lie(n):
    pre_1 = 1
    pre_2 = 1
    for x in range(1, n+1):
        if x == 1 or x == 2:
            current = 1
            yield current

            # print(current)
            continue
        current = pre_1 + pre_2
        pre_1, pre_2 = pre_2, current
        # print(current)
        yield current

print(xu_lie(10))
xulie = xu_lie(10)
print(xulie.__next__())
print(xulie.__next__())
print(xulie.__next__())

for x in xulie:
    print('==:',x)


if __name__ == '__main__':
    x = (i for i in range(100000))
    # x 就是一个生成器，用来产生数据
    print(x)

    print(x.__next__())
    print(x.__next__())

    print('=====')
    num = 100

    print(x.__next__())

    # print(xulie.__next__())




