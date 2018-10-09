#  1、显示界面
"""
学生管理系统管理学生--->管理的是多个学生--->需要容器存储学生--->
考虑使用哪种容器--->列表？字典？--->系统对应的大的容器是字典
--->字典中的某一个key对应的值是所有的学生（用了表作为容器）
--->每一个学生是一个字典
{'students':[学生1，学生2，学生3...]}
"""
# 声明所有的key值
key_all_student = 'students'  # 所有学生
key_name = 'student_name'
key_age = 'age'
key_tel = 'tel'
key_id = 'id'

# 系统容器
system_info = {}
# 当前已经添加过的学生人数
number = 0

# 系统入口
while True:
    # ======显示主页======
    print('==========')
    print('欢迎进入XXX学生管理系统')
    print('1.添加学生\n2.查看学生信息\n3.删除学生信息\n4.修改学生信息\n0.退出系统')
    print('==========')
    input_value = input('请选择： ')

    # ======退出系统======
    if input_value == '0':
        break

    # ======添加学生======
    if input_value == '1':
        while True:
            print('==添加学生==')
            # 输入信息
            add_name = input('姓名：')
            add_age = input('年龄：')
            add_tel = input('电话：')
            # 产生学号
            number += 1
            add_id = 'py1805' + str(number).rjust(3, '0')

            # 创建学生（一个学生就是一个字典）
            add_student = {key_name: add_name, key_age: add_age, key_tel: add_tel, key_id: add_id}

            # 获取存学生的容器
            all_students = system_info.get(key_all_student)
            if not all_students:
                all_students = []
            #  将学生添加到容器中
            all_students.append(add_student)
            system_info[key_all_student] = all_students
            print('添加学生 %s 成功' % add_name)
            print(system_info)

            # 给出选择
            print('1.继续添加学生\n其他：返回上一层')
            add_input = input('>>>')
            if add_input != '1':
                break
        continue

    # ======查看学生======
    if input_value == '2':
        """给出选择"""
        print('===查看学生===')
        print('1.查看所有的学生信息')
        print('2.根据姓名查看学生信息')
        print('3.根据学号查看学生信息')
        print('4.返回上一层')
        find_input = input('>>>')

        #  直接返回上一层
        if find_input == '4':
            continue

        # 先看有没有学生
        all_students = system_info.get(key_all_student)

        """系统还没有添加学生"""
        """or 和 and 的短路操作"""
        if (not all_students) or (not len(all_students)):
            print('系统还没有学生！！')
            continue

        # ==查看所有==
        if find_input == '1':

            """有学生的时候"""
            for student in all_students:
                print('姓名:%s, 年龄：%s, 电话：%s, 学号：%s '% \
                      (student[key_name], student[key_age], student[key_tel], student[key_id]))

        elif find_input == '2':
            pass
        elif find_input == '3':
            pass


        continue

    # ======删除学生======
    if input_value == '3':
        while True:
            print('1.按姓名删除')
            print('2.按学号删除')
            print('3.返回')
            del_input = input('请输入(1,2,3):')
            if del_input == '3':
                break

        #  把所有的学生拎出来
        all_students = system_info.get(key_all_student)


        continue

    # ======修改信息======
    if input_value == '4':
        print('修改学生')
        continue

