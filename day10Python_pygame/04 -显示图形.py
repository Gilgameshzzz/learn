# Filename  : 04 -显示图形.py
# Date  : 2018/7/27

import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((666, 555))
    screen.fill((123, 123, 223))

    """
    1、画直线
    line(Surface, color, start_pos, end_pos, width=1)
    Surface -> 画在哪个地方
    color ->线的颜色
    start_pos ->起点
    end_pos ->终点
    width -> 线的宽度
    """
    pygame.draw.line(screen, (0, 0, 255), (120, 124), (200, 433), 10)
    pygame.draw.line(screen, (0, 222, 255), (10, 124), (200, 433), 20)

    """
    lines(画线的地方，颜色，closed（是否封闭），坐标点的列表，width=1)
    """
    pygame.draw.lines(screen, (0, 123, 234), True, [(29, 150), (200, 250), (3, 400)], 10)

    """
    2、画曲线
    arc(Surface, color, Rect, start_angle, stop_angle, width=1)
    Rect ->(x, y, width, height)矩形
    star_angle
    stop_angle
    """
    from math import pi
    pygame.draw.arc(screen, (0,0,0),(100,100,300,300),pi/2,pi,30)

    """
    3、画图
    circle(位置，颜色，圆心位置，半径，with=0)
    """
    pygame.draw.circle(screen,(0, 34, 100),(200,200),100, 40)

    """
    画椭圆
    ellipse(Surface,color,rect,width=0)
    """
    pygame.draw.ellipse(screen,(130,79,90),(22,33,400,222),20)
    # 将内容展示在屏幕上
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()