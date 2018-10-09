# Filename  : entry.py
# Date  : 2018/7/27
import json



count = 0
# 载入用户数据
with open('./user_name.json', encoding='utf-8') as f:
    name_data = json.load(f)
print(name_data)

# 载入学生信息
with open('./student_info.json', encoding='utf-8') as f:
    info_data = json.load(f)

load_name = ''  # 登录账户名
user_info = []  # 账户下学生信息
  # 要添加的学生信息
user_info = []   # 账户下的学生信息
   # 使用添加学生的次数，好编写学号
# 设置登录系统
def entry():
    while True:
        # 验证账户名是否存在
        global load_name
        load_name = input('请输入用户名：')
        for name in name_data:
            if load_name != name:
                print('用户名不存在，请重新输入！')
                continue
            else:
                # 验证输入的密码是否正确
                while True:
                    load_password = input('请输入密码：')
                    if load_password != str(name_data[load_name]):
                        print('密码错误，请重新输入！')
                    else:
                        print('登录成功! %s欢迎使用系统' % load_name)
                        return

def info_function():
    while True:
        print('1、查看学生\n2、添加学生\n3、删除学生')
        while True:
            int_choose = input('请选择')
            if int_choose != '1' and int_choose != '2' and int_choose != '3':
                print('输入有误，请重新输入！！')
            else:
                break

        # 打印账户名下所有学生信息
        if int_choose == '1':
            global user_info
            user_info = info_data[load_name]  # 将账户下的信息存入一个变量
            print(user_info)
            int1 = input('除回车键，按任意键返回上一层')

        # 添加学生信息
        if int_choose == '2':
            m = True
            while m:
                while True:
                    student_info = {}
                    # 将要存入的信息变成字典
                    student_name = input('请输入学生姓名：')
                    try:  # 判断输入信息是否符合格式要求
                        student_age = int(input('请输入学生年龄：'))
                    except ValueError:
                        print('年龄为纯数字且不能有字符，请重新输入学生信息')
                        continue
                    try:
                        student_tel = int(input('请输入学生电话号码：'))
                    except ValueError:
                        print('电话号码也只能为纯数字且不能有字符，请重新输入学生信息')
                        continue
                    student_info['name'] = student_name
                    student_info['age'] = student_age
                    student_info['tel'] = student_tel
                    print('要添加的学生信息', student_info, sep='')
                    print('执行判断', user_info)
                    print(student_info)
                    for x in user_info:
                        if x['name'] == student_info['name'] and x['age'] == student_info['age'] and x['tel'] == \
                                student_info['tel']:
                            print('该学生信息已存在，请重新输入！！')
                            break
                    #  count 计数没有起作用
                        else:
                            global count
                            count += 1  # 添加学生学号
                            print(count)
                            count_num = str(count)
                            count_num = count_num.rjust(3, '0')
                            id_num = 'py1234' + count_num
                            student_info['student_id'] = id_num
                            user_info.append(student_info)  # 将新建的学生信息存入账户学生信息下
                            print(user_info)
                            print('学生信息添加成功！')
                            with open('./student_info.json', 'w', encoding='utf-8') as g:
                                info_data[load_name] = user_info  # 将数据保存到json文件中
                                json.dump(info_data, g)
                        break
                    break


                print('1、继续添加学生\n2、返回上一层界面')
                shuru = input('选择:')
                if shuru == '2':
                    m = False
                    continue
                if shuru == '1':
                    continue

        # 删除学生信息
        if int_choose == '3':
            pass












if __name__ == '__main__':
    entry()
    info_function()