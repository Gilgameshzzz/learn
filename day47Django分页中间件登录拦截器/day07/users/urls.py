# Filename  : urls.py
# Date  : 2018/9/18
from django.conf.urls import url

from users import views

urlpatterns = [
	# 登录
	url(r'^login/', views.login, name='login'),

	url(r'^index/', views.index, name='index'),
	# 注销
	url(r'^logout',views.logout, name='logout')
]
