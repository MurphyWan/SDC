# coding:utf8
# 3定义home视图

# 从当前模块中导入
from . import home
from flask import render_template, redirect, url_for


# 在home.html的内容里面定义数据块{% block content %}{% endblock %}之后
# 这里我们要导入render_template模块，用于呈现网页

# 定义视图函数
@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/login/")
def login():
    return render_template("home/login.html")


@home.route("/logout/")
def logout():
    return redirect(url_for('home.login'))  # 这里，我们退出后就重新回到登录界面，所以要用到重定向redirect，导入该库。


@home.route("/register/")
def register():
    return render_template("home/register.html")

@home.route("/user/")
def user():
    return render_template("home/user.html")

@home.route("/pwd/")
def pwd():
    return render_template("home/pwd.html")

@home.route("/comments/")
def comments():
    return render_template("home/comments.html")

@home.route("/loginlog/")
def loginlog():
    return render_template("home/loginlog.html")

@home.route("/moviecol/")
def moviecol():
    return render_template("home/moviecol.html")
