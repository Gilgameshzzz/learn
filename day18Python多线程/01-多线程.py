# Filename  : 01-多线程.py
# Date  : 2018/8/8

import threading
import time

def download(file):
    print('开始下载',file)
    time.sleep(3)
    print(file,'下载完成')

if __name__ == '__main__':
    print('abc')
    # 1、创建线程对象
    """
    target:需要在子线程中执行的函数
    args:调用函数的参数列表 (参数类型是列表)
    返回值：线程对象
    """
    t1 = threading.Thread(target=download,args=['亚人'])
    # 2、在子线程中执行任务
    t1.start()

    t2 = threading.Thread(target=download, args=['无头骑士异闻录'])
    t2.start()

    # download('英雄')
    # download('女神异闻录5')
    print('=======')