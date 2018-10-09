# Filename  : homework.py
# Date  : 2018/8/8
"""
注意：
1、想要结束一个进程就是让它里面的所有线程都结束，进程才会结束
2、想要关闭一个子线程，就是想方设法让子线程中的任务结束（就是让run方法结束）
3、如果一个线程崩溃（发生异常），不会影响其他线程
"""
"""
写一个服务器，可以和多个客户端同时通信，并且把接收到的消息显示在屏幕上
"""
import socket
import pygame
from threading import Thread
from random import randint
import time

class Massage:
    """处理不同的消息"""
    def __init__(self,text):
        self.color = randint(0,255),randint(0,255),randint(0,255)
        self.x = 0
        self.y = randint(0,500)
        self.text = text

class TalkAboutThread(Thread):
    """处理不同的客户端信息"""
    all_message =[]
    def __init__(self,talk:socket.socket):
        super().__init__()
        self.talk = talk

    def run(self):
        """让服务器和客户端一直保持通话"""
        while True:
            # 接收客户端发送的消息
            re_message = self.talk.recv(1024).decode(encoding ='utf-8')
            message = Massage(re_message)
            TalkAboutThread.all_message.append(message)


class TalkThread(Thread):
    def __init__(self,server:socket.socket):
        super().__init__()
        self.server = server

    def run(self):
        while True:
            talk, address = self.server.accept()
            t1 = TalkAboutThread()
            t1.start()


class Get_word():
    def pygame_word(self):
        pygame.init()
        screen = pygame.display.set_mode((300,600))
        screen.fill((255,255,255))
        font = pygame.font.Font('./aa.ttf', 25)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            # 获取每条信息，显示在屏幕上
            for message in TalkAboutThread.all_message[:]:
                surface = font.render(message.text,True,message.color)
                flag = True
                while flag:
                    time.sleep(0.1)
                    screen.fill((255, 255, 255))
                    screen.blit(surface, (Massage.x, Massage.y))
                    Massage.x += 5
                    if Massage.x > 450:
                        TalkAboutThread.all_message.remove(message)
                        flag = False
                    pygame.display.flip()


if __name__ == '__main__':
    server = socket.socket()
    server.bind(('10.7.181.83', 5555))
    server.listen(210)
    while True:

        c = TalkThread(server)
        c.start()

        get = Get_word()

        # get.pygame_word(message)

