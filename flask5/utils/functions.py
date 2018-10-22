# Filename  : functions.py
# Date  : 2018/10/18
import redis

from house.models import db
from house.user_views import login_manager
from utils.settings import MYSQL_DATABASES, REDIS_DATABASES


def init_ext(app):

	login_manager.login_view = 'user.login'
	login_manager.init_app(app)
	# 绑定app和db
	db.init_app(app)


def get_mysqldb_url():
	DRIVER = MYSQL_DATABASES['DRIVER']
	DH = MYSQL_DATABASES['DH']
	ROOT = MYSQL_DATABASES['ROOT']
	PASSWORD = MYSQL_DATABASES['PASSWORD']
	HOST = MYSQL_DATABASES['HOST']
	PORT = MYSQL_DATABASES['PORT']
	NAME = MYSQL_DATABASES['NAME']
	return '{}+{}://{}:{}@{}:{}/{}'.format(DRIVER, DH, ROOT, PASSWORD, HOST, PORT, NAME)


def get_redisdb_url():
	host = REDIS_DATABASES['HOST']
	port = REDIS_DATABASES['PORT']
	return redis.Redis(host=host, port=port)