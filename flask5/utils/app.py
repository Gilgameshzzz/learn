# Filename  : app.py
# Date  : 2018/10/18
from flask import Flask

from house.house_views import house
from house.order_views import order
from house.user_views import users, login_manager
from utils.config import Config
from utils.functions import init_ext
from utils.settings import STATIC_DIR, TEMPLATES_DIR


def create_app():
	app = Flask(
		__name__,
		static_folder=STATIC_DIR,
		template_folder=TEMPLATES_DIR
	)
	# 注册蓝图
	app.register_blueprint(blueprint=house, url_prefix='/house')
	app.register_blueprint(blueprint=users, url_prefix='/user')
	app.register_blueprint(blueprint=order, url_prefix='/order')

	# 配置
	app.config.from_object(Config)

	init_ext(app)

	return app
