# Filename  : middlwrare.py
# Date  : 2018/9/19
import logging
import time

from django.utils.deprecation import MiddlewareMixin

from users.models import MyUser


class UerAuthMiddlwrare(MiddlewareMixin):
	def process_request(self, request):
		user = MyUser.objects.get(username='admin')
		request.user = user
		return None


class logMIddleware(MiddlewareMixin):
	# url到服务器的时候，经过中间件最先执行的方法
	def process_request(self, request):
		request.init_time = time.time()
		request.init_body = request.body

	# 经过中间件，最后执行的方法
	def process_response(self, request, response):
		count_time = (time.time() - request.init_time)*1000
		code = response.status_code
		req_body = request.init_body
		res_body = response.content
		# 获取logger
		logger = logging.getLogger(__name__)
		msg = '%s %s %s %s' % (count_time, code, req_body, res_body)
		logger.info(msg)
		return response