from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from app.models import Student


def index(request):
	if request.method == 'GET':
		stus = Student.objects.all()

		return render(request, 'stus.html', {'students': stus})


def del_stu(request, s_id):
	if request.method == 'GET':
		# 删除方法
		# 1、获取URL中的id值
		# id = request.GET.get('id')
		# 2、获取id对应的学生对象
		stu = Student.objects.get(pk=s_id)
		# 3、对象.delete()
		stu.delete()
		return HttpResponseRedirect(reverse('app:index'))


# return HttpResponseRedirect('/app/stu/')


def look_stu_info(request, s_info):
	if request.method == 'GET':

		re1 = "<a href='http://127.0.0.1:8087/app/stu/'>返回</a"
		stu1 = Student.objects.get(pk=s_info)
		info = ['姓名：', stu1.s_name, '<br>', '年龄：', stu1.s_age, '<br>', '性别：', stu1.s_sex,
				'<br>', '语文成绩：', stu1.chinese, '<br>',
				'数学成绩：', stu1.math, '<br>', '住址：', stu1.stu_info.address, '<br>',
				'电话：', stu1.stu_info.phone, '<br>', '课程：', stu1.g.g_name, '<br>', re1
				]

		return HttpResponse(info)
