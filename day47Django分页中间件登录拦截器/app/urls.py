# Filename  : urls.py
# Date  : 2018/9/17
from django.conf.urls import url

from app import views

urlpatterns = [
	# 注册
	url(r'^register/', views.register, name='register'),
	# 	登录
	url(r'^login/', views.login, name='login'),
	# 	首页
	url(r'^index/', views.index, name='index'),
	# 	用户管理
	url(r'^users/', views.users, name='users')
]
