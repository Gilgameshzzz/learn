# Filename  : 练习.py
# Date  : 2018/8/1

import json

with open('./data.json', encoding='utf-8') as g:
    d = json.load(g)
    # 把需要的数据转换成字典
    data1 = d['data'][0]


class Data:
    def __init__(self):
        self.type = ''
        self.text = ''
        self.user_id = ''
        self.name = ''
        self.screen_name = ''
        self._width = 0
        self._height = 0
        self._themes = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, num):
        if type(num) != type(23):
            print('输入有误，请输入数字')
        else:
            self._width = int(num)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, num):
        if type(num) != type(23):
            print('输入有误，请输入数字')
        else:
            self._height = int(num)

    @property
    def themes(self):
        if not self._themes:
            return '无'
        return self._themes

    # 根据字典创建对象
    @classmethod
    def creat_data(cls, dict1):
        data = cls()
        for key in dict1:
            if key == 'width':
                data.width = dict1[key]
                continue
            if key == 'height':
                data.height = dict1[key]
                continue
            if key == 'themes':
                data._themes = dict1[key]
                continue
            data.__setattr__(key, dict1[key])
        return data


if __name__ == '__main__':
    print(data1)
    data = Data()
    data2 = data.creat_data(data1)
    print(data2.screen_name)
