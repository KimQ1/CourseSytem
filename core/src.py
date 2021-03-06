'''
主视图层
'''

from core import teacher
from core import student
from core import admin


func_dic={
    '1':admin.admin_view,
    '2':student.student_view,
    '3':teacher.teacher_view,
}




def run():
    while True:
        print('''
        ================欢迎来到选课系统===========
                1、管理员功能
                2、学生功能
                3、老师功能
        ====================end=================
        ''')
        choice=input('请输入编号').strip()
        if choice not in func_dic:
            print('请重新输入')
            continue
        func_dic.get(choice)()


