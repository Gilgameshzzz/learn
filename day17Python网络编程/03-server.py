# Filename  : 03-server.py
# Date  : 2018/8/7
import socket

if __name__ == '__main__':
    # 1、创建对象
    server = socket.socket()

    # 2、绑定地址
    server.bind(('10.7.181.83', 8088))

    # 3、监听
    server.listen(50)

    # 保持服务器不关闭
    while True:
        conversation,addr = server.accept()

        # 让客户端和服务器一直处于连接状态
        while True:
            # 发送消息
            message = input('>>>')
            conversation.send(message.encode())

            # 接收消息
            message_data = conversation.recv(1024)
            print(message_data.decode(encoding = 'utf-8'))