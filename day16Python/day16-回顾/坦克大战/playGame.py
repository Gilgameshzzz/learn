"""__author__ = 余婷"""

"""
1.通过键盘控制坦克上下左右移动
2.坦克发射子弹
3.出现敌机
4.敌机发射子弹，自由的动
"""

import pygame
from 坦克大战.color import Color
from 坦克大战.tank import Tank, Direction


def game():
    pygame.init()
    screen = pygame.display.set_mode((400, 500))
    screen.fill(Color.white)
    pygame.display.set_caption('坦克大战')

    my_tank = Tank((100, 100))


    pygame.display.flip()
    while True:
        # =============事件检测=============
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                my_tank.direction = event.key
                my_tank.is_move = True

            if event.type == pygame.KEYUP:
                my_tank.is_move = False


        # ============游戏循环==============
        screen.fill(Color.white)
        my_tank.move(screen)
        my_tank.show(screen)


        pygame.display.update()




if __name__ == '__main__':
    game()