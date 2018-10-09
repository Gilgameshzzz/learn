# Filename  : 面向对象作业.py
# Date  : 2018/8/1
import json

try:
    with open('./new_staff.json', 'r', encoding='utf-8') as g:
        old_data = json.load(g)

except FileNotFoundError:
    with open('./new_staff.json', 'w', encoding='utf-8') as g:
        old_data = []
        json.dump(old_data, g)

def write():
    with open('./new_staff.json', 'w', encoding='utf-8') as g:
        json.dump(old_data, g)

class Staff:
    def __init__(self, name, age, id_num, money, job, department):
        self.name = name
        self._age = age
        self.id_num = id_num
        self._money = money
        self.job = job
        self.department = department

    def info(self):

        staff_info = {}
        staff_info['name'] = self.name
        staff_info['age'] = self._age
        staff_info['id_num'] = self.id_num
        staff_info['money'] = self._money
        staff_info['job'] = self.job
        staff_info['department'] = self.department
        old_data.append(staff_info)
        return old_data


class HR_manager:

    def add_staff(self):
        name = input('请输入员工的姓名：')
        while True:
            try:
                age = int(input('请输入员工年龄：'))
                break
            except ValueError:
                print('请输入大于0且小于150的纯数字')
        id_num = input('请输入员工工号：')
        while True:
            try:
                money = int(input('请输入员工薪资：'))
                break
            except ValueError:
                print('请输入大于0纯数字：')

        job = input('请输入员工职位：')
        department = input('请输入员工所在部门：')
        new_staff = Staff(name, age, id_num, money, job, department)
        a = new_staff.info()
        write()

    def del_staff(self, ):
        name = input('请输入要删除员工的姓名：')
        for x in old_data:
            if x['name'] == name:
                del x
                print('删除成功')
        else:
            print('没有该员工信息')
        write()

    def watch_staff(self):
        name = input('请输入员工姓名')
        for x in old_data:
            if x['name'] == name:
                print(x)
        else:
            print('没有该员工信息')

    def heighest_money(self):
        a = old_data[0]
        for x in old_data:
            if x['money'] > a['money']:
                a = x
        print('工资最高的员工信息：', a)

    def avg_money(self):
        depart = input('请输入指定的部门')
        for x in old_data:
            if x['department'] == depart:
                avg1 =[]
                avg1.append(x['money'])
        print('%s部门平均工资为%d' % (depart, sum(avg1)/int(len(avg1))))

    def avg_age(self):
        age1 = []
        for x in old_data:
            age1.append(x['age'])
        print('所有员工平均年龄为%d' % (sum(age1)/int(len(age1))))




if __name__ == '__main__':

    hr = HR_manager()
    hr.add_staff()

