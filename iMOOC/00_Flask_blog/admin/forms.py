# coding:utf8
from flask_wtf import FlaskForm  # 引入表单库
from wtforms import StringField, PasswordField, SubmitField  # 需要处理用户名(StringField)和密码(PasswordField)的字段,
# 表单提交字段(SubmitField) ，如果需要处理整数，就用IntegerField；
from wtforms.validators import DataRequired  # 验证器


# 定义后台登陆的表单，要继承FlaskForm
class LoginForm(FlaskForm):
    """管理员Admin登录的表单"""
    account = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号!")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            "required": "required"

        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
            "required": "required"
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
            }
    )
