'''
Author: auhjin auhjin_ai8@163.com
Date: 2024-02-10 23:17:24
LastEditors: auhjin auhjin_ai8@163.com
LastEditTime: 2024-02-10 23:23:38
FilePath: \QAforum\blueprints\auth.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from flask import Blueprint, render_template, request, flash, redirect, url_for

Blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@Blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '123456':
            flash('登录成功')
            return redirect(url_for('index'))
        else:
            flash('登录失败')
            return redirect(url_for('auth.login'))