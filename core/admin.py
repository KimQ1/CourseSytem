'''管理员视图'''

from interface import admin_interface
from lib import common

admin_info={
    'user':None
}

def regisiter():
    while True:
        username=input('请输入用户名').strip()
        password=input('请输入密码').strip()
        re_password=input('请输入密码').strip()
        if password==re_password:
            #调用接口
            flag,msg=admin_interface.admin_register_interface(
                username,
                password
            )
            if flag:
                print(msg)
                #可变类型不需要global
                admin_info['user']=username
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')

def login():
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        #1、调用管理员登录接口
        flag,msg=admin_interface.admin_login_interface(
            username,password
        )
        if flag:
            print(msg)
            #记录当前用户登录状态

            break
        else:
            print(msg)

@common.auth('admin')
def create_school():
    while True:
        #1、输入学校的名城和地址
        school_name=input()
        school_addr=input()
        #2、调用接口保存学校
        admin_interface.create_school_interface(
            school_name,school_addr,
        )

@common.auth('admin')
def create_course():
    pass
@common.auth('admin')
def create_teacher():
    pass


func_dict={
    '1': regisiter,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}

def admin_view():
    while True:
        print('''
        - 1.注册
        - 2.登录
        - 3.创建学校
        - 4.创建课程(先选择学校)
        - 5.创建讲师
        ''')
        choice=input('请输入编号')
        if choice not in func_dict:
            print('请重新输入')
            continue
        func_dict.get(choice)()