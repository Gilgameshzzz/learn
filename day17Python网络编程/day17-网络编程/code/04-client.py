"""__author__ = 余婷"""
import socket
if __name__ == '__main__':
    # 1.创建套接字对象
    client = socket.socket()

    # 2.连接服务器
    client.connect(('10.7.181.117', 12345))

    while True:
        # 接收消息
        data = client.recv(1024)
        print(data.decode(encoding='utf-8'))

        # 发送消息
        message = input('>>>')
        client.send(message.encode())
