'''
存放类
学校类、学员类、课程类、讲师类、管理员类
'''

from db import db_handler


# 让所有子类继承save和select方法
class Base:
    @classmethod
    def select(cls, username):
        # obj:对象 或者None
        obj = db_handler.select_data(cls, username)
        return obj

    # 保存数据
    def save(self):
        db_handler.save_data(self)


# 管理员类
class Admin(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        # self.save()

    # 创建学校
    def create_school(self, school_name, school_addr):
        school_obj = School(school_name, school_addr)
        school_obj.save()

    # 创建课程
    def create_course(self, school_obj, course_name):
        # 1.调用课程类，实例化创建课程
        course_obj = Course(course_name)
        course_obj.save()
        # 2.获取当前学校对象，并将课程添加到课程列表中
        school_obj.course_list.append(course_name)
        # 3.更新学校数据
        school_obj.save()

    # 创建讲师
    def create_teacher(self,teacher_name,teacher_pwd):
        #1、调用老师类，实例化得到老师对象，并保存
        teacher_obj=Teacher(teacher_name,teacher_pwd)
        teacher_obj.save()




# 学校类
class School(Base):
    def __init__(self, name, addr):
        # 这里必须写self.user
        # 因为db_handler里面的select_data 统一规范
        self.user = name
        self.addr = addr
        # 课程列表：没说学校都应该有相应的课程
        self.course_list = []


class Student(Base):
    pass


class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []


class Teacher(Base):
    def __init__(self,teacher_name,teacher_pwd):
        self.user=teacher_name
        self.pwd=teacher_pwd
        self.course_list_from_tea=[]
