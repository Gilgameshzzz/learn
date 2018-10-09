"""__author__ = 余婷"""
"""
出现异常(错误)不想让程序崩溃，就可以进行异常捕获
try:
    需要捕获异常的代码
except:
    出现异常会执行的代码
    
try:
    需要捕获异常的代码
except 错误类型:
    捕获到指定的错误类型，才执行的代码
    
"""

if __name__ == '__main__':
    try:
        with open('./aaaa.txt') as ff:
            print('打开成功')
    except FileNotFoundError:
        print('===')
        open('./aaa.txt','w')