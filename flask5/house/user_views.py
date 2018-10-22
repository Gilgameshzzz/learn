# Filename  : user_views.py
# Date  : 2018/10/15
import os
import re

from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required, logout_user, LoginManager, login_user, current_user
from werkzeug.security import generate_password_hash

import status_code
from house.models import User, db
from utils.settings import UPLOAD_DIR

users = Blueprint('user', __name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)


@users.route('/register/', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')

	if request.method == 'POST':
		mobile = request.form.get('mobile')
		pwd_hash = request.form.get('pwd_hash')
		user = User.query.filter(User.phone == mobile).first()
		# 判断是否是手机号
		if not re.match(r'^1(?:3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8\d|9\d)\d{8}$', mobile):
			return jsonify(status_code.USER_REGISTER_MOBILE_INVALID)
		# 密码字符不得少于6个
		if len(pwd_hash) < 6:
			return jsonify(status_code.USER_REGISTER_PASSWORD_LESS)
		if user:
			return jsonify(status_code.USER_REGISTER_MOBILE_EXSIST)
		else:
			user = User()
			user.phone = mobile
			user.pwd_hash = generate_password_hash(pwd_hash)
			user.name = mobile
			user.add_update()
			return jsonify({'code': 200})


@users.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')

	if request.method == 'POST':
		mobile = request.form.get('mobile')
		paswd = request.form.get('password')
		user = User.query.filter(User.phone == mobile).first()
		if not all([mobile, paswd]):
			return jsonify(status_code.USER_LOGIN_PARAMS_VALID)
		if not re.match(r'^1(?:3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8\d|9\d)\d{8}$', mobile):
			return jsonify(status_code.USER_REGISTER_MOBILE_INVALID)
		if user:
			if user.check_pwd(paswd):
				# session['user_id'] = user.id
				login_user(user)
				return jsonify(status_code.SUCCESS)
			else:
				return jsonify(status_code.USER_LOGIN_PASSWORD_ERROR)
		else:
			return jsonify(status_code.USER_LOGIN_MOBILE_INVALID)


@users.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
	# 注销
	logout_user()
	return render_template('login.html')


@users.route('/auth/', methods=['GET', 'POST'])
@login_required
def auth():
	# 实名认证
	user = current_user
	if request.method == 'GET':
		return render_template('auth.html')

	if request.method == 'POST':
		id_name = request.form.get('real_name')
		id_card = request.form.get('id_card')
		if not all([id_name, id_card]):
			return jsonify(status_code.USER_LOGIN_INFO_VALID)
		re_card = r'^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'
		if re.match(re_card, id_card):
			user.id_name = id_name
			user.id_card = id_card
			user.add_update()
			user_info = user.to_auth_dict()
			return jsonify(code=status_code.SUCCESS, user=user_info)
		else:
			return jsonify(status_code.USER_AUTH_ID_ERRRE)


@users.route('/show_id/', methods=['GET'])
@login_required
def show_id():
	user = current_user.to_auth_dict()
	return jsonify(code=status_code.SUCCESS, user_id=user)


@users.route('/my/', methods=['GET', 'POST'])
@login_required
def my():
	if request.method == 'GET':
		return render_template('my.html')

	if request.method == 'POST':
		user = current_user.to_basic_dict()
		return jsonify(code=status_code.SUCCESS, user_info=user)


@users.route('/profile/', methods=['GET', 'PATCH', 'POST'])
@login_required
def profile():
	if request.method == 'GET':
		return render_template('profile.html')

	if request.method == 'PATCH':
		# 获取头像
		avatar = request.files.get('avatar')
		# 获取当前用户
		user = current_user
		photo = ['.jpg$', '.png$', '.bmp$']
		if avatar.filename:
			# 	判断是否为图片格式
			for p in photo:
				if re.search(p, avatar.filename):
					avatar.save(os.path.join(UPLOAD_DIR, avatar.filename))
					avatar_file = os.path.join('upload', avatar.filename)
					user.avatar = avatar_file
					user.add_update()
					return jsonify(code=status_code.SUCCESS, img=avatar_file)


@users.route('/change_name/', methods=['POST'])
@login_required
def change_name():
	new_name = request.form.get('name')
	user = User.query.filter(User.name == new_name).first()
	if user:
		return jsonify(code=1007)
	else:
		# 获取当前用户
		old = current_user
		old.name = new_name
		old.add_update()
		return jsonify(code=200, name=new_name)
