# Filename  : 02-显示文字.py
# Date  : 2018/7/27
import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    # 设置窗口的背景颜色
    screen.fill((255, 255, 100))
    # 1、创建字体对象
    """
    创建系统字体
    SysFont(name, size, bold=False, italic=False, constructor=None)
    name ->字体名
    size ->字体大小
    bold ->加粗
    italic->倾斜
    """

    """
    创建自定义字体
    Font(字体文件路径，字体大小)
    """
    font = pygame.font.Font('./font/aa.ttf', 35)
    # 2、根据字体去创建显示对象（文字）(找内容)
    """
    render(self, text, antialias, color, background=None):
    text ->要显示的文字内容（str）
    antialias -> 是否平滑
    color ->计算机三原色（红、绿、蓝）RGB颜色，值范围是0-255
    (0, 0, 0)-->黑色
    (255,0,0)-->红色
    (0,0,255)-->蓝色
    (x,x,x)--->灰色
    """
    surface = font.render('Cannot write Chinese', True, (0, 255, 0))

    # 3、将内容添加到窗口上（画在纸上）
    """
    blit(需要显示的对象，显示位置)
    需要显示的对象-->Surface类型的数据
    显示位置-->坐标（x, y）
    """
    screen.blit(surface, (0, 100))

   #  4、将窗口的内容展示出来
    pygame.display.flip()


   # 游戏循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()