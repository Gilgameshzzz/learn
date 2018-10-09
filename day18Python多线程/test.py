# Filename  : test.py
# Date  : 2018/8/8
import pygame
from random import randint
from threading import Thread
import time
# pygame.init()
# screen = pygame.display.set_mode((400,600))
# screen.fill((255,255,255))

class Test(Thread):
    @classmethod
    def shuru(cls):
        print('开始输入')
        cls.message = input('输入')

# message_box =[]
# Test.shuru()
# message_box.append(Test.message)
# print(message_box)

class Get_word():
    def pygame_word(self,message):
        message_box = []
        message_box.append(message)
        pygame.init()
        screen = pygame.display.set_mode((300,600))
        screen.fill((255,255,255))
        font = pygame.font.Font('./aa.ttf', 15)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            for message1 in message_box:
                surface = font.render(message1,True,(randint(0,255),randint(0,255),randint(0,255)))
                flag = True
                x = 0
                y = randint(0, 500)
                while flag:
                    time.sleep(0.1)
                    screen.fill((255, 255, 255))
                    screen.blit(surface, (x, y))
                    x += 5
                    if x > 450:
                        message_box.remove(message1)
                        flag = False
                    pygame.display.flip()


if __name__ == '__main__':
    Test.shuru()
    get1 = Get_word()
    get1.pygame_word(Test.message)