# Filename  : models.py
# Date  : 2018/10/8
from manage import app


@app.route('/get_id/<id>/')
def get_id(id):
    # 匹配str类型的id值
    return 'id: %s' % id


@app.route('/get_int_id/<int:id>/')
def get_int_id(id):
    # 匹配int类型的id值
    return 'id: %d' % id


@app.route('/get_float/<float:uid>/')
def get_float(uid):
    # 匹配float类型的值，不能匹配int类型
    return 'uid: %.2f' % uid


@app.route('/get_path/<path:upath>/')
def get_path(upath):
    # 匹配URL路径
    return 'path: %s' % upath