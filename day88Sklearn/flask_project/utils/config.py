# Filename  : config.py
# Date  : 2018/11/21
from utils.functions import get_mysqldb_url


class Config():
	# 配置数据库
	SQLALCHEMY_DATABASE_URI = get_mysqldb_url()
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'secret_keyqwzxvb07328945'
	# session的配置
	SESSION_TYPE = 'redis'

	# SESSION_REDIS = get_redisdb_url()

	# app.config['DEBUG_TB_INTERCEPT_REDIRECTS '] = False
	# app.config['SECRET_KEY'] =
	# app.config[''] = ''