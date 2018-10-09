"""__author__ = 余婷"""
"""
0.定义一个学生类。有属性：姓名、年龄、成绩（语文，数学，英语)[每课成绩的类型为整数]
方法： a. 获取学生的姓名：getname() b. 获取学生的年龄：getage()
c. 返回3门科目中最高的分数。get_course()
"""

class Score:
    """成绩类"""
    def __init__(self,chinese=0, math=0, english=0):
        self.chinese = chinese
        self.math = math
        self.english = english


class Student:
    """学生类"""
    def __init__(self, name='', age=0):
        self.name = name
        self.score = None
        self.age = age

    def get_name(self):
        """获取学生名字"""
        return self.name

    def get_age(self):
        """获取学生年龄"""
        return self.age

    def get_course(self):
        """获取所有学科中的最高分"""
        # 成绩最低是0分
        max = 0
        for course_name in self.score.__dict__:
            # 获取某一科的分数
            score = getattr(self.score, course_name)
            if score > max:
                max = score
        return max


if __name__ == '__main__':
    stu = Student('小明', 30)
    stu.score = Score(90, 89, 98)

    print(stu.get_name())
    print(stu.get_age())
    print(stu.get_course())