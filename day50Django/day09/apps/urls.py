# Filename  : urls.py
# Date  : 2018/9/20
from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from apps import views

# 引入路由
router = SimpleRouter()
# 使用router注册地址,不要加/
router.register(r'^student', views.StudentView)

urlpatterns = [
	url(r'^index/', views.index, name='index'),
	url(r'^add/', views.add, name='add'),
	url(r'^update/', views.update, name='update')
]
urlpatterns += router.urls