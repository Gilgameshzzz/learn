"""__author__ = 余婷"""
import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))

    # 1.获取图片对象
    image = pygame.image.load('./images/luffy.jpeg')

    """
    a.获取图片大小
    get_size()
    """
    image_size = image.get_size()
    print(image_size)

    """
    b.形变：
    transform：形变包含缩放、旋转和平移
    
    scale(缩放对象,新的大小) --> 返回一个缩放后的新对象
    """
    # image = pygame.transform.scale(image, (150, 150))

    """
    旋转
    rotate(旋转对象, 旋转角度) --- 角度是0-360对应的度数
    """
    image = pygame.transform.rotate(image, -90)

    """
    def rotozoom(旋转对象, 旋转角度, 缩放比例)
    """
    image = pygame.transform.rotozoom(image, 90, 0.4)

    # 2.将图片对象渲染到窗口上
    screen.blit(image, (0, 0))
    # screen.blit(image,(60, 60))
    # 3.展示在屏幕上
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()