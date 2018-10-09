"""__author__ = 余婷"""
import socket

if __name__ == '__main__':
    client = socket.socket()
    client.connect(('10.7.181.117', 8080))
    while True:
        print(client.recv(1024).decode(encoding='utf-8'))
        message = input('>>>')
        client.send(message.encode())
