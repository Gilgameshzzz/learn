# Filename  : 学生管理系统.py
# Date  : 2018/7/27
import json
import register
# 判断数据文件是否存在,不存在就创建
try:
    with open('./user_name.json', encoding='utf-8') as f:
        name_data = json.load(f)
except FileNotFoundError:
    with open('./user_name.json', 'w', encoding='utf-8') as f:
        name_data = {}
        json.dump(name_data, f)

try:
    with open('./student_info.json', encoding='utf-8') as f:
        info_data = json.load(f)
except FileNotFoundError:
    with open('./student_info.json', 'w', encoding='utf-8') as f:
        info_data = {}
        json.dump(info_data, f)

# 打印系统界面
while True:
    print('===========================')
    print('   欢迎进入学生管理系统')
    print('1.注册用户\n2.登录系统\n3.退出系统')
    print('===========================')
    # 判断输入的是否符合规范
    while True:
        int_choose = input('请选择')
        if int_choose != '1' and int_choose != '2' and int_choose != '3':
            print('输入有误，请重新输入！！')
        else:
            break
    # 退出系统
    if int_choose == '3':
        break

    # 注册用户
    if int_choose == '1':
        while True:
            register.register()
            print('1、继续注册新用户')
            print('2、返回上一层')
            while True:
                int_order = input('请选择')
                if int_order != '1' and int_order != '2':
                    print('输入有误，请重新输入！！')
                else:
                    break
            if int_order == '2':
                break

    # 登录系统
    if int_choose == '2':
        pass





# if __name__ == '__main__':
#     pass