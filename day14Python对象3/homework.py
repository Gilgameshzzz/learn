# Filename  : homework.py
# Date  : 2018/8/2


class Staff:
    def __init__(self, name, age, salary, job, department):
        self.name = name
        self.age = age
        self.id = ''
        self.salary = salary
        self.job = job
        self.department = department


class HrManager:
    """人力资源管理系统"""
    # 整个公司的所有员工
    all_staff = []

    # 目前公司已入职的员工
    __numers = 0

    __all_department = ['财务部', '行政部', '研发部', '总经办', '后勤部']

    @classmethod
    def add_staff(cls):
        # 添加员工功能
        name = input('名字：')
        age = int(input('年龄'))
        salary = int(input('薪资'))
        while True:
            print('公司部门：', *cls.__all_department)
            department = input('部门：')
            if department in cls.__all_department:
                break
            else:
                print('部门输入有误')
        job = input('职位：')

        # 生成工号
        cls.__numers += 1
        id = str(cls.__numers).rjust(4,'0')

        # 创建员工
        staff = Staff(name, age, salary, job, department)
        staff.id = id

        # 添加员工
        cls.all_staff.append(staff)

    @classmethod
    def del_staff(cls):
        """删除员工"""
        name = input('请输入要删除的员工姓名：')
        flag = False
        for staff in cls.all_staff:
            if staff.name == name:
                flag = True
                value = input('是否删除（Y/N）')
                if value == 'Y':
                    cls.all_staff.remove(staff)
                    print('删除成功')
        if not flag:
            print('公司没有该员工')

if __name__ == '__main__':
    pass