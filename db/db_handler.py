import os
import pickle
from conf import settings

#保存数据
def save_data(obj):
    #获取对象的保存文件的路径
    #获取类的名字
    class_name=obj.__class__.__name__
    user_dir_path=os.path.join(
        settings.DB_PATH,class_name
    )
    #2、判断文件是否存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)
    #3、拼接当前用户的pickle文件路劲，以用户名作为文件名
    user_path=os.path.join(
        user_dir_path,obj.user
    )
    with open(user_path,'wb') as f:
        pickle.dump(obj,f)
#查看数据
def select_data(cls,username):
    class_name = cls.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )
    # 2、判断文件是否存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)
    # 3、拼接当前用户的pickle文件路劲，以用户名作为文件名
    user_path = os.path.join(
        user_dir_path, username
    )
    #4.判断文件如果存在，再打开，并返回，若不存在，则代表用户不存在
    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            obj=pickle.load(f)
            return obj