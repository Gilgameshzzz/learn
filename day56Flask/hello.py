# Filename  : hello.py
# Date  : 2018/10/8
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
# 将flask对象交给Manager管理，并且启动方式修改为manager.run()
manager = Manager(app=app)


@app.route('/')
def hello_world():
	return 'Hello World!'


# 路由匹配规则
# 1、<id>:，默认接收的类型为str
# 2、<string:id>,指定id类型为str
# 3、<int:id>，指定id类型为整型
# 4、<float:id>，指定id类型为浮点数
# 5、<path:path>，指定接收path为URL中的路径

@app.route('/get_id/<id>/')
def get_id(id):
	# 返回str类型的id值
	return 'id: %s' % id


@app.route('/get_int_id/<int:id>/')
def get_int_id(id):
	# 匹配int类型的id值
	return 'id: %d' % id


@app.route('/get_float/<float:uid>/')
def get_float(uid):
	# 匹配float类型的值，不能匹配int类型
	return 'float: %.2f' % uid


@app.route('/get_path/<path:upath>/')
def get_path(upath):
	# 匹配float类型的值，不能匹配int类型
	return 'path:%s' % upath


if __name__ == '__main__':
	# 修改启动ip和端口
	# app.run(host='0.0.0.0', port=8080, debug=True)不推荐
	# python xx.py runserver -h 0.0.0.0 -p 8080
	manager.run()