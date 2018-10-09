"""__author__ = 余婷"""
"""
socket编程(套接字): 指的就是通过代码来创建实现通信的两个端(服务器和客户端)
socket一般可以基于TCP和UDP实现客户端和服务器之间的可靠传输和不可靠传输

python中的内置模块socket可以支持socket编程
"""

import socket

# 通过socket实现服务器端

if __name__ == '__main__':
    # 1. 创建服务器套接字对象
    """
    family：确定服务类型 
            AF_INET --> ipv4
            AF_INET6 --> ipv6
            
    type：确定传输协议类型
        SOCK_STREAM -> TCP协议
        SOCK_DGRAM -> UDP协议 
    """
    # server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server = socket.socket()

    # 2. 绑定ip地址和端口
    """
    地址格式:(ip地址字符串, 端口号)
    端口号是用来区分一个计算机中不同的服务,范围是0-65535；
    注意：1.其中0-1024是'著名端口'用来绑定一些特殊的服务的，一般不使用。
         2.同一时间一个端口只能绑定一个服务
    """
    server.bind(('10.7.181.117', 8081))

    # 3. 监听
    """
    参数：用来限制一次性能够接受的客服端请求数量
    """
    server.listen(50)
    print('开始监听请求')

    # 保证服务器处于一直启动的状态
    while True:
        # 4. 接收客户端的请求
        """
        accept()会阻塞线程，当有客户端给这个服务器发送请求，才会开始执行
        """
        client, addr = server.accept()
        print(addr)

        # 5.给客户端发送消息
        """
        send(数据)：数据必须是二进制数据(bytes)类型
        
        字符串转二进制：
        bytes(字符串,encoding=编码方式)
        字符串.encode(encoding=编码方式)
        """
        client.send('HTTP/1.1 200 OK\r\n\r\n'.encode(encoding='utf-8'))
        client.send(bytes('hello', encoding='utf-8'))
        client.send('python'.encode())

        # 接收从客户端发来的消息
        """
        bufsize：设置缓存大小（单位是字节）
        1024字节 -> 1k
        1024k -> 1M
        1024M -> 1G
        1024G -> 1T
        1024T - 1P
        
        二进制(bytes)转换字符串：
        a. str(二进制数据, encoding='utf-8')
        b. 二进制数据.decode(encoding='utf-8')
         """
        # data = client.recv(1024)
        # str1 = str(data, encoding='utf-8')
        # str2 = data.decode(encoding='utf-8')
        # print(str1)

        # 6.关闭连接
        client.close()





