# Filename  : 坦克.py
# Date  : 2018/8/6
"""
1、通过键盘控制坦克上下左右移动
2、坦克发射子弹
3、出现敌机
4、敌机发射子弹，自由的动
"""
import pygame
from color import Color
from tank import Tank


def game():
    pygame.init()
    screen = pygame.display.set_mode((400, 500))
    screen.fill(Color.white)
    pygame.display.set_caption('坦克大战')

    pygame.display.flip()

    while True:
        # ========事件检测=========
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # =========游戏循环=========
        my_tank.show


if __name__ == '__main__':
    game()