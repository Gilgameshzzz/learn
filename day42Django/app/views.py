from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Student, StudentInfo, Grade, Course


# Create your views here.


def create_stu(request):
    # 创建学生信息
    # 引入ORM概念：对象关系映射
    # 第一种方式
    Student.objects.create(s_name='卫宫')
    # 第二种
    stu=Student()
    stu.s_name='远斑'
    stu.save()
    # 第三种
    stu = Student('樱',18,1)
    stu.save()
    return HttpResponse('创建学生方法')


def select_stu(request):
    """
    all:所有
    filter:获取的结果为queryset,可以返回空，
    get
    1、django的get方法是从数据库的取得一个匹配的结果，返回一个对象，如果记录不存在的话，它会报错。
    2、2如果你用django的get去取得关联表的数据的话，而关键表的数据如果多于2条的话也会报错。
    filter
    1、django的filter方法是从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]。
    2、如果你用django的filter去取得关联表的数据的话，无论关联表有多少记录的都不会报错。
    """
    # 查询数据
    # select * from app_student;
    stus = Student.objects.all()
    # select * from xxx where s_name='小花'
    stus = Student.objects.filter(s_name='小花')
    # filter(): 查询年龄等于19的学生
    stus = Student.objects.filter(s_age=19)
    # get(): 查询年龄等于19的学生
    # stus = Student.objects.get(s_age=18)
    # 年龄等于19, 姓名等于小花
    stus = Student.objects.filter(s_age=19, s_name='小花')

    # # 排序按照id升序/降序 ---》asc/desc
    stus = Student.objects.all().order_by('id')
    stus = Student.objects.all().order_by('-id')
    # # 查询姓名不为小花的  exclude:不包含
    stus = Student.objects.exclude(s_name='小花')

    # values()
    stus=Student.objects.all().values('id','s_name','s_age')

    # 切片，[a:b],如果b超过下标，即从a开始一直取完
    # 如果a超过索引范围，则返回一个空列表[]（不会报错）
    stus = Student.objects.all().order_by('-id')[10:]

    # 查询名字带花的信息select * from xxx where name like '%花%'
    stus = Student.objects.filter(s_name__contains='花')
    # 查询名字以花开头的信息select * from xxx where name like '花%'
    stus = Student.objects.filter(s_name__startswith='花')
    # 查询名字以花结尾的信息select * from xxx where name like '%花'
    stus = Student.objects.filter(s_name__endswith='花')

    # Q(),查询姓名叫小花的,或者年龄等于18的
    stus = Student.objects.filter(Q(s_name='小花') | Q(s_age=18))

    # 获取学生的姓名
    # for stu in stus:
    #     print(stus.s_name)
    # stu_names = [(stu.s_name,stu.id) for stu in stus]
    # print(stu_names)
    return HttpResponse(stus)


def delete_stu(request):
    # 删除
    # stu=Student.objects.get(pk=1)
    stu=Student.objects.filter(pk=(1,2,3,4)).first()
    stu.delete()
    return HttpResponse('删除')


def update_stu(request):
    # 更新
    # 第一种
    stu = Student.objects.get(id=1)
    stu.s_name = "侍郎"
    stu.save()
    # 第二种
    # Student.objects.filter(id=1).update(s_name='切嗣')
    # return HttpResponse('修改')


def create_stu_info(request):
    if request.method == 'GET':
        s = 0
        for a in range(5):
            num = str(18200384770 + s)
            num1 = '金牛区' + str(s)
            s +=10
            StudentInfo.objects.create(phone=num,address=num1)
        return  HttpResponse('创建')

    if request.method=='POST':
        pass


def stu_add_stuinfo(request):
    if request.method =="GET":
        # #给id为1的学生绑定stu_info_id
        # stu = Student.objects.filter(id=1)
        # #绑定关系一
        # # stu.stu_info_id = 2
        # #绑定关系二
        # stu.stu_info= StudentInfo.objects.filter(id=2).first()
        # stu.save()
        num = 1
        for i in range(5):
            stu = Student.objects.get(id=num)
            stu.stu_info = StudentInfo.objects.get(id=num)
            stu.save()
            num+=1
        return HttpResponse('绑定成功')


def sel_phone_by_stu(request):
    if request.method =='GET':
        #获取学生的手机号
        #方法1、
        stu = Student.objects.filter(id = 1).first()
        info_id = stu.stu_info_id
        stu_info = StudentInfo.objects.get(pk=info_id)
        phone= stu_info.phone
        #方法2、
        stu= Student.objects.get(id=1)
        stu_info= stu.stu_info
        phone= stu_info.phone
        return HttpResponse('查找学生手机号')

def sel_stu_by_phone(request):
    if request.method =='GET':
        stu_info = Student
        pass


def create_grade(request):
    if request.method == 'GET':
        #创建班级
        grade_name=['Python','Java','Php','VHDL']
        for i in grade_name:
            Grade.objects.create(g_name=i)
        return HttpResponse('创建成功')

def sel_stu_by_grade(request):
    if request.method =="GET":
        # 查询叫杀死给的学生对应的班级名称
        stu = Student.objects.get(s_name = '杀死给')
        g_name = stu.g.g_name

        #查询java班级下有多少学生，获取学生的姓名
        grade = Grade.objects.filter(g_name='Java').first()
        stus = grade.student_set.all()

        return HttpResponse(g_name)

def create_course(request):
    if request.method =='GET':
        course_name=['math','English','Chinese','Computer','PE']
        for i in course_name:
            Course.objects.create(c_name=i)
        return HttpResponse('创建课程')


def create_stu_course(request):
    if request.method=='GET':
        # 添加学生
        stu = Student.objects.get(id=2)
        # 添加add方法
        stu.c.add(2)
        # 添加math和id=4的学生关联
        cou = Course.objects.get(c_name = 'math')
        # 添加add（）
        cou.student_set.add(4)
        # 删除id=2的学生选的id=2的课程
        stu.c.remove(2)