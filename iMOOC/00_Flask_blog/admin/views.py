# coding:utf8
# 4定义admin视图;下一步定义app模块下的初始化文件__init__.py

# 从当前模块中导入
from . import admin
from flask import render_template, redirect, url_for, flash, session, request
from app.admin.forms import LoginForm
from app.models import Admin
from functools import wraps


def admin_login_req(f):  # 定义一个函数和一个参数
    @wraps(f)  # 定义一个@wraps，把函数作为参数传进入
    def decorated_function(*args, **kwargs):  # 然后定义装饰器的一个方法，让某个函数继承我们的参数
        # if not session.has_key("admin") or session["admin"] is None:  # 看看session中有无admin字段,可以看到33行有一个admin，或者是一个None
        if "admin" not in session:  # 看看session中有无admin字段,可以看到43行有一个admin，或者是一个None
            return redirect(url_for("admin.login", next=request.url))  # 如果session没有或者是None，我们要定义个限制，返回登录页面,
                                                                       # TA获取的就是我们跳转的地址
        return f(*args, **kwargs)  # return这个函数，装饰器的作用是给我们的函数继承的。

    return decorated_function


# @admin.route("/")
# def index():
#     return "<h1 style='color:red'>this is admin </h1>"

@admin.route("/")
@admin_login_req
def index():
    return render_template("admin/index.html")


@admin.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # 表示提交的时候进行验证
        data = form.data  # 定义好之后，我把错误信息显示到模板中
        admin = Admin.query.filter_by(name=data['account']).first()
        if not admin.check_pwd(data['pwd']):  # 验证密码不成功，则闪现flash密码错误提示。
            flash('秘密错误哦！')  # 导入flash
            return redirect(url_for('admin.login'))
        session["admin"] = data["account"]  # 用session保存admin，这里要导入session库
        return redirect(request.args.get("next") or url_for("admin.index"))  # 导入request库，这里跳转有两个，一个是next一个是admin.index
    return render_template("admin/login.html", form=form)


@admin.route("/logout/")
@admin_login_req
def logout():
    session.pop("admin", None)
    return redirect(url_for("admin.login"))


@admin.route("/pwd/")
@admin_login_req
def pwd():
    return render_template("admin/pwd.html")


@admin.route("/tag/add/")
@admin_login_req
def tag_add():
    return render_template("admin/tag_add.html")


@admin.route("/tag/list/")
@admin_login_req
def tag_list():
    return render_template("admin/tag_list.html")


@admin.route("/movie/add/")
@admin_login_req
def movie_add():
    return render_template("admin/movie_add.html")


@admin.route("/movie/list/")
@admin_login_req
def movie_list():
    return render_template("admin/movie_list.html")


# 5-3 5'30
@admin.route("/preview/add/")
@admin_login_req
def preview_add():
    return render_template("admin/preview_add.html")


@admin.route("/preview/list/")
@admin_login_req
def preview_list():
    return render_template("admin/preview_list.html")


# 5-4
@admin.route("/user/list/")
@admin_login_req
def user_list():
    return render_template("admin/user_list.html")


@admin.route("/user/view/")
@admin_login_req
def user_view():
    return render_template("admin/user_view.html")


# 5-4
@admin.route("/comment/list/")
@admin_login_req
def comment_list():
    return render_template("admin/comment_list.html")


@admin.route("/moviecol/list/")
@admin_login_req
def moviecol_list():
    return render_template("admin/moviecol_list.html")


# 5-5
@admin.route("/oplog/list/")
@admin_login_req
def oplog_list():
    return render_template("admin/oplog_list.html")


@admin.route("/adminloginlog/list/")
@admin_login_req
def adminloginlog_list():
    return render_template("admin/adminloginlog_list.html")


@admin.route("/userloginlog/list/")
@admin_login_req
def userloginlog_list():
    return render_template("admin/userloginlog_list.html")


@admin.route("/role/add/")
@admin_login_req
def role_add():
    return render_template("admin/role_add.html")


@admin.route("/role/list/")
@admin_login_req
def role_list():
    return render_template("admin/role_list.html")


@admin.route("/auth/add/")
@admin_login_req
def auth_add():
    return render_template("admin/auth_add.html")


@admin.route("/auth/list/")
@admin_login_req
def auth_list():
    return render_template("admin/auth_list.html")


# 5-6
@admin.route("/admin/add/")
@admin_login_req
def admin_add():
    return render_template("admin/admin_add.html")


@admin.route("/admin/list/")
@admin_login_req
def admin_list():
    return render_template("admin/admin_list.html")
