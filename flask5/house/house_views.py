# Filename  : house_views.py
# Date  : 2018/10/13
import os

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

import status_code
from house.models import User, Area, Facility, House, HouseImage, Order
from house.user_views import login_manager
from utils.settings import HOUSE_DIR

house = Blueprint('house', __name__)


# @login_manager.user_loader()
# def load_user(user_id):
# 	return User.query.get(user_id)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)


@house.route('/index/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

	if request.method == 'POST':
		user = current_user
		if user:
			user = user.to_basic_dict()
		houses = House.query.all()
		house_list = [ahouse.to_dict() for ahouse in houses]
		return jsonify(code=200, user=user, house=house_list)


@house.route('/search/', methods=['GET'])
def search():
	if request.method == 'GET':
		return render_template('search.html')


@house.route('/house_search/', methods=['GET'])
def search_house():
	area_id = request.args.get('aid')
	sd = request.args.get('sd')
	ed = request.args.get('ed')
	sk = request.args.get('sk')

	# 过滤区域信息
	house = House.query.filter(House.area_id != area_id)
	# 过滤登录用户发布房屋信息
	if current_user:
		house_list = house.filter(House.user_id != current_user.id)

	# 查询不满足条件的房屋id
	order1 = Order.query.filter(Order.begin_date <= sd, Order.end_date >= ed)
	order2 = Order.query.filter(Order.begin_date <= sd, Order.end_date >= sd)
	order3 = Order.query.filter(Order.begin_date >= sd, Order.begin_date <= ed)
	order4 = Order.query.filter(Order.begin_date >= sd, Order.end_date <= ed)
	house_ids1 = [order.house_id for order in order1]
	house_ids2 = [order.house_id for order in order2]
	house_ids3 = [order.house_id for order in order3]
	house_ids4 = [order.house_id for order in order4]

	# 去重
	house_ids = list(set(house_ids1+house_ids2+house_ids3+house_ids4))
	# 最终展示房屋信息
	houses = house_list.filter(House.id.notin_(house_ids))
	if sk == 'booking':
		houses = house.order_by('order_count')
	elif sk == 'price-inc':
		houses = house.order_by('price')
	elif sk == 'price-des':
		houses = house.order_by('price')
	elif sk == 'new':
		houses = house.order_by('-price')
	else:
		# sk == 'new' 默认展示最新
		houses = house.order_by('-price')

	house_info = [ahouse.to_dict() for ahouse in houses]
	return jsonify(code=200, house_info=house_info)


@house.route('/myhouse/', methods=['GET', 'POST'])
@login_required
def myhouse():
	if request.method == 'GET':
		return render_template('myhouse.html')


@house.route('/myhouse_info/', methods=['GET'])
@login_required
def myhouse_info():
	# 获取当前登录用户
	user = current_user
	# 字典形式表示信息
	user_dict = user.to_auth_dict()
	id_name = user_dict['id_name']
	# 获取房屋信息，并以字典形式表示
	house_info = House.query.filter(House.user_id == user.id).all()
	house_list = [info.to_dict() for info in house_info]
	return jsonify(house_info=house_list, code=status_code.SUCCESS['code'], id_name=id_name)


@house.route('/newhouse/', methods=['GET', 'POST'])
@login_required
def newhouse():
	if request.method == 'GET':
		return render_template('newhouse.html')

	if request.method == 'POST':
		# 把表格数据存入字典
		data = {}
		# 循环遍历表格数据的name
		for item in request.form:
			if item != 'facility':
				# 存入字典
				data[item] = request.form.get(item)
				# 如果没有填写数据，就发生提示信息
				if not data[item]:
					return jsonify(status_code.USER_LOGIN_INFO_VALID)
		# 存入数据库
		ahouse = House(**data)
		# 获取当前登录用户，并把数据存入对应的用户
		ahouse.user_id = current_user.id
		# 获取facility数据，由于有多个name=checkbox，所以用getlist方法，把facility存入一个列表
		for item in request.form.getlist('facility'):
			# 循环遍历列表从Facility表格获取对应的item信息，并把item信息赋值于f
			f = Facility.query.get(item)
			# 可能会有多个f, 所以以列表形式存入House表
			ahouse.facilities.append(f)
		ahouse.add_update()
		return jsonify(code=status_code.SUCCESS['code'], house_id=ahouse.id)


@house.route('/image/', methods=['PATCH'])
@login_required
# 创建房屋图片
def image():
	house_id = request.form.get('house_id')
	house_img = request.files.get('house_image')
	# 保存图片 保存地址为 xxx/static/media/house/xx.jpg
	house_img.save(os.path.join(HOUSE_DIR, house_img.filename))
	# 保存图片和用户房屋信息
	house_img_info = HouseImage()
	# 保存图片地址和存入表格HouseImage中
	img_url = os.path.join('house', house_img.filename)
	house_img_info.url = img_url
	house_img_info.house_id = house_id
	house_img_info.add_update()
	houses = House.query.get(house_id)
	# 判断房屋首页展示是否有图,没有就保存
	if not houses.index_image_url:
		houses.index_image_url = img_url
		houses.add_update()
		imgs = [img_url]
		return jsonify(code=status_code.SUCCESS['code'], imgs=imgs)
	else:
		imgs = HouseImage.query.filter(HouseImage.house_id == house_id).all()
		img = [img.url for img in imgs]
		houses.add_update()
		return jsonify(code=status_code.SUCCESS['code'], imgs=img)


@house.route('/new/', methods=['GET'])
@login_required
# 返回下拉框和多选框数据
def new_info():
	areas = Area.query.all()
	# 生成一个房屋所在区的列表
	house_area = [area.name for area in areas]
	# 生成配套设施的列表
	facility = [facilities.name for facilities in Facility.query.all()]
	return jsonify(code=status_code.SUCCESS['code'], house_area=house_area, facility=facility)


@house.route('/detail/', methods=['GET', 'POST'])
def detail():
	return render_template('detail.html')


@house.route('/detail/<int:id>/', methods=['GET'])
def house_detail(id):
	house_info = House.query.get(id)
	# 用户自己的房源不能自己预定
	if current_user.id == house_info.user_id:
		return jsonify(code=200, house_detail=house_info.to_full_dict(), flag=1)
	else:
		return jsonify(code=200, house_detail=house_info.to_full_dict(), flag=0)