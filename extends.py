'''
Author: auhjin auhjin_ai8@163.com
Date: 2024-02-10 23:08:24
LastEditors: auhjin auhjin_ai8@163.com
LastEditTime: 2024-02-10 23:13:47
FilePath: \QAforum\extends.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from flask_sqlalchemy import SQLAlchemy
# from flask_socketio import SocketIO
from flask_migrate import Migrate

# 循环引用
db = SQLAlchemy()


