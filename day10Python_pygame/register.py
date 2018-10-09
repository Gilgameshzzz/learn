# Filename  : register.py
# Date  : 2018/7/27
import json

# 用户注册
def register():
# 先读取已注册的用户数据
    old_data = {}  # 用于存储旧数据的容器
    with open('./user_name.json', encoding='utf-8')as f:
        old_data = json.load(f)
    #  设置用户名
    while True:
        new_user = input('请输入新的用户名：')
        for find_name in old_data:
            if new_user == find_name:
                print('用户名已存在，请重新输入！')
                break
        # else:       # 没有else会跳出？
        break

    # 设置密码
    while True:
        frist_password = input('请设置密码：')
        second_password = input('请再次输入密码')
        if frist_password != second_password:
            print('两次输入的密码不同，请重新设置密码！')
        else:
            print('注册成功！')
            break

    # 保存注册好的账号
    old_data[new_user] = frist_password

    with open('./user_name.json', 'w', encoding='utf-8')as g:
        json.dump(old_data, g)

if __name__ == '__main__':
    register()