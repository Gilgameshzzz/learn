# Filename  : 05-http.py
# Date  : 2018/8/7
"""
服务器：（python）\java\php等等

HTTP(为了可以让客户端和服务器能够进行有效的数据交流)
超文本传输协议，访问的是远程的网络资源，格式是http://


客户端：网页（js）、IOS设备上的软件（OC/Swift）、安卓设备上的软件（java）
URL：统一资源定位符
通过一个URL，能找到互联网上唯一的1个资源
URL的基本格式 = 协议://主机地址/路径
协议:不同的协议，代表着不同的资源查找方式、资源传输方式
主机地址：存放资源的主机（服务器）中的具体位置
路径：资源在主机（服务器）中的具体位置

"""
"""
python中访问网络中的数据：第三方库 request
"""
from requests import request
if __name__ == '__main__':
    # https://www.apiopen.top/satinApi?type=1&page=1
    # get请求：参数以?号的形式拼接到url地址后面，参数名 = 值的形式，多个参数用&隔开
    # 1、确定url
    url = 'https://www.apiopen.top/satinApi?type=1&page=1'

    # 2、发送请求
    response = request('GET', url)
    print(type(response), response)

    # 1、以字符串的形式获取响应体（服务器返回的数据）
    text = response.text
    print(type(text),text)

    # 2、以json的形式获取响应体
    json = response.json()
    print(type(json), json)

    # 3.以二进制的形式获取响应体
    content = response.content
    print(type(content), content)