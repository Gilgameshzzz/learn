"""__author__ = 余婷"""

import socket
from threading import Thread


class CoversationThread(Thread):
    """在子线程中处理不同的客户端会话"""
    """
    python中可以在函数参数的后面加一个冒号，来对参数的类型进行说明
    """
    def __init__(self, conversation:socket.socket, address):
        super().__init__()
        self.conversation = conversation
        self.address = address

    def run(self):
        while True:
            self.conversation.send('你好!'.encode())
            print(self.address,self.conversation.recv(1024).decode(encoding='utf-8'))



if __name__ == '__main__':

    server = socket.socket()
    server.bind(('10.7.181.117', 8080))
    server.listen(512)

    while True:

        conversation, address = server.accept()
        t = CoversationThread(conversation, address)
        t.start()
        # while True:
        #     conversation.send('你好！'.encode())
        #     print(conversation.recv(1024).decode(encoding='utf-8'))
