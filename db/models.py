'''
存放类
学校类、学员类、课程类、讲师类、管理员类
'''

from db import db_handler

class Admin:
    def __init__(self,user,pwd):
        self.user=user
        self.pwd=pwd
        # self.save()
    @classmethod
    def select(cls,username):
        #obj:对象 或者None
        obj=db_handler.select_data(cls,username)
        return obj

    def save(self):
        db_handler.save_data(self)






class School:
    pass

class Student:
    pass

class Course:
    pass

class Teacher:
    pass

