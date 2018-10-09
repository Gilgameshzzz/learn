# Filename  : 03-多线程应用.py
# Date  : 2018/8/8
import socket
from threading import Thread

class ConversationThread(Thread):
    """在子线程中处理不同的客户端会话"""
    """
    python中可以在函数参数后面加个冒号，来对参数的类型进行说明
    """
    def __init__(self,conversation:socket.socket,address):
        super().__init__()
        self.conversation = conversation
        self.address = address
    def run(self):
        while True:
            self.conversation.send('daqwe'.encode())
            print(self.address,self.conversation.recv(1024).decode(encoding = 'utf-8'))


if __name__ == '__main__':
    server =socket.socket()
    server.bind(('10.7.181.117',8080))
    server.listen(210)
    while True:
        conversation, address = server.accept()
        t=ConversationThread(conversation,address)
        print(conversation.recv(1024).decode(encoding = 'utf-8'))
