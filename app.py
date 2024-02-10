'''
Author: auhjin auhjin_ai8@163.com
Date: 2024-02-09 22:56:49
LastEditors: auhjin auhjin_ai8@163.com
LastEditTime: 2024-02-10 22:57:14
FilePath: \QAforum\app.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.sql import text
from flask_migrate import Migrate
from datetime import datetime

# 创建app
app = Flask(__name__)
# 数据库配置
Hostname = 'localhost'
Port = 3306
Database = 'flask'
Username = 'root'
Password = '123456'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{Username}:{Password}@{Hostname}:{Port}/{Database}?charset=utf8mb4'


db = SQLAlchemy(app)
migrate = Migrate(app, db)
# ORM 模型映射

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text('select 1'))
#         print(rs.fetchone())

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.now)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref='articles')

# ORM 增删改查
@app.route('/user/add')
def user_add():
    user = User(name='auhjin', email='auhjin_ai8@163.com', password='123456')
    db.session.add(user)
    db.session.commit()
    return 'ok'

@app.route('/user/delete/<int:user_id>')
def user_delete(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return 'ok'

@app.route('/user/update/<int:user_id>')
def user_update(user_id):
    user = User.query.get(user_id)
    user.name = 'auhjin2'
    db.session.commit()
    return 'ok'

@app.route('/user/list')
def user_list():
    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/user/<int:user_id>')
def user(user_id):
    user = User.query.get(user_id)
    return render_template('user.html', user=user)

@app.route('/article/add')
def article_add():
    article = Article(title='flask', content='flask is a web framework')
    article.author = User.query.get(1)
    db.session.add(article)
    db.session.commit()
    return 'ok'

@app.route('/article/delete/<int:article_id>')
def article_delete(article_id):
    article = Article.query.get(article_id)
    db.session.delete(article)
    db.session.commit()
    return 'ok'

@app.route('/article/update/<int:article_id>')
def article_update(article_id):
    article = Article.query.get(article_id)
    article.title = 'flask2'
    db.session.commit()
    return 'ok'

@app.route('/article/list')
def article_list():
    user = User.query.get(1)
    for article in user.articles:
        print(article)
    # articles = Article.query.all()
    return render_template('article_list.html', articles=user.articles)

# with app.app_context():
#     db.create_all()

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
