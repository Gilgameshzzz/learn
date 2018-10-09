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
	# 序列化结果
	serializer_class = StudentSerializer

	# def perform_destroy(self, instance):
