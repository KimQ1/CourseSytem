'''
学生视图
'''

from lib import common
from interface import student_interface
from interface import common_interface

student_info = {
    'user': None
}


# 学生注册
def regisiter():
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        re_password = input('请再次输入密码').strip()
        if password == re_password:
            # 调用接口层，学生注册接口
            flag, msg = student_interface.student_register_interface(
                username,
                password
            )
            if flag:
                print(msg)
                # 可变类型不需要global
                student_info['user'] = username
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


# 学生登录
def login():
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        # 1、调用管理员登录接口
        flag, msg = common_interface.login_interface(
            username, password, user_type='student'
        )
        if flag:
            print(msg)
            # 记录当前用户登录状态
            # 可变类型不需要global
            student_info['user'] = username
            break
        else:
            print(msg)


@common.auth('student')
def choice_school():
    while True:
        # 1、获取所有学校
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break
        for index, school_name in enumerate(school_list):
            print(f'编号{index},学校名：{school_name}')

        # 2、学生输入学校编号
        choice = input('输入学校编号').strip()
        if not choice.isdigit():
            print('编号有误')
        choice = int(choice)

        if choice not in range(len(school_list)):
            print('输入有误')
            continue
        school_name = school_list[choice]
        # 3、开始调用学生选择学校接口
        flag, msg = student_interface.add_school_interface(
            school_name, student_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth('student')
def choice_course():
    while True:
        # 1、先获取当前学生所在学校的课程列表
        flag,course_list=student_interface.get_course_list_interface(
            student_info.get('user')
        )
        if not flag:
            print(course_list)
            break
        #2、打印课程列表、并让用户选择课程
        for index, course_name in enumerate(course_list):
            print(f'编号{index},课程名：{course_name}')

        # 2、学生输入课程编号
        choice = input('输入课程编号').strip()
        if not choice.isdigit():
            print('编号有误')
        choice = int(choice)

        if choice not in range(len(course_name)):
            print('输入有误')
            continue
        #3、获取选择的课程名称
        course_name = course_name[choice]
        #4、调用选择课程接口
        flag,msg=student_interface.add_course_interface(
            course_name,
            student_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)



    # 2、打印课程列表、并让用户选择课程

@common.auth('student')
def check_score():
    score_dict=student_interface.check_score_interface(
        student_info.get('user')
    )
    if not score_dict:
        print('meiyouchengjie')
    print(score_dict)


@common.auth('student')
def choice_teacher():
    pass


func_dict = {
    '1': regisiter,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': choice_teacher,
}


def student_view():
    while True:
        print('''
        - 1.注册
        - 2.登录功能
        - 3.选择校区
        - 4.选择课程
        - 5.查看分数
        ''')
        choice = input('请输入编号')
        if choice not in func_dict:
            print('请重新输入')
            continue
        func_dict.get(choice)()
