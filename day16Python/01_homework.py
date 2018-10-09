# Filename  : 01_homework.py
# Date  : 2018/8/6
"""
解析歌词
分析：面向对象
1.需要几个类
类1 --->解析歌词文件
类2 --->解析歌词时间
"""
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
        miao =float(time[3:])
        self._time = fen*60 + miao

    # 重载 <
    def __it__(self, other):
        return self._time < other._time


class AnalysisLyrics:
    """解析歌词"""
    def __init__(self, file_path):
        self.all_lrc = []
        self.file_path = file_path

    def analysis_lyrics(self):
        """解析歌词"""
        # 打开歌词文件
        with open(self.file_path, 'r', encoding='utf-8') as f:
            # 一行一行的读文件中的内容
            line = f.readline()
            while line:
                # 对当前读的一行的内容进行操作
                self.operate_line(line)
                line = f.readline()

        # 在这儿已经将文件中所有的内容都读完了，并且转换成歌词对象，保存到all_lrc中



    def operate_line(self, line):
        # 切割
        lines = line.split(']')
        # 取词
        lrc = line[-1]

    def show_lrc(self, time):
        # 如果已经解析过了，就不用再解析了
        if not self.all_lrc:
            self.analysis_lyrics()
        # 取时间对应的歌词
        for item in self.all_lrc:
            if item.time < time:
                return item.lrc

if __name__ == '__main__':
    pass