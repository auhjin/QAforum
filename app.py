'''
Author: auhjin auhjin_ai8@163.com
Date: 2024-02-09 22:56:49
LastEditors: auhjin auhjin_ai8@163.com
LastEditTime: 2024-02-09 23:50:26
FilePath: \QAforum\app.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from flask import Flask

# 创建app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
