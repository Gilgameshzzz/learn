"""__author__ = 余婷"""

import re


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
        fen = float(time[:2])
        miao = float(time[3:])
        self._time = fen*60 + miao

    # 重载 <
    def __lt__(self, other):
        return self._time < other._time

    # 自定义类的对象的打印
    def __str__(self):
        return str(self._time)+':'+self.lrc




class AnalysisLyrics:
    """解析歌词"""
    def __init__(self, file_path):
        self.all_lrc = []
        self.file_path = file_path

    def __anlysis_lyrics(self):
        """解析歌词"""
        # 打开歌词文件
        with open(self.file_path,'r', encoding='utf-8') as f:
            # 一行一行的读文件中的内容
            line = f.readline()
            while line:
                # 对当前读的一行的内容进行操作
                self.__operate_line(line)
                line = f.readline()

        # 在这儿已经将文件中所有的内容都读忘了，并且转换成了歌词对象，保存到all_lrc中了
        # 排序
        self.all_lrc.sort(reverse=True)
        # for lrc in self.all_lrc:
        #     print(lrc)


    def __operate_line(self, line):
        # print(line)
        # [00:00.20]蓝莲花

        # 切割
        lines = line.split(']')
        # ['[00:00.20','蓝莲花']

        # 取词
        lrc = lines[-1]
        # 蓝莲花

        # 遍历所有的时间
        # index = range(0,1)  -> 0
        for index in range(len(lines)-1):
            # print('%s:%s' % (lrc, lines[index][1:]))
            # 创建歌词对象
            lyrics = Lyrics()
            # 设置歌词和时间属性
            lyrics.lrc = lrc
            # 蓝莲花
            lyrics.time = lines[index][1:]
            # 00:00.20

            # 保存歌词对象
            self.all_lrc.append(lyrics)

    def show_lrc(self, time):
        # 如果已经解析过了，就不用再解析了
        if not self.all_lrc:
            self.__anlysis_lyrics()
        # 取时间对应的歌词
        for item in self.all_lrc:
            if item.time < time:
                return item.lrc


import time

if __name__ == '__main__':
    lan_lian_hua = AnalysisLyrics('./蓝莲花')

    time1 = 0
    while True:
        time.sleep(1)
        time1 += 1
        print(lan_lian_hua.show_lrc(time1))

    # with open('./蓝莲花','r',encoding='utf-8') as f:
    #     print('~~~',f.readline())
    #     # f.seek(字节数)
    #     f.seek(0)
    #     print('===',f.readline())
    #     print('!!!', f.read())





