'''管理员接口'''

from db import models


def admin_register_interface(username, password):
    # 1、判断用户是否存在
    # 1.1、若存在不予注册，返回Flase
    # 调用Admin类中的select——data的方法
    admin_obj = models.Admin.select(username)

    # 1.2、若不存在允许注册，调用类实例化得到对象并保存
    if admin_obj:
        return False, '用户已存在!!!'
    # 可在models里面
    admin_obj = models.Admin(username, password)
    admin_obj.save()
    return True, '注册成功'


# def admin_login_interface(username, password):
#     # 判断用户是否存在
#     admin_obj = models.Admin.select(username)
#     # 如果不存在，则返回用户不存在返回给视图层
#     # 如果存在，则校验密码
#     if not admin_obj:
#         return False, '用户不存在!!!'
#     if password == admin_obj.pwd:
#         return True, '登录成功'
#     else:
#         return False, '密码错误'


def create_school_interface(school_name, school_addr, admin_name):
    # 1、查看学校是否存在  school_obj-》对象 or None
    school_obj = models.School.select(school_name)
    # 2、若学校存在，则返回False，告诉用户学校已存在
    if school_obj:
        return False, '该学校已存在'
    # 3、若不存在，则创建学校
    admin_obj = models.Admin.select(admin_name)
    # 由管理员来调用创建学校方法，并传入学校的名字与地址
    admin_obj.create_school(
        school_name, school_addr
    )
    # 4、返回创建学校成功给视图层
    return True, f'[{school_name}]学校创建成功'


def create_course_interface(school_name, course_name, admin_name):
    # 1、查看课程是否存在
    # 1、1 获取学校对象中的课程列表
    school_obj = models.School.select(school_name)
    # 1、2 判断当前课程是否存在当前列表中
    if course_name in school_obj.course_list:
        return False, '当前课程已存在！'
    # 1、3 课程不存在，则创建课程，由管理员创建
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(
        school_obj, course_name
    )

    return True, f'[{course_name}]创建成功，绑定在【{school_name}】'


# 创建老师接口
def create_teacher_interface(teacher_name, admin_name,teacher_pwd='123'):
    # 1、判断用户是否存在,若存在，返回Flase
    teacher_obj=models.Teacher.select(teacher_name)
    if teacher_obj:
        return False,'该老师已存在'
    #2、不存在，则创建老师，让管理员创建
    admin_obj=models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name,teacher_pwd)
    return True,f'[{teacher_name}]创建成功'





