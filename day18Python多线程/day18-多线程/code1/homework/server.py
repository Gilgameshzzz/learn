"""__author__ = 余婷"""
import socket
import requests
import re

if __name__ == '__main__':
    server = socket.socket()
    server.bind(('10.7.181.117', 8080))
    server.listen(512)

    while True:
        cover, addr = server.accept()

        while True:
            message = input('我:')
            cover.send(message.encode())

            message_re = cover.recv(1024).decode(encoding='utf-8')
            # 1.如果是'拜拜'
            if message_re == '拜拜':
                cover.close()
                break
            # http://122.2323.232.23/
            elif re.fullmatch(r'http://(\w+\.){2}(\w+)/[\w?=&%@/\.]+ ', message_re):
                print('是网址')
                match = re.search(r'(\.png|\.jpg|\.gif|\.jpeg|\.ico) $', message_re)

                # 如果是图片
                if match:
                    # 返回的是服务器的响应
                    response = requests.request('GET',message_re)
                    # 获取服务器返回的响应头
                    print(response.headers)
                    # 获取响应体的二进制
                    content = response.content
                    with open('./image'+match.group(), 'wb') as f:
                        f.write(content)
                else:
                    response = requests.request('GET', message_re)
                    txt = response.text
                    with open('./text', 'a', encoding='utf-8'):
                        f.write(txt)

            else:
                print(message_re)



