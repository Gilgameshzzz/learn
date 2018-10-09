# Filename  : 作业.py
# Date  : 2018/8/2


class Student:
    def __init__(self, name='', age=0, score1=0, score2=0, score3=0):
        score = {'语文': score1, '数学': score2, '英语': score3}
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        print('该生姓名：%s' % self.name)

    def get_age(self):
        print('该生年龄：%s' % self.age)

    def get_course(self):
        # ???????????
        max_score = max(self.score[k] for k in self.score)
        print(self.score.items(),  max_score)


# 第二题
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.brief = ''

    def descibe_user(self):
        print(self.first_name + ' '+self.last_name)

    def greet_user(self):
        print('早上好，%s %s' % (self.first_name, self.last_name))


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(*self.privileges)


if __name__ == '__main__':
    student = Student(score1=98, score2=100, score3=199)
    # admin = Admin('alan', 'PT')
    # admin.show_privileges()
    student.get_course()
