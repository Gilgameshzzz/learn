from django.shortcuts import render
from rest_framework import viewsets, mixins
# Create your views here.
from apps.models import Student
from apps.serializers import StudentSerializer


class StudentView(
	mixins.ListModelMixin,
	viewsets.GenericViewSet,
	mixins.CreateModelMixin,
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
):
	# 返回数据
	queryset = Student.objects.all()
	# queryset = Student.objects.all().filter(is_delete=0) 假删除
	# 序列化结果
	serializer_class = StudentSerializer
	# 过滤
	filter_class = ''
	# def perform_destroy(self, instance):
	# 假删除
	# def perform_destroy(self, instance):
	# 	instance.is_delete = 1
	# 	instance.save()
	# def get_queryset(self):
	# 	获取学生对象数据
	# 	queryset = self.queryset
	# 	返回过滤的学生结果
	# 	return queryset.filter(s_name__contains='达到')


def index(request):
	if request.method == 'GET':
		return render(request, 'index.html')


def add(request):
	if request.method == 'GET':
		return render(request, 'add.html')


def update(request):
	if request.method == 'GET':
		return render(request, 'update.html')
