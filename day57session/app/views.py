# Filename  : views.py
# Date  : 2018/10/9

from flask import Blueprint, redirect, url_for,\
	request, make_response, render_template, abort, session

from utils.function import is_login

blue = Blueprint('app', __name__)


@blue.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')

	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		# 校验用户名和密码，不能为空
		if not all([username, password]):
			return render_template('login.html')
		if username == 'coco' and password == '123123':
			session['login_status'] = 1
			return redirect(url_for('app.index'))
		else:
			return render_template('login.html')


@blue.route('/index/', methods=['GET'])
@is_login
def index():
	return render_template('index.html')


@blue.route('/scores/', methods=['GET'])
def scores():
	stu_scores = [80, 90, 54, 98, 50, 69]
	content = '<h2>hello python</h2>'
	return render_template(
		'scores.html',
	    stu_scores=stu_scores,
		content=content
		)

if __name__ == '__main__':
	pass