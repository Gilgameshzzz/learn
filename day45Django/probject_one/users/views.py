from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from users.form import UserForm, UserLoginForm
from django.contrib import auth
# Create your views here.


def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')

	if request.method == 'POST':
		# 校验页面中传递的参数，是否填写完整
		form = UserForm(request.POST)
		# is_valid():判断表单是否验证通过
		if form.is_valid():
			# 获取校验后的用户名和密码
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			password2 = form.cleaned_data.get('password2')
			# 判断密码是否相同
			# if password == password2:
			# 创建普通用户create_user,创建超级用户create_superuser
			User.objects.create_user(username=username, password=password)
			# 实现跳转到登录界面
			return HttpResponseRedirect(reverse('user:login'))
			# else:
			# 	return render(request, 'register.html')
		else:
			return render(request, 'register.html', {'form': form})


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')

	if request.method == "POST":
		# 表单验证，用户名和密码是否填写，校验用户名是否注册
		form = UserLoginForm(request.POST)
		if form.is_valid():
			# 校验用户名和密码，判断返回的对象是否为空，如果不为空，则为user对象
			user = auth.authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password']
			)
			if user:
				# 	用户名和密码是正确的
				auth.login(request, user)
				return HttpResponseRedirect(reverse('user:index'))
			else:
				# 	密码不正确
				return render(request, 'login.html', {'errors': '密码错误'})
		else:
			return render(request, 'login.html', {'form': form})


def index(request):
	if request.method == 'GET':
		return render(request, 'index.html')


def logout(request):
	if request.method == 'GET':
		# 注销
		auth.logout(request)
		return HttpResponseRedirect(reverse('user:login'))


@login_required()
def myview(request):
	username = form
	return render_to_response('index.html', {'username': username})