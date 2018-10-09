from django.contrib import admin

# Register your models here.
from apps.models import Student, CarName


class StudentAdmin(admin.ModelAdmin):
    # 修改管理后台展示列表的字段
    list_display = ('id','s_name','s_age')
    # 过滤
    list_filter = ['s_age']
    #搜索
    search_fields = ['s_name']
    #分页,例：每页显示2个
    list_per_page = 2

admin.site.register(Student,StudentAdmin)
admin.site.register(CarName)