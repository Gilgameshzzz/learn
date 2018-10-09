"""__author__ = 余婷"""
import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))

    """
    1.画直线
    line(Surface, color, start_pos, end_pos, width=1)
    Surface -> 画在哪个地方
    color -> 线的颜色
    start_pos -> 起点
    end_pos -> 终点
    width -> 线的宽度
    """
    pygame.draw.line(screen, (255, 0, 0), (78, 59), (100, 100), 2)
    pygame.draw.line(screen, (0, 255, 0), (0, 0), (130, 100), 2)

    """
    lines(画线的位置, 颜色, closed, 点的列表, width=1)
    """
    pygame.draw.lines(screen, (0, 0, 255), True, [(10, 10), (200, 50), (100, 100)])


    """
    画矩形
    rect(位置，颜色，(x,y,width,height))
    """
    pygame.draw.rect(screen,(255,255,0),(0,0,200,200),2)

    """
    2.画曲线
    arc(Surface, color, Rect, start_angle, stop_angle, width=1)
    Rect -> (x, y, width, height)矩形
    start_angle
    stop_angle
    """
    from math import pi
    pygame.draw.arc(screen, (0, 0, 0), (0, 0, 100, 200), pi+pi/4, pi*2-pi/4)


    """
    3.画圆
    circle(位置, 颜色, 圆心位置, 半径, width=0)
    """
    import random
    pygame.draw.circle(screen,\
            (random.randint(0,255),random.randint(0,255),random.randint(0,255)),\
            (400,200),100)

    """
    画椭圆
    ellipse(Surface, color, Rect, width=0)
    """
    pygame.draw.ellipse(screen, (0, 100, 0), (100, 300, 200, 80), 1)



    # 将内容展示在屏幕上
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()