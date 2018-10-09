sum_student_info = []
student_info = []
names = {}
student_id = {}
sum_scores = {}
scores = {}
ages = {}
#  系统运行
while True:
    #   系统界面选项
    print('欢迎进入学院管理系统')
    print('1、添加学生')
    print('2、查看学生')
    print('3、删除学生')
    print('4、查看学生成绩和平均成绩')
    print('q、退出系统')
    choose = input()
    if choose == 'q':
        break
    elif choose == '1':
        while True:
            """" 输入学生信息"""
            names['姓名'] = input('请输入学生姓名')
            student_id['学号'] = input('请输入学生学号')
            scores['英语'] = int(input('请输入学生英语成绩'))
            scores['体育'] = int(input('请输入学生体育成绩'))
            scores['美术'] = int(input('请输入学生美术成绩'))
            scores['数学'] = int(input('请输入学生数学成绩'))
            ages['年龄'] = int(input('请输入学生年龄'))
            sum_scores['成绩'] = scores
            student_info.append(names)
            student_info.append(student_id)
            student_info.append(sum_scores)
            student_info.append(ages)
            sum_student_info.append(student_info)
            #  添加完成
            print('1、继续添加')
            print('2、返回上一层')
            choose = input()
            if choose == '2':
                break
    elif choose == '2':  # 查看学生信息功能

        print('请输入学生姓名')
        student_name = input()
        for i in range(len(sum_student_info)):
            if student_name == sum_student_info[i][0]['姓名']:
                print(sum_student_info[i])
        else:
            print('没有该学生')
    elif choose == '3':   # 删除学生信息功能

        print('请输入学生姓名')
        student_name = input()
        for i in range(len(sum_student_info)):
            if student_name == sum_student_info[i][0]['姓名']:
                del sum_student_info[i]
                print('删除成功')
        else:
            print('没有该学生')
    elif choose == '4':  # 查看学生成绩功能
        print('请输入学生姓名： ')
