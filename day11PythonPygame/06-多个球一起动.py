# Filename  : 06-多个球一起动.py
# Date  : 2018/7/30
import pygame
import random
import math
all_balls = []
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill((255, 255, 255))
    pygame.display.flip()

    # all_balls中保存多个球
    # 每个球要保存 ：半径、圆心坐标、颜色、x速度、y速度


    while True:
        pygame.time.delay(8)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #  点一下鼠标创建一个球
                ball = {
                    'r': random.randint(10, 20),
                    'pos': event.pos,
                    'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    'x_speed': random.randint(-3, 3),
                    'y_speed': random.randint(-3, 3)
                }
                # 保存球
                all_balls.append(ball)
        #  刷新界面
        screen.fill((255, 255, 255))
        for ball_dict in all_balls:
            # 取出球原来的X坐标和y坐标以及速度
            x, y = ball_dict['pos']
            x_speed = ball_dict['x_speed']
            y_speed = ball_dict['y_speed']
            x += x_speed
            y += y_speed
            if x + ball_dict['r'] >= 640:
                x = 640 - ball_dict['r']
                x_speed *= -1
            if x - ball_dict['r'] <= 0:
                x = 0 + ball_dict['r']
                x_speed *= -1
            if y - ball_dict['r'] <= 0:
                y = 0 + ball_dict['r']
                y_speed *= -1
            if y + ball_dict['r'] >= 480:
                y = 480 - ball_dict['r']
                y_speed *= -1
            pygame.draw.circle(screen, ball_dict['color'], (x, y), ball_dict['r'])
            # 更新球对应的坐标
            ball_dict['pos'] = x, y
            ball_dict['x_speed'] = x_speed
            ball_dict['y_speed'] = y_speed

        for ball_1 in all_balls:
            x1, y1 = ball_1['pos']
            for ball_2 in all_balls:
                x2, y2 = ball_2['pos']
                if ball_1 != ball_2:
                    if math.sqrt((x1 - x2)**2 + (y1 - y2)**2) < ball_1['r']+ball_2['r']:
                        if ball_2['r'] > ball_1['r']:
                            ball_2['r'] += ball_1['r']
                            all_balls.remove(ball_1)
                        else:
                            ball_1['r'] += ball_2['r']
                            all_balls.remove(ball_2)
        for ball in all_balls:
            if ball['r'] > 240:
                all_balls.remove(ball)



        pygame.display.update()