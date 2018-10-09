from django.db import models
from django.contrib.auth.models import User, Group, Permission, AbstractUser
# Create your models here.


class MyUser (AbstractUser):
	"""
	自定义Django自带的user模型
	"""
	id_delete = models.BooleanField(default=0, verbose_name='是否删除')

	class Meta:
		# (第一个为权限名称，第二个为描述字段)
		permissions = (
			('change_myuser_username', '修改用户名'),
			('change_myuser_password', '修改密码'),
		)