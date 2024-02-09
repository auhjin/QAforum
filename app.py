'''
Author: auhjin auhjin_ai8@163.com
Date: 2024-02-09 22:56:49
LastEditors: auhjin auhjin_ai8@163.com
LastEditTime: 2024-02-10 00:45:04
FilePath: \QAforum\app.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from flask import Flask, render_template
from datetime import datetime

# 创建app
app = Flask(__name__)

# 自定义过滤器
@app.template_filter('datetime_format')
def datetime_filter(value, format='%Y-%m-%d %H:%M:%S'):
    return value.strftime(format)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    mytime = datetime.now()
    return render_template('blog.html', blog_id = blog_id, mytime = mytime)
    

if __name__ == '__main__':
    app.run(debug=True)
