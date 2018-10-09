import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session
from app.views import blue

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/app')


# session配置
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

# 获取session对象，并初始化app
se = Session()
se.init_app(app)

# 将flask对象交给Manager管理，并且启动方式修改为manager.run()
manager = Manager(app=app)


@app.route('/')
def hello_world():
	return 'Hello World!'


if __name__ == '__main__':
	manager.run()
