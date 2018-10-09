# Filename  : 01-pygame.py
# Date  : 2018/7/27


import pygame
if __name__ == '__main__':
    # 1、初始化Pygame
    pygame.init()

    # 2、创建游戏窗口
    # set_mode（（宽度，高度）），里面为元组，单位是像素
    screen = pygame.display.set_mode((700, 900))

    # 3、游戏循环
    while True:
        # 检测事件
        for event in pygame.event.get():
            # 检测窗口上的关闭按钮是否被点击
            if event.type == pygame.QUIT:
                # 退出游戏
                print('关闭按钮被点击')
                exit()

        # 其他操作