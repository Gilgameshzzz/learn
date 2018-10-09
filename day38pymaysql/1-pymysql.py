import pymysql

# 第一步，连接数据库，类似于指令里面的  mysql -uroot -p
# mysql -h地址 -uroot -p
'''
连接数据库需要用到的参数
主机：host
端口：port
用户名：user
密码：password
指定数据库：db
指定字符集：charset
'''
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='dudu', charset='utf8')
# 连接成功之后，得到一个对象
# print(db)
# 首先根据db得到游标，游标就是执行sql语句用到的东西
# cursor = db.cursor()

# 给cursor添加一个参数，让其的到数据是一个字典
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
# 准备sql语句，执行sql语句
sql = 'select * from star'
# 返回结果rows是受影响的行数
rows = cursor.execute(sql)
# print(rows)
# 通过cursor的方法得到数据
# 返回一个元组，元组里面每个元素的值对应的就是数据表中每个字段对应的值
# 获取内容的时候，里面有个迭代器在记录你的位置
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchmany(5))
# print(cursor.fetchmany(5))

# 元组里面套元组
# print(cursor.fetchall())

# 打印得到所有的用户名
ret = cursor.fetchall()
for obj in ret:
    print('我叫%s,我来自%s,我有%s￥' % (obj['name'], obj['province'], obj['money']))
# print(ret)
# 遍历每一个元组
# for tp in ret:
#     print(tp[1])

# 最后呀，要记得关闭
cursor.close()
db.close()