# Filename  : settings.py
# Date  : 2018/11/21
import os

# 基础路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 静态路径
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# templates路径
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# media路径
MEDIA_DIR = os.path.join(STATIC_DIR, 'media')

# 上传路径
UPLOAD_DIR = os.path.join(MEDIA_DIR, 'upload')

# 房屋图片路径
HOUSE_DIR = os.path.join(MEDIA_DIR, 'house')

# 数据库配置
MYSQL_DATABASES = {
	'DRIVER': 'mysql',
	'DH': 'pymysql',
	'ROOT': 'root',
	'PASSWORD': 'qwer1234',
	'HOST': '127.0.0.1',
	'PORT': '3306',
	'NAME': 'flask9'
}


REDIS_DATABASES = {
	'HOST': '127.0.0.1',
	'PORT': 6379
}