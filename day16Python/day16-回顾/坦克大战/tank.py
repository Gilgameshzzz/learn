"""__author__ = 余婷"""
# 枚举类：声明一个类，继承Enum
"""
1.类中只能有类字段用来存储一些固定的值
2.可以使用@unique修饰，让类中的字段的值唯一
3.字段的值保存在字段的value属性中
4.类变成枚举后，只有字段对象的对象（不能自己再去创建其他的对象）
"""
from enum import Enum, unique
# @unique


# 修饰后，类中的字段的值必须唯一
# @unique
class Direction():
    """方向类"""
    left = 276
    right = 275
    up = 273
    down = 274


import pygame
class Tank:
    """坦克类"""
    image_up = pygame.image.load("./imge/p1tankU.gif")
    image_down = pygame.image.load("./imge/p1tankD.gif")
    image_left = pygame.image.load("./imge/p1tankL.gif")
    image_right = pygame.image.load("./imge/p1tankR.gif")

    def __init__(self, pos):
        self.image = Tank.image_up
        self.x = pos[0]
        self.y = pos[1]
        self.x_speed = 0
        self.y_speed = -3
        self._direction = Direction.up
        self.is_move = False
        self.all_bullet = []

    def shoot(self):
        """发射子弹"""
        # 1.创建一个子弹对象
        # 2.根据坦克的方向设置子弹方向和子弹的初始位置
        # 3.保存起来
        pass

    def move(self, screen):
        """坦克移动"""
        if not self.is_move:
            return
        newx = self.x + self.x_speed
        newy = self.y + self.y_speed

        sw, sh = screen.get_size()
        tw, th = self.image.get_size()

        # 判断是否越界
        if newx <= 0:
            newx = 0
        elif newx >= sw - tw:
            newx = sw - tw

        if newy <= 0:
            newy = 0
            # self.direction = Direction.down
        elif newy >= sh - th:
            newy = sh - th
            # self.direction = Direction.up


        self.x = newx
        self.y = newy


    def show(self, screen):
        """显示坦克"""
        screen.blit(self.image, (self.x, self.y))


    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction
        if direction == Direction.up:
            self.image = Tank.image_up
            self.x_speed = 0
            self.y_speed = -3
        elif direction == Direction.down:
            self.image = Tank.image_down
            self.x_speed = 0
            self.y_speed = 3
        elif direction == Direction.left:
            self.image = Tank.image_left
            self.x_speed = -3
            self.y_speed = 0
        elif direction == Direction.right:
            self.image = Tank.image_right
            self.x_speed = 3
            self.y_speed = 0





