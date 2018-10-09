from flask import Flask
from flask_script import Manager
from app.views import blue
app = Flask(__name__)


# 第二步， 绑定蓝图blue和app的关系
app.register_blueprint(blueprint=blue, url_prefix='/app')

# 设置secret_key
app.config['SECRET_KEY'] = '123'


# 将flask对象交给Manager管理，并且启动方式修改为manager.run()
manager = Manager(app=app)

# @app.route('/')
# def hello_world():
#     # 1/0
#     return 'Hello World!'

# 路由匹配规则
# 1. <id>: 默认接收的类型的str
# 2. <string:id>,指定id的类型为str
# 3. <int:id>, 指定id的类型为整型
# 4. <float:id>, 指定id的类型为浮点数
# 5. <path:path>, 指定接收的path为URL中的路径


# @app.route('/get_id/<id>/')
# def get_id(id):
#     # 匹配str类型的id值
#     return 'id: %s' % id
#
#
# @app.route('/get_int_id/<int:id>/')
# def get_int_id(id):
#     # 匹配int类型的id值
#     return 'id: %d' % id
#
#
# @app.route('/get_float/<float:uid>/')
# def get_float(uid):
#     # 匹配float类型的值，不能匹配int类型
#     return 'uid: %.2f' % uid
#
#
# @app.route('/get_path/<path:upath>/')
# def get_path(upath):
#     # 匹配URL路径
#     return 'path: %s' % upath


if __name__ == '__main__':
    # 修改启动的ip和端口, debug模式
    # app.run(host='0.0.0.0', port=8080, debug=True)

    # python xxx.py runserver -h 0.0.0.0 -p 8080 -d
    manager.run()
