# manage.py作为启动文件
from flask_script import Manager

from utils.app import create_app


app = create_app()

# 使用Manager管理app
manager = Manager(app=app)

if __name__ == '__main__':
	manager.run()
