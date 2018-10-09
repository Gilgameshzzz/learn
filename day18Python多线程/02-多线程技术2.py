# Filename  : 02-多线程技术2.py
# Date  : 2018/8/8
"""
方式2：写一个自己的线程类
1、写一个类，继承自Thread类
2、重写run方法，在里面规定需要在子线程中执行的任务
3、在子线程中执行的任务对应的功能，如果需要参数，通过类的对象属性来传值
"""
from threading import Thread
import requests
import re
# 下载数据
class DownloadThread(Thread):
    """下载类"""
    def __init__(self,file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        """run方法"""
        """
        1、写在这个方法的内容就是在子线程中执行的内容，
        2、这个方法不要直接调用
        """
        print('开始下载')
        response = requests.request('GET',self.file_path)
        data = response.content

       # 获取文件后缀
        suffix = re.search('.{4}\.\w+$',self.file_path).group()
        with open('./git'+suffix,'wb') as f:
            f.write(data)
        print('下载完成。。。')

if __name__ == '__main__':
    print('22==22')
    t1 = DownloadThread('http://img3.imgtn.bdimg.com/it/u=1799413732,2888154639&fm=27&gp=0.jpg')
    # 通过start简介调用run方法，run方法中的任务在子线程中执行
    t1.start()
    # 直接调用run方法，run方法中的任务在当前线程中执行
    print('11==11')