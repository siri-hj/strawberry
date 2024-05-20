from flask import jsonify, render_template, request
from models import User
from config import Random_num, redis_store
from .cookies import cookies, get_cookies
from app import db
from . import user
from app import redis_client

@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    user_name = request.form.get('name')
    user_password = request.form.get('password')
    user_exit = db.session.query(User).filter(User.name == user_name).all()
    if user_exit:
        for i in user_exit:
            if i.password == user_password:
                # 设置页面cookie，方便其他页面获取
                cookies.set_cookies(i.id)

                return render_template('success.html')

        return render_template('login.html')
    return jsonify(status='失败', msg="查询不到用户")

@user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method =='GET':
        return render_template('register.html')
    user_name = request.form.get('name')
    user_password = request.form.get('password')
    user_phone = request.form.get('phone')
    val_code = request.form.get('valid_code')


    #获取保存在redis里面的验证码
    redis_code = redis_client.get(user_phone).decode('utf-8')

    if not redis_code:
        return jsonify(status='失败', msg="验证码已过期")

        # 判断验证码是否错误
    elif val_code.lower() != redis_code.lower():
        return jsonify(status='失败', msg="验证码错误")

    user = User()
    user.name = user_name
    user.password = user_password
    user.phone = user_phone
    db.session.add(user)
    db.session.commit()
    return render_template('success.html')

@user.route('/impression')
def impression():
    kind = request.args.get('kind')
    print(kind)
    userid = get_cookies()
    print('userid:' + str(userid))
    try:
        return jsonify(status='成功', msg="添加成功")
    except Exception as e:
        return jsonify(status='失败', msg="添加失败")

@user.route('/user_code')
def user_code():
    #获取用户验证码
    phone = request.args.get('phone')
    print(phone)
    user_phones = db.session.query(User).filter(User.phone == phone).all()
    if user_phones:
        return jsonify(status='失败', msg="该号码已被注册")
    try:
        # 生成四位随机数字字母作为验证码
        code = Random_num()

        # 将验证码保存到redis中，第一个参数是key，第二个参数是value，第三个参数表示60秒后过期
        redis_client.set(phone, code, 60)
        # 这里用输出验证码来代替短信发送验证码
        print(code)
        return jsonify(status="成功", msg="验证码发送成功")
    except Exception as e:
        return jsonify(status='失败', msg="验证码发送失败")