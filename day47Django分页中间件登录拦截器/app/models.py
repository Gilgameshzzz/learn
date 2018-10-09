from django.db import models


# Create your models here.
class Users(models.Model):
	username = models.CharField(
		max_length=10,
		unique=True,
		verbose_name='姓名')
	password = models.CharField(max_length=255, verbose_name='密码')
	create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建是时间')
	operate_time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')
	icon = models.ImageField(upload_to='upload', null=True)

	class Meta:
		db_table = 'users'


class UserTicket(models.Model):
	user = models.ForeignKey(Users)
	ticket = models.CharField(max_length=30)
	create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建是时间')

	class Meta:
		db_table = 'user_ticekt'