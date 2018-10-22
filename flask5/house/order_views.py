# Filename  : order_views.py
# Date  : 2018/10/15
from datetime import datetime

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

from house.models import User, House, Order
from house.user_views import login_manager

order = Blueprint('order', __name__)


# 学习前端传后端数据 ：https://blog.csdn.net/kikaylee/article/details/54885250


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)


@order.route('/order/', methods=['GET', 'POST'])
@login_required
def my_order():
	if request.method == 'GET':
		return render_template('orders.html')

	if request.method == 'POST':
		# 创建订单模型
		# 1. 获取开始和结束的时间 strftime strptime
		start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d')
		end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
		# 获取房屋信息和用户信息
		house_id = request.form.get('house_id')
		user = current_user
		house_info = House.query.get(house_id)

		# 将订单提交到数据库
		order = Order()
		order.user_id = user.id
		order.house_id = house_id
		order.begin_date = start_date
		order.end_date = end_date
		# 将日期差的结果转换为数字
		order.days = (end_date - start_date).days + 1
		order.house_price = house_info.price
		order.amount = house_info.price * order.days
		order.add_update()
		return jsonify(code=200)


@order.route('/show_order/', methods=['GET'])
@login_required
def show_info():
	# 展示登录用户下的订单详情
	user = current_user.id
	user_orders = Order.query.filter(Order.user_id == user)
	user_order = [aorder.to_dict() for aorder in user_orders]
	return jsonify(code=200, user_order=user_order)


@order.route('/lorders/', methods=['GET', 'POST'])
def customer_orders():
	if request.method == 'GET':
		return render_template('lorders.html')


@order.route('/booking/', methods=['GET'])
@login_required
def booking():
	return render_template('booking.html')


@order.route('/booking/<int:id>/', methods=['GET'])
@login_required
def book(id):
	house_info = House.query.get(id)
	house_info = house_info.to_dict()
	return jsonify(code=200, house_info=house_info)


@order.route('/my_order/', methods=['GET'])
@login_required
# 登录用户的房源被下单信息
def owner_order():
	owner_id = current_user.id
	# 获取登录用户房屋信息
	owner_houses = House.query.filter(House.user_id == owner_id)
	order_house_list = []
	# 获取有登录 用户的房屋被下单的订单
	for owner_house in owner_houses:
		if Order.query.filter_by(house_id=owner_house.id):
			order_info = Order.query.filter_by(house_id=owner_house.id).first()
			order_house_list.append(order_info.to_dict())
	return jsonify(code=200, order_house=order_house_list)


@order.route('/order_status/', methods=['POST'])
# 获取订单是否接单或拒单
def accept_order():
	order_id = request.form.get('order_id')
	order = Order.query.get(order_id)
	order.status = request.form.get('status')
	comment = request.form.get('comment')
	# 拒单原因
	if comment:
		order.comment = comment
	order.add_update()
	return jsonify(code=200)