'''
教师接口
'''
from db import models


#老师查看课程接口
def check_course_interface(teacher_name):
    #1、获取当前老师对象
    teacher_obj=models.Teacher.select(teacher_name)
    #2、判断吗老师对象中课程列表是否有值
    # course_list=teacher_obj.course_list_from_tea
    #让老师对象，调用查看教授课程方法，返回课程
    course_list=teacher_obj.show_course()
    #3、若有值则返回Ture,无则返回False
    if not course_list:
        return False,'老师没有课程'
    #4、调用
    return True,course_list

#老师添加课程接口
def add_course_interface(course_name,teacher_name):
    #获取老师对象
    teacher_obj=models.Teacher.select(teacher_name)
    #判断当前课程是否存在老师的课程表zhong
    course_list=teacher_obj.course_list_from_tea
    if course_name in course_list:
        return False,'该课程已存在'

    #不存在，则添加该课程到老师课程表中
    teacher_obj.add_course(course_name)
    return True,'课程添加成功'