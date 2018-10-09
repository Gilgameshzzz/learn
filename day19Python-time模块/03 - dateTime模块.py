# Filename  : 03 - dateTime模块.py
# Date  : 2018/8/9
import datetime

if __name__ == '__main__':
    # 1、日期类（date）--只能表示年月日
    """1、类的字段"""
    # 最小日期
    print(datetime.date.min,type(datetime.date.min))
    # 最大日期
    print(datetime.date.max,type(datetime.date.max))
    # 最小单位
    print(datetime.date.resolution)

    """2.类方法"""
    # 获取当前日期
    today1 = datetime.date.today()
    print(today1)

    # 将时间戳转换成日期
    today2 = datetime.date.fromtimestamp(1000000)
    print(today2)

    """2、对象属性"""
    print(today1.year,type(today1.year))
    print(today1.month)
    print(today1.day)

    """3、对象方法"""
    # 1、获取星期（0-6 -->周一到周天）
    print(today1.weekday())
    print(today1.isoweekday())  #返回的1-7代表周一到周日

    # 2、将指定日期转换成指定格式的字符串日期
    print(today1.strftime('%Y-%m-%d %w'))

    # 创建日期对象
    print(datetime.date(2017,8,29))

    # ==========datetime==========
    datetime.datetime