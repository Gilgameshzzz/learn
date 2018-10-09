# Filename  : 03-client.py
# Date  : 2018/8/8
import socket
# 客户端
if __name__ == '__main__':
    client = socket.socket()
    client.connect(('10.7.181.83', 5555))

    while True:
        # 接收服务器返回信息
        print(client.recv(1024).decode(encoding = 'utf-8'))
        # 发送消息
        message = input('>>>')
        client.send(message.encode())
