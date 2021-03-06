'''管理员接口'''

from db import models

def admin_register_interface(username,password):
    #1、判断用户是否存在
    #1.1、若存在不予注册，返回Flase
    #调用Admin类中的select——data的方法
    admin_obj=models.Admin.select(username)

    #1.2、若不存在允许注册，调用类实例化得到对象并保存
    if admin_obj:
        return False,'用户已存在!!!'
    #可在models里面
    admin_obj=models.Admin(username,password)
    admin_obj.save()
    return True,'注册成功'

def admin_login_interface(username,password):
    #判断用户是否存在
    admin_obj=models.Admin.select(username)
    if not admin_obj:
        return False, '用户不存在!!!'
    if password==admin_obj.pwd:
        return  True,'登录成功'
    else:
        return False,'密码错误'

    #如果不存在，则返回用户不存在返回给视图层
    #如果存在，则校验密码
    pass







