# Filename  : 03-显示图片.py
# Date  : 2018/7/27

import pygame
pygame.init()
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill((232, 255, 164))

    # 1、获取图片对象
    image = pygame.image.load('./font/xx.jpg')
    """
    a、获取图片大小
    get_size()
    """
    image_size = image.get_size()
    print(image_size)

    """
    b、形变：
    transform：形变包含缩放，旋转，平移
    scale(缩放对象，新的大小)--->返回一个缩放后的对象
    """
    # image = pygame.transform.scale(image, (200, 200))

    """
    旋转
    rotate(旋转对象，旋转角度) ----角度是0-360对应的度数
    """
    # image = pygame.transform.rotate(image, -60)

    """
    旋转缩放
    rotozoom(旋转对象，旋转角度，缩放比例)
    """
    image = pygame.transform.rotozoom(image, 0, 1.5)


    # 2、将图片对象渲染到窗口上
    screen.blit(image, (0, 0))
    # 3、展示在屏幕上
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

