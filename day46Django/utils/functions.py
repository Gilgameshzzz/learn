# Filename  : functions.py
# Date  : 2018/9/17
import random

from django.http import HttpResponseRedirect
from django.urls import reverse

from app.models import UserTicket


def get_ticket():
	s = 'sadafdwqffgfhytuyk432646'
	ticket = ''
	for i in range(25):
		ticket += random.choice(s)
	return ticket


def is_login(func):

	def check(request):
		ticket = request.COOKIES.get('ticket')
		# 如果cookie中存在设置的ticket则通过user_ticket表进行校验
		if ticket:
			# 通过user_ticket表获取对象
			user_ticket = UserTicket.objects.filter(ticket=ticket).first()
			if user_ticket:
				return func
			else:
				# ticket参数错误，则跳转到登录
				return HttpResponseRedirect(reverse('users:login'))
		else:
			# 没有ticket就说明没有登录
			return HttpResponseRedirect(reverse('users:login'))
	return check
