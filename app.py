from flask import Flask, Blueprint
from flask_migrate import Migrate
from db_create import db
from config import SQLALCHEMY_DATABASE_URI
from flask_redis import FlaskRedis

app = Flask(__name__)

#初始化redis
app.config['REDIS_URL'] = 'redis://localhost:6379/0'
redis_client = FlaskRedis(app)

#设置连接数据库url地址
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
#是否追踪数据库修改（开启后一般会触发钩子函数）一般不开
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#是否显示底层执行的SQL语句
app.config['SQLALCHEMY_ECHO'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return '欢迎光临'

#创建蓝图
from admin import admin
from user import user
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')

if __name__ == '__main__':
    app.run()