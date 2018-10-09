import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='dudu', charset='utf8')
cursor = db.cursor()

'''
# 准备sql语句
obj = {'name': '李云龙', 'money': '20', 'province': '河南', 'age': 36, 'sex': '男'}
# 注意，这里的引号需要加
sql = 'insert into star(name, money, province, age, sex) values("%s", "%s", "%s", "%s", "%s")' % (obj['name'], obj['money'], obj['province'], obj['age'], obj['sex'])
'''

# id = 8
# sql = 'delete from star where id=%s' % id

sql = 'update star set name="马德华" where id=12'

# 注意，没有添加进去，是因为没有提交，需要提交才能成功
try:
    cursor.execute(sql)
    # 提交，写入磁盘
    db.commit()
except Exception as e:
    print(e)
    # 回滚到最初始的状态
    db.rollback()
finally:
    cursor.close()
    db.close()
