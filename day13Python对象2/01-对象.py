# Filename  : 01-对象.py
# Date  : 2018/8/1

"""对象的属性：通过对象来使用；声明init方法，self.属性名=值"""
# 类的字段：通过类来使用；类里面函数的外面，属性名=值

"""
init方法
a、用来初始化对象的属性
b、通过类创建对象的时候，系统自动调用init方法(创建的时候要保证init每个参数都要有值)
"""

# 注意：如果函数的参数是对象（列表、字典、类的对象），传参的时候传的
# 是地址，如果函数中需要对象的内容进行修改，传参的时候传对象的拷贝（如果是列表可以切片）
def func1(list1):
    list1.append(10)
    print(list1)

def func2(list2):
    list2.append(20)
    print(list2)


list11 = [1, 2, 3, 4]
func1(list11)
func2(list11)

func1(list11[:])
func2(list11[:])


if __name__ == '__main__':
    pass