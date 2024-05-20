from flask import render_template, request
from . import admin
from models import User

@admin.route('/')
def aaa():
    return '使用blueprint成功'

@admin.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@admin.route('/user_check')
def admin_check():
    if request.method == 'GET':
        users = User.query.all()
        return render_template('user_check.html', users=users)

