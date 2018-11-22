# Filename  : app.py
# Date  : 2018/11/21
from flask import Flask

from baijiaxing.names_views import name
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
	app.register_blueprint(blueprint=name, url_prefix='/')

	# 配置
	app.config.from_object(Config)

	init_ext(app)

	return app