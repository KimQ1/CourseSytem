from db import models


def student_register_interface(username, password):
    # 1、判断用户是否存在
    # 1.1、若存在不予注册，返回Flase
    # 调用Admin类中的select——data的方法
    student_obj = models.Student.select(username)

    # 1.2、若不存在允许注册，调用类实例化得到对象并保存
    if student_obj:
        return False, '用户已存在!!!'
    # 可在models里面
    student_obj = models.Student(username, password)
    student_obj.save()
    return True, '注册成功'


# def student_login_interface(username,password):
#     # 判断用户是否存在
#     student_obj = models.Student.select(username)
#     # 如果不存在，则返回用户不存在返回给视图层
#     # 如果存在，则校验密码
#     if not student_obj:
#         return False, '用户不存在!!!'
#     if password == student_obj.pwd:
#         return True, '登录成功'
#     else:
#         return False, '密码错误'

# 学生选择学校接口
def add_school_interface(school_name, student_name):
    # 1、判断学生是否存在学校
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False, '当前学生已选学校'
    student_obj.add_school(school_name)
    return True, '选择学校成功'


# 获取学生所在学校所有课程接口
def get_course_list_interface(student_name):
    # 1、获取学生对象
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school
    # 2、判断当前学生是否有学校，若没有则返回False
    if not school_name:
        return False, '没有学校，请先选择学校'
    # 3、开始获取学校对象中的课程列表
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    # 3.1 判断当前学校是否有课程，若没有课程联系管理员创建
    if not course_list:
        return False, '联系管理元创建课程'
    # 3.2、若有则则返回course_list
    return True, course_list


# 学生选择学校接口
def add_course_interface(course_name, student_name):
    # 1、先判断当前课程是否存在学生课程列表中
    student_obj = models.Student.select(student_name)
    if course_name in student_obj.course_list:
        return False, '该课程已选择了'
    # 2、调用学生对象中添加课程的方法
    student_obj.add_course(course_name)
    return True, f'{course_name}课程添加成功'


def check_score_interface(student_name):
    student_obj=models.Student.select(student_name)
    if student_obj.score_dict:
        return True,student_obj.score_dict

