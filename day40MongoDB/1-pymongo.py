import pymongo

# 链接数据库
conn = pymongo.MongoClient(host='localhost', port=27017)
# 选择数据库
# db = conn['dudu']
db = conn.dudu
# 选择集合
col = db.star

# 插入数据
# col.insert({'name': '尹兰林', 'age': 26, 'gender': 1, 'height': 160})
# data = [
#         {'name': '流血', 'age': 29, 'gender': 0, 'height': 155}, {'name': '流泪', 'age': 23, 'gender': 1, 'height': 160},
#         {'name': '流汗', 'age': 22, 'gender': 1, 'height': 163},
#     ]
# ret = col.insert_many(data)
# print(ret.inserted_ids)

# ret = col.find()
import re
# ret = col.find({'address': re.compile(r'^新')})
# print(ret)
# ret = col.find().sort('age', -1).skip(2).limit(2)
# for obj in ret:
#     print(obj)

col.update_many({'gender': 1}, {'$inc': {'age': 1}})