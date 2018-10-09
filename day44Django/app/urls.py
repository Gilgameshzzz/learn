# Filename  : urls.py
# Date  : 2018/9/13
from django.conf.urls import url

from app import views

urlpatterns = [
	# url第一个参数是正则表达式
	url(r'^stu/', views.index, name='index'),
	# url(r'^del_stu/(\d+)/', views.del_stu, name='del_stu')
	url(r'^del_stu/(?P<s_id>\d+)/', views.del_stu, name='del_stu'),
	url(r'look_stu_info/(?P<s_info>\d+)/', views.look_stu_info, name='look_stu_info')
]
