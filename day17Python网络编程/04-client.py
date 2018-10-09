# Filename  : 04-client.py
# Date  : 2018/8/7
import socket
if __name__ == '__main__':
    # 1、创建套接字对象
    client = socket.socket()

    # 2、连接服务器
    client.connect(('10.7.181.59', 8088))

    while True:
        # 接收消息
        data = client.recv(1024)
        print(data.decode(encoding = 'utf-8'))
        # 发送消息
        message = input('>>>')
        client.send(message.encode(encoding='utf-8'))
