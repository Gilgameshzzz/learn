import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='dudu', charset='utf8')
# print(db)
cursor = db.cursor()
sql = 'select * from start'

# 查询语句，通过try-except，让代码更加健壮
try:
    ret = cursor.execute(sql)
    print(cursor.fetchall())
except Exception as e:
    print(e)
finally:
    cursor.close()
    db.close()