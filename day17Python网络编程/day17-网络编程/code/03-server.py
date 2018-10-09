"""__author__ = 余婷"""

import socket

if __name__ == '__main__':
    # 1.创建对象
    server = socket.socket()

    # 2.绑定地址
    server.bind(('10.7.181.117', 12345))

    # 3.监听
    server.listen(50)

    # 保持服务器不关闭
    while True:
        conversation, addr = server.accept()
        print(addr)

        # 让客户端和服务器一直处于连接的状态
        while True:
            # 发送消息
            message = input('>>>')
            conversation.send(message.encode())

            # 接收消息
            message_data = conversation.recv(1024)
            print(message_data.decode(encoding='utf-8'))

