# Filename  : 03-鼠标事件的应用.py
# Date  : 2018/7/30
# 要求：先在屏幕上显示一张图，鼠标按下移动的时候，拽着图片跟着一起动。鼠标弹起就不动
import pygame

# 写一个函数，判断 一个点是否在某个范围：
def is_in_rect(pos, rect):
    x, y = pos
    rx, ry, rw, rh = rect
    if (rx <= x <= rx+rw) and (ry <= y <= ry+rw):
        return True
    return False


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((232, 255, 255))
    pygame.display.set_caption('图片')

    # 显示图片
    image = pygame.image.load('./xx.jpg')
    image = pygame.transform.scale(image, (200, 200))
    image_x = 100
    image_y = 100
    screen.blit(image, (image_x, image_y))
    w, h = image.get_size()

    pygame.display.flip()

    # 用来存储图片是否可以移动
    is_move = False
    while True:
        for event in pygame.event.get():
            # 检测窗口上的关闭按钮是否被点击
            if event.type == pygame.QUIT:
                # 退出游戏
                print('关闭按钮被点击')
                exit()
            # 鼠标按下的时候，让状态变为可动
            if event.type == pygame.MOUSEBUTTONDOWN:

                if is_in_rect(event.pos, (image_x, image_y, w, h)):

                    is_move = True
            # 鼠标弹起的时候，状态变为不可动
            if event.type == pygame.MOUSEBUTTONUP:
                is_move = False

            # 鼠标移动对应的事件
            if event.type == pygame.MOUSEMOTION:
                if is_move:
                    screen.fill((255, 255, 255))   #  遮住前面的图
                    x, y = event.pos
                    image_x = x - h/2
                    image_y = y - w/2
                    image_w, image_h = image.get_size()
                    # 保证鼠标在图片的中心位置
                    screen.blit(image, (image_x, image_y))
                    pygame.display.update()

