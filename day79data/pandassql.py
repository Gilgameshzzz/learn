import pandas as pd
from sqlalchemy import create_engine

# pandas DataFrame数据传入mysql

result = array(['Animation', "Children's"])

a = pd.DataFrame(result, coulumns=['category'])

db = create_engine('mysql+pymysql://root:qwer1234@127.0.0.1:3306/diudiu?charset=utf8')

# genres 表名
pd.io.sql.to_sql(a['category'], 'genres', db, if_exists='append', index=False)

#或者 a.to_sql('genres',   con=db, index=False,  if_exists='append')

#在MySQL中导入数据 
#先mysql --local-infile=1 -u root -p
#                                                                               文件地址                       表名          数据以什么分割               需要添加数据的字段
#输入密码后  LOAD DATA local INFILE 'F:\\python\\day79data\\datasets\\movielens\\ratings.dat' INTO TABLE ratings FIELDS TERMINATED BY '::'  ENCLOSED BY '"' LINES TERMINATED BY '\n' (UserID,MovieID,Rating,Timestamp);


