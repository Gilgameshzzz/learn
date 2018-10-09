import redis

# 连接redis数据库
'''
host : 主机
port : 端口号
db : 数据库
password : 密码
'''
r = redis.StrictRedis(host='localhost', port=6379)

# 使用r来进行操作你的redis服务器
# r.set('name', 'maodan')
# value = r.get('name')
# print(value)

# ret = r.hmset('ming', {'name': 'goudan', 'age': 30, 'height': 180})
# print(ret)

# ret = r.lpush('nba', '科比妻子', '斯嘉丽', '金卡戴珊', '科勒卡戴珊')
# print(ret)
# value = r.lpop('nba')

# print(value.decode('utf8'))

# ret = r.sadd('star', '郭德纲', '姜昆', '冯巩', '牛群', '郭德纲', '冯巩')

# ret = r.zadd('class', 100, '毛主席', 90, '蒋介石', 101, '孙中山', 0, '溥仪', -250, '慈禧老娘们')
# print(ret)
# ret = r.zrevrange('class', 0, -1, True)
# 返回的是一个列表，列表里面都是元组，元组第一个元素是成员，第二个元素是分值
# print(ret)

# ret = r.keys('*')
# print(ret)

# print(r.exists('girl'))
