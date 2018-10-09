from _datetime import datetime, timedelta

from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, Permission, Group
# Create your views here.
from django.urls import reverse

from users.models import Users
from utils.functions import is_login


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')

	if request.method == 'POST':
		# 使用cookie +session形式实现登录
		username = request.POST.get('username')
		password = request.POST.get('password')

		# all() 校验参数里的元素是否有空的，有就返回false,没有就返回true
		if not all([username, password]):
			msg = '请填写完整的参数'
			return render(request, 'login.html', {'msg': msg})
		# 校验是否能通过username和password找到user对象
		user = Users.objects.filter(username=username).first()
		if user:
			if not check_password(password, user.password):
				msg = '密码错误'
				return render(request, 'login.html', {'msg': msg})
			else:
				# 	向cookie中设置，想user_ticket表中设置
				request.session['user_id'] = user.id
				# 设置session过期时间
				# request.session.set_expiry(600) 600秒后删除，若用下面这句需要将timedelta=4序列化
				request.session.set_expiry(timedelta(days=4))
				return HttpResponseRedirect(reverse('users:index'))
		else:
			msg = '用户名错误'
			return render(request, 'login.html', {'msg': msg})


@is_login
def index(request):
	if request.method == 'GET':
		user_id = request.session.get('user_id')
		return render(request, 'index.html')


@is_login
def logout(request):
	if request.method == 'GET':
		# 注销，删除session和cookie
		#  主要记下面这一句，数据库和浏览器都删除
		request.session.flush()
		# session_key = request.session.session_key     只能删除数据库
		# request.session.delete(session_key)
		return HttpResponseRedirect(reverse('users:login'))