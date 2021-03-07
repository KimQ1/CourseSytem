'''
公告所有接口
'''

import os
from conf import settings
from db import models


def get_all_school_interface():
    # 1、获取学校文件路径
    school_dir = os.path.join(
        settings.DB_PATH, 'School'
    )
    # 2判断文件夹是否存在
    if not os.path.exists(school_dir):
        return False, '没有学校，请联系管理员'
    # 3文件夹存在获取文件夹中所有文件的名字
    school_list = os.listdir(school_dir)
    return True, school_list


# 公共登录接口
def login_interface(user, pwd, user_type):
    if user_type == 'admin':
        obj = models.Admin.select(user)

    elif user_type == 'student':
        obj = models.Student.select(user)

    elif user_type == 'teacher':
        obj = models.Teacher.select(user)
    else:
        print()
        return False, '你输入的类型不存在'

    if obj:
        if pwd == obj.pwd:
            return True, '登陆成功'
        else:
            return False, '密码错误'
    else:
        return False, '用户民不存在'

#获取指定学校的所有课程
def get_all_course_in_school_interface(school_name):
    #1、获取学校对象
    school_obj=models.School.select(school_name)
    #2、获取学校对象下的课程
    course_list=school_obj.course_list
    if not course_list:
        return False,'该学校没有课程'
    return True,course_list
