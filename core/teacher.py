'''
老师视图
'''
from lib import common

teacher_info={
    'user':None
}

def login():
    pass

@common.auth('teacher')
def check_course():
    pass

@common.auth('teacher')
def choose_course():
    pass

@common.auth('teacher')
def check_stu_from_course():
    pass

@common.auth('teacher')
def change_score_from_student():
    pass

func_dict = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_score_from_student,
}




def teacher_view():
    while True:
        print('''
        - 1.登录
        - 2.查看教授课程
        - 3.选择教授课程
        - 4.查看课程下学生
        - 5.修改学生分数
        ''')
        choice=input('请输入编号')
        if choice not in func_dict:
            print('请重新输入')
            continue
        func_dict.get(choice)()