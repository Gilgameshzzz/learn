# Filename  : battle-fly.py
# Date  : 2018/8/4
import pygame

Up = 273
Down = 274
Left = 276
Right = 275
import time


class Ship:
    def __init__(self, screen):
        """初始化飞船"""
        self.screen = screen
        """加载飞船图像并获取外接矩形"""
        image1 = pygame.image.load('./fly.jpg')
        image2 = pygame.transform.rotozoom(image1, 0, 0.1)
        self.image = image2


class Bullet:
    """子弹类"""
    all_bullet = []

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.speed = 6
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), 5)
        # screen.blit(bullet, (self.x, self.y))

    def move(self):
        self.y -= self.speed
        if self.y < -5:
            pass


def run_game():
    # 飞船初始化坐标
    x = 215
    y = 580
    # 飞船初始化速度
    yu_speed = 0
    yd_speed = 0
    xr_speed = 0
    xl_speed = 0
    # 初始化游戏屏幕
    pygame.init()
    screen = pygame.display.set_mode((480, 640))
    pygame.display.set_caption = 'Battle-Fly'
    # 创建飞船
    ship = Ship(screen)
    #  开始游戏主循环
    while True:
        pygame.time.delay(5)
        screen.fill((255, 255, 255))
        # 让绘制的屏幕可见
        pygame.display.flip()
        # 检测鼠标键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # 控制飞船移动
        if event.type == pygame.KEYDOWN:
            # 向上移动
            if event.key == Up:
                yu_speed = -1
            # 向下移动
            if event.key == Down:
                yd_speed = 1
            # 向右移动
            if event.key == Right:
                xr_speed = 1
            # 向左移动
            if event.key == Left:
                xl_speed = -1

        if event.type == pygame.KEYUP:
            # 键盘松开，飞船速度为0
            yu_speed = 0
            yd_speed = 0
            xr_speed = 0
            xl_speed = 0

        # 检测边界
        if x + 50 > 480:
            xr_speed = 0
        if x < 0:
            xl_speed = 0
        if y + 50 > 640:
            yd_speed = 0
        if y < 0:
            yu_speed = 0
        x += xr_speed
        x += xl_speed
        y += yu_speed
        y += yd_speed
        # 刷新屏幕
        screen.blit(ship.image, (x, y))
        bullet = Bullet(x + 26, y , screen)

        pygame.display.update()


if __name__ == '__main__':
    run_game()
