"""__author__ = 余婷"""

from random import randint


class Color:
    """颜色类"""
    white = 255, 255, 255
    green = 0, 255, 0
    red = 255, 0, 0
    black = 0, 0, 0
    gray = 100, 100, 100
    light_gray = 200, 200, 200

    @staticmethod
    def rgb_color(r, g, b):
        """rgb颜色值"""
        return r, g, b

    @staticmethod
    def rand_color():
        """随机颜色"""
        return randint(0, 255), randint(0, 255), randint(0, 255)


