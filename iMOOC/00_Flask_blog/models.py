# coding:utf8
# 导入三个库
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql # python3连接MySQL数据库需要用的库
from datetime import datetime

# 实例化，连接数据库；以下四行顺序不能颠倒
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:yourpassword@127.0.0.1:3306/movie"  # 此处不要打错！有密码！！！
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


# 建立User表(在这里其实就是建立一个User类，在ORM中将数据库中的User表映射为Python中的对象，两者一一对应)
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    uuid = db.Column(db.String(255), unique=True)
    userlogs = db.relationship("Userlog", backref="user")  # userlog外键关系关联
    comments = db.relationship("Comment", backref="user")
    moviecols = db.relationship("Moviecol", backref="user")

    def __repr__(self):
        return "<User %r>" % self.name  # __repr__是sqlalchemy自带方法，这里查询的时候可以返回会员名


# 建立Userlog表
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # user.id作为此处的外键，所以在user表中需要建立对应关系,参见user数据模型的最后一行
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Userlog %r>" % self.id  # 查询的时候可以传入id


# 3-2
# 建立标签tag
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    movies = db.relationship("Movie", backref="tag")  # 电影外键关联关系

    def __repr__(self):
        return "<Tag %r>" % self.name


# 建立电影表 Moive
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 电影时长
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    comments = db.relationship("Comment", backref="movie")
    moviecols = db.relationship("Moviecol", backref="movie")

    def __repr_(self):
        return "<Movie %r>" % self.title


# 上映预告的数据模型
class Preview(db.Model):
    __tablename__ = "priview"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True)  # 封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr_(self):
        return "<Preview %r>" % self.title


# 3-3
# 定义评论模型
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 注意有movie外键
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 注意有user外键
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Comment %r>" % self.id


# 定义电影收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Moviecol %r>" % self.id


# 权限 right
class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tabelname__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(800))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Role %r>" % self.name


# 定义管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    adminlogs = db.relationship("Adminlog", backref='admin')
    oplogs = db.relationship("Oplog", backref='admin')

    def __repr__(self):
        return "<Admin %r>" % self.name


# 定义管理员登录日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 管理员外键关联
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Adminlog %r>" % self.id


# 定义操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 管理员外键关联
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(600))  # 操作的原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Oplog %r>" % self.id


# 接下来，将数据模型生成数据库表。
if __name__ == '__main__':
    #db.create_all()  # 这里要调用create_all()方法 3-3 17'35"
# 然后使用Terminal，输入 python models.py

#建立一个超级管理员角色
    """
    role = Role(  #Role是数据模型，表示角色；变量name是对应的同名字段
        name='超级管理员',
        auths=''
    )
    db.session.add(role) #添加这个role实例对象到数据库中去
    db.session.commit() #提交到数据库，然后我们输入 python models.py运行
    """

#建立一个管理员账户

    #实例化管理员对象，因为这里涉及到用户名密码，所以需要考虑到安全因素，需要导入werkzeug.security
    from werkzeug.security import generate_password_hash
    admin = Admin(
        name='murphy1',
        pwd=generate_password_hash("murphy"),
        is_super=0,
        role_id=1
    )
    db.session.add(admin)
    db.session.commit()
    #运行后发现，时间有些问题，不是本地时间。所以要改一下，把utcnow改成now。
