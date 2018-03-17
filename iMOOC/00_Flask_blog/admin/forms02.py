# coding:utf8
from flask_wtf import FlaskForm  # 引入表单库
from wtforms import StringField, PasswordField, SubmitField  # 需要处理用户名(StringField)和密码(PasswordField)的字段,
# 表单提交字段(SubmitField) ，如果需要处理整数，就用IntegerField；
# 更多详细了解，可以将鼠标移到以上某个库名上，按住键盘Ctrl+b看源代码和更多类型字段。
from wtforms.validators import DataRequired,ValidationError  # 验证器，比如字段不能为空。
from app.models import Admin

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
            # "required": "required"

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
            # "required": "required"
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
            }
    )

    def validate_account(self,field):
        account = field.data
        admin=Admin.query.filter_by(name=account).count() #需要导入Admin模型，查询这个account到底有几条
        if admin ==0: # 如果没有查到，抛出验证错误
            raise ValidationError("账号不存在！") #导入ValidationError

