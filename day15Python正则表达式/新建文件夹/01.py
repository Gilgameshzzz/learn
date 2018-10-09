"""__author__ = 余婷"""
import pygame


class Direction:
    UP = 273
    DOWN = 274
    RIGHT = 275
    LEFT = 276

class Bullet:
    """子弹类"""
    all_bullet = []
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 6
        self.image = './files/9.gif'
        self.is_show = True

    def show(self, screen):
        if self.is_show:
            image = pygame.image.load(self.image)
            screen.blit(image, (self.x, self.y))

    def move(self, screen):
        if self.direction == Direction.UP:
            self.y -= self.speed
            if self.y < -100:
                self.is_show = False
        elif self.direction == Direction.DOWN:
            self.y += self.speed
            if self.y > screen.get_size()[1]+100:
                self.is_show = False
        elif self.direction == Direction.LEFT:
            self.x -= self.speed
            if self.x < -100:
                self.is_show = False
        elif self.direction == Direction.RIGHT:
            self.x += self.speed
            if self.x > screen.get_size()[0]+100:
                self.is_show = False

    @classmethod
    def show_all(cls, screen):
        """显示所有的子弹"""
        index = 0
        while index < len(cls.all_bullet):
            bullet = cls.all_bullet[index]
            if not bullet.is_show:
                del cls.all_bullet[index]
                index -= 1
            else:
                bullet.show(screen)
            index += 1

    @classmethod
    def move_all(cls, screen):
        for bullet in cls.all_bullet:
            bullet.move(screen)









class Tank:
    """坦克类"""
    def __init__(self, x, y):
        self.image = ''
        self.x = x
        self.y = y
        self.speed = 5
        self.direction = Direction.UP
        self.size = (0, 0)

    # 移动
    def move(self):
        # 更新坦克的方向
        # self.direction = direction

        # 改变位置
        if self.direction == Direction.UP:
            self.y -= self.speed
        elif self.direction == Direction.DOWN:
            self.y += self.speed
        elif self.direction == Direction.RIGHT:
            self.x += self.speed
        elif self.direction == Direction.LEFT:
            self.x -= self.speed

    # 显示坦克
    def show(self, screen):
        # 1.确定坦克的图片
        image_file = ''
        if self.direction == Direction.UP:
            image_file = './files/p1tankU.gif'
        elif self.direction == Direction.DOWN:
            image_file = './files/p1tankD.gif'
        elif self.direction == Direction.RIGHT:
            image_file = './files/p1tankR.gif'
        elif self.direction == Direction.LEFT:
            image_file = './files/p1tankL.gif'
        # 2.创建图片对象
        image = pygame.image.load(image_file)
        self.size = image.get_size()
        # 3.将图片添加到窗口上
        screen.blit(image, (self.x, self.y))

    # 发射子弹
    def shout(self):
        # 根据坦克的方向设置子弹的位置
        x, y = 0, 0
        if self.direction == Direction.UP:
            x = self.x + self.size[0]/2 - 5
            y = self.y
        if self.direction == Direction.DOWN:
            x = self.x + self.size[0] / 2 - 5
            y = self.y + self.size[1]

        if self.direction == Direction.RIGHT:
            x = self.x + self.size[0]
            y = self.y + self.size[1]/2 - 5

        if self.direction == Direction.LEFT:
            x = self.x
            y = self.y + self.size[1] / 2 - 5
        bullet = Bullet(x, y, self.direction)
        Bullet.all_bullet.append(bullet)



def main():
    # 游戏初始化
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))
    tank = Tank(300, 200)
    tank.show(screen)
    is_move = False
    num = 0
    # 游戏循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == Direction.UP or event.key == Direction.DOWN \
                        or event.key == Direction.RIGHT or event.key == Direction.LEFT:
                    # 改变方向
                    tank.direction = event.key
                    is_move = True
                else:
                    print('其他')
            if event.type == pygame.KEYUP:
                if event.key == Direction.UP or event.key == Direction.DOWN \
                        or event.key == Direction.RIGHT or event.key == Direction.LEFT:
                    is_move = False



        pygame.time.delay(40)
        num += 1
        screen.fill((255, 255, 255))
        # 坦克移动
        if is_move:
            tank.move()
        tank.show(screen)

        # 隔一段时间发射一颗子弹
        if num == 10:
            tank.shout()
            num = 0

        # 子弹移动
        # Bullet.move(screen)
        Bullet.move_all(screen)
        Bullet.show_all(screen)

        pygame.display.flip()



if __name__ == '__main__':
    main()