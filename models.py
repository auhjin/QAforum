'''
Author: auhjin auhjin_ai8@163.com
Date: 2024-02-10 23:12:18
LastEditors: auhjin auhjin_ai8@163.com
LastEditTime: 2024-02-10 23:12:28
FilePath: \QAforum\models.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from extends import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(20), unique=True)
    avatar = db.Column(db.String(200))
    create_time = db.Column(db.DateTime)
