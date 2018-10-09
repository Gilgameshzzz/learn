"""__author__ = 余婷"""
import socket

if __name__ == '__main__':
    client = socket.socket()
    client.connect(('10.7.181.117', 8081))

    # 接收数据，因为图片数据较大，可能会分多次发送
    image_data = bytes()  # 创建一个空的bytes用来保存整个图片数据
    data = client.recv(1024)
    while data:
        image_data += data
        data = client.recv(1024)

    # 保存图片到本地
    with open('./image.png', 'wb') as f:
        f.write(image_data)

    client.close()