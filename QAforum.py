'''
Author: auhjin auhjin_ai8@163.com
Date: 2024-02-10 23:04:46
LastEditors: auhjin auhjin_ai8@163.com
LastEditTime: 2024-02-10 23:23:34
FilePath: \QAforum\QAforum.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from flask import Flask
from extends import db
from models import *
from blueprints import blueprint as bp_auth
import config

app = Flask(__name__)
db.init_app(app)
app.register_blueprint(bp_auth)
# 加载配置文件
app.config.from_object(config)


if __name__ == '__main__':
    app.run(debug=True)