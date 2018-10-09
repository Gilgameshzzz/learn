"""__author__ = 余婷"""


class Lyrics:
    """歌词类"""
    def __init__(self):
        self.lrc = ''
        self._time = 0

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        # 在给时间赋值前，将时间字符串转换成秒
        index = time.index(':')
        fen = time[1:index]
        miao = time[index+1:]
        self._time = float(fen)*60 + float(miao)

    def __str__(self):
        return str(self.time)+':'+self.lrc

    def __gt__(self, other):
        return self.time > other.time



class LrcAnalyzer:
    """歌词解析类"""

    # 保存所有的歌词对象
    __all_lrcs = []



    @classmethod
    def __analysis(cls, file):
        """读取歌词内容"""
        # 将数据读出来
        with open(file, 'r', encoding='utf-8') as f:
            """
            readline():读一行内容
            while循环：每次读文件中的一行内容，读完为止
            """
            line = f.readline()
            while line:
                # 创建歌词
                cls.__creat_lrc(line)
                line = f.readline()

            # 歌词获取完后,对歌词按时间排序
            cls.__all_lrcs.sort(reverse=True)


    @classmethod
    def __creat_lrc(cls, line):
        """将一行歌词转换成歌词对象"""
        # 按']'进行切割, 每一行切割成一个列表：['[02:11.27', '[01:50.22', '[00:21.95', '穿过幽暗地岁月\n']
        lrcs = line.split(']')

        # 遍历列表获取每个元素，获取歌词和时间
        # 获取最后一个元素作为歌词
        lrc = lrcs[-1]
        # 从第一个到倒数第二个是时间
        for index in range(0, len(lrcs)-1):
            time = lrcs[index]
            lrc_obj = Lyrics()
            lrc_obj.lrc = lrc
            lrc_obj.time = time
            cls.__all_lrcs.append(lrc_obj)

    @classmethod
    def get_lrc(cls, time, file):
        """根据时间获取歌词"""
        # 先判断是否已经解析歌词，如果没有，先将歌词解析
        if not cls.__all_lrcs:
            cls.__analysis(file)

        # 由时间从大到小，找到第一个小于等于指定的时间的歌词就是要找的歌词
        for lrc_obj in cls.__all_lrcs[:]:
            if lrc_obj.time <= time:
                return lrc_obj

import time
if __name__ == '__main__':

    number = 0
    while True:
        time.sleep(0.01)
        number += 0.01
        print(LrcAnalyzer.get_lrc(number, './files/蓝莲花.txt'))


