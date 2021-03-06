'''
公告所有接口
'''

import os
from conf import settings


def get_all_school_interface():
    #1、获取学校文件路径
    school_dir=os.path.join(
        settings.DB_PATH,'School'
    )
    #2判断文件夹是否存在
    if not os.path.exists(school_dir):
        return False,'没有学校，请联系管理员'
    #3文件夹存在获取文件夹中所有文件的名字
    school_list=os.listdir(school_dir)
    return True,school_list