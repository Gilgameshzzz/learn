"""__author__ = 余婷"""
import socket

if __name__ == '__main__':
    server = socket.socket()
    server.bind(('10.7.181.117', 8081))
    server.listen(10)

    while True:
        conversation, addr = server.accept()
        print(addr)

        # 发送一张图片
        with open('./luffy2.png', 'rb') as f:
            data = f.read()
        conversation.send(data)


        conversation.close()
