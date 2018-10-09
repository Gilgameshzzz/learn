# Filename  : 05-ballGame.py
# Date  : 2018/7/30
import pygame

def draw_ball(place, color, pos):
    """
    画球
    """
    pygame.draw.circle(place, color, pos, 20)

# 方向对应的key值
Up = 273
Down = 274
Left = 276
Right = 275

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill((255, 255, 255))
    pygame.display.flip()

    # 保存初始坐标
    ball_x = 100
    ball_y = 100
    x_speed = 0
    y_speed = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if event.type == pygame.KEYDOWN:
            if event.key == Up:
                y_speed = -5
                x_speed = 0
            if event.key == Down:
                y_speed = 5
                x_speed = 0
            if event.key == Right:
                x_speed = 5
                y_speed = 0
            if event.key == Left:
                x_speed = -5
                y_speed = 0


        # 刷新屏幕
        screen.fill((255, 255, 255))
        pygame.time.delay(5)
        ball_x += x_speed
        ball_y += y_speed
        if ball_x + 20 >= 640:
            ball_x = 640 - 20
            x_speed *= -1
        if ball_x - 20 <= 0:
            ball_x = 0 + 20
            x_speed *= -1
        if ball_y - 20 <= 0:
            ball_y = 0 + 20
            y_speed *= -1
        if ball_y + 20 >= 480:
            ball_y = 480 - 20
            y_speed *= -1
        draw_ball(screen, (255, 0, 0), (ball_x, ball_y))
        pygame.display.update()