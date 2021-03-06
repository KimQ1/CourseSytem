'''
学生视图
'''

from lib import common


student_info={
    'user':None
}

def regisiter():
    pass

def login():
    pass

@common.auth('student')
def choice_school():
    pass

@common.auth('student')
def choice_course():
    pass

@common.auth('student')
def choice_teacher():
    pass


func_dict={
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
        choice=input('请输入编号')
        if choice not in func_dict:
            print('请重新输入')
            continue
        func_dict.get(choice)()