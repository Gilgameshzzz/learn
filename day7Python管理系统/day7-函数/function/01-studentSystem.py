"""__author__ = 余婷"""

"""
1.分析数据结构
学生管理系统管理学生----> 管理的是多个学生 ----> 需要容器存储学生 ---> 考虑使用哪种容器
--->列表？字典？---> 系统对应的大的容器是字典 ---> 字典中的某一个key对应的值是所有的学生(用了表作为容器)
--->每一个学生是一个字典
{'students':[学生1， 学生2， 学生3....]}

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
    # ============显示主页==============
    print('===========================')
    print('   欢迎进入XXX学生管理系统')
    print('1.添加学生\n2.查看学生信息\n3.删除学生\n4.修改学生信息\n0.退出')
    print('===========================')
    input_value = input('请选择:')

    # ============退出系统==============
    if input_value == '0':
        break
    # ============添加学生==============
    if input_value == '1':
        while True:
            print('==添加学生==')
            # 输入信息
            add_name = input('姓名:')
            add_age = input('年龄:')
            add_tel = input('电话:')
            # 产生学号
            number += 1
            add_id = 'py1805' + str(number).rjust(3, '0')

            # 创建学生(一个学生就是一个字典)
            add_student = {key_name: add_name, key_age: add_age, key_tel: add_tel, key_id: add_id}

            # 获取存学生的容器
            all_students = system_info.get(key_all_student)
            if all_students == None:
                all_students = []
            # 将学生添加到容器中
            all_students.append(add_student)
            system_info[key_all_student] = all_students
            print('添加学生 %s 成功' % add_name)
            # print(system_info)

            # 给出选择
            print('1.继续添加\n其他:返回上一层')
            add_input = input('>>>')
            if add_input != '1':
                break
        continue

    # ============查看学生==============
    if input_value == '2':
        """给出选择"""
        print('=查看学生=')
        print('1.查看所有的学生信息')
        print('2.根据姓名查看学生信息')
        print('3.根据学号查看学生信息')
        print('4.返回上一层')
        find_input = input('请输入(1,2,3,4):')

        # 直接回到上一层
        if find_input == '4':
            continue

        #  先看有没有学生
        """拿到所有的学生"""
        all_students = system_info.get(key_all_student)

        """系统还没有添加过学生"""
        """
        or和and的短路操作:
            表达式1 or 表达式2：如果表达式1的值是True，那么不会执行表达式2，结果直接为True
            表达式1 and 表达式2：如果表达式1的值是False,那么不会执行表达式2，结果直接是False
            None []
        """
        if (not all_students) or (not len(all_students)):
            print('系统中还没有学生!!')
            continue

        # ==查看所有==
        if find_input == '1':

            """有学生的时候"""
            for student in all_students:
                print('姓名:%s,年龄:%s,电话:%s,学号:%s' % \
                      (student[key_name], student[key_age], student[key_tel], student[key_id]))

        # ==根据姓名找
        elif find_input == '2':
            find_name = input('请输入要查看的学生的名字:')
            flag = True  # 表示是否找不到
            for student in all_students:
                # 如果学生的名字和输入的名字相同，就打印这个学生的信息
                if find_name == student[key_name]:
                    print(student)
                    flag = False
            if flag:
                print('找不到该学生信息!')

        # ==根据学号找
        elif find_input == '3':
            find_id = input('请输入要查看的学生的学号:')
            flag = True
            for student in all_students:
                if find_id == student[key_id]:
                    print(student)
                    flag = False
                    break
            if flag:
                print('找不到该学生信息!')

        continue

    # ============删除学生==============
    if input_value == '3':
        while True:
            print('1.按姓名删除')
            print('2.按学号删除')
            print('3.返回')
            del_input = input('请输入(1,2,3):')
            if del_input == '3':
                break

            # 把所有的学生拎出来
            all_students = system_info.get(key_all_student)
            if (not all_students) or (not len(all_students)):
                print('该系统没有学生!')
                break

            if del_input == '1':
                del_name = input('输入要删除的学生的姓名:')
                del_students = []
                # 找到所有可能要删除的学生
                for student in all_students:
                    if del_name == student[key_name]:
                        # 保存可能要删除的学生
                        del_students.append(student)

                # 判断是否找到
                if not len(del_students):
                    print('没有找到相关的学生信息!')
                    continue
                # 打印所有可能需要删除的学生
                index = 0
                for student in del_students:
                    print(index, student)
                    index += 1

                del_num = input('请选择要删除的学生的编号:')
                del_student = del_students[int(del_num)]
                # 从系统中删除这个学生
                system_info[key_all_student].remove(del_student)
                print('删除成功!')






        continue

    # ============修改信息==============
    if input_value == '4':
        print('修改信息')
        continue