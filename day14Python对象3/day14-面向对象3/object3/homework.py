"""__author__ = 余婷"""


class Staff:
    """员工类"""
    def __init__(self, name, age, salary, job, department):
        self.name = name
        self.age = age
        self.id = ''
        self.salary = salary
        self.job = job
        self.department = department

    def show_info(self):
        print('姓名:%s 工号:%s 部门:%s 职位:%s' % (self.name, self.id, self.department, self.job))

    def __add__(self, other):
        return self.age + other.age

class HrManager:
    """人力资源管理系统"""
    # 整个公司的所有的员工
    all_staff = []

    # 目前公司已经入职的人数
    __numers = 0


    __all_department = ['财务部', '行政部', '研发部', '总经办','后勤部']

    @classmethod
    def add_staff(cls):
        """添加员工"""
        name = input('名字:')
        age = int(input('年龄:'))
        salary = int(input('薪资:'))
        while True:
            print('公司部门:', *cls.__all_department)
            department = input('部门:')
            if department in cls.__all_department:
                break
            else:
                print('部门输入有误')
        job = input('职位:')

        # 生成工号
        cls.__numers += 1
        id = str(cls.__numers).rjust(4, '0')

        # 创建员工对象
        staff = Staff(name, age, salary, job, department)
        staff.id = id

        # 添加员工
        cls.all_staff.append(staff)

    @classmethod
    def del_staff(cls):
        """删除员工"""
        name = input('请输入要删除的员工姓名:')
        flag = False
        for staff in cls.all_staff[:]:
            if staff.name == name:
                flag = True
                staff.show_info()
                value = input('是否删除(Y/N):')
                if value == 'Y':
                    cls.all_staff.remove(staff)
                    print('删除成功!')
        if not flag:
            print('公司没有该员工!')

    @classmethod
    def find_staff(cls):
        name = input('请输入要查找的员工姓名:')
        flag = False
        for staff in cls.all_staff:
            if staff.name == name:
                flag = True
                staff.show_info()

        if not flag:
            print('公司没有该员工!')

    @classmethod
    def get_most_rich(cls):
        if len(cls.all_staff) == 0:
            print('公司还没有员工!')
            return

        max_staff = cls.all_staff[0]
        for staff in cls.all_staff:
            if staff.salary > max_staff.salary:
                max_staff = staff
        print('薪资最高是:%s %d' % (max_staff.name, max_staff.salary))

    @classmethod
    def average_age(cls):
        """获取公司员工的平均年龄"""
        if len(cls.all_staff) == 0:
            print('公司还没有员工!')
            return
        return sum(cls.all_staff)/len(cls.all_staff)







if __name__ == '__main__':

    HrManager.add_staff()
    HrManager.add_staff()
    HrManager.add_staff()
    HrManager.del_staff()