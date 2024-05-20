from db_create import db
from datetime import datetime
class User(db.Model):
    # 定义表名
    __tablename__ = 'users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)

class Student(db.Model):
    # 定义表名
    __tablename__ = 'student'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    phone = db.Column(db.String(64))

class Imperssion(db.Model):
    #定义表名
    __tablename__ = 'impressions'
    #定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    scenery = db.Column(db.Integer)
    animal = db.Column(db.Integer)
    impression_num = db.Column(db.Integer)
    user_id = db.Column(db.Integer, primary_key=True)
