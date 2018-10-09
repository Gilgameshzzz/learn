# Filename  : 02-时间模块.py
# Date  : 2018/8/9
# 主要包含处理年月日，时分秒对应的时间，主要着重时分秒
import time

# 专门处理年月日
import datetime

if __name__ == '__main__':
    #1、获取时间
    """
    时间戳：就是从格林威治时间（1970年1月1日0:0:0）到当前时间的时间差（单位是秒）
    1、存时间以时间戳的形式去存，可以节省空间（一个浮点数的内存是4/8个字节，若存字符串一个字符占2个字节）
    2、自带对时间加密的功能（加密更方便）
    """
    time1 = time.time()
    print(time1,type(time1))

    # 2、将时间戳转换成struct_time
    """
    localtime(seconds)
    参数seconds:a、不传参，就是将当前时间对应的时间戳转换成struct_time
    b、传参，就是将指定的时间转换成struct_time
    """
    time1 = time.localtime()
    print(time1)
    """
    struct_time的结构
    tm_year:年
    tm_mon:月
    tm_mday:日
    tm_hour:时
    tm_min:分
    tm_sec:秒
    tm_wday:星期（0-6 -->周一-周天）
    tm_yday:当前是当年的第几天
    tm_isdst:是否是夏令时
    """
    struct1 = time.localtime(100000)
    print(struct1)
    # 2.1将struct_time转换成时间戳
    """
    mktime(结构时间)
    """
    """2018-8-31 23:30:40"""
    strc = time.strptime('2018-8-31 23:30:40','%Y-%m-%d %H:%M:%S')
    time1 = time.mktime(strc)
    # 时间加一个小时
    time1 += 3600
    print('===',time.localtime(time1))

    # 3、时间的格式转换
    """
    strftime(时间格式，时间)
    将时间以指定的格式转换成字符串
    """
    time_str = time.strftime('%j',time.localtime())
    print(time_str)

    """
    strptime(需要转换的字符换，时间格式)
    将时间字符串转换成相应的struct_time
    """
    struct_time = time.strptime('今天是8102年8月9号','今天是%Y年%m月%d号')
    print(struct_time)


    # 4、延迟
    """
    sleep(秒)
    可以让线程阻塞指定的时间
    """
