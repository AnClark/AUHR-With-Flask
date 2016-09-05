# -*- coding: UTF-8 -*-

""" 《《《数据模型定义文件》》》  """

from app import db
# UserMixIn：用户模型可选之类库。引入旨在防止调用login_user函数时出错，
#   并通过展示成员函数重载关系，提高代码可读性。
from flask_login import UserMixin


class Member(db.Model):
    """ 【社联人力资源核心表——人员信息表】
            所有字段一看即知
    """
    __tablename__ = "Member"
    # 【警告！】 db.Column 中的 Column 首字母大写！
    id = db.Column(db.Integer, primary_key=True, unique=True)
    Name = db.Column(db.String(64), index=True)     # 考虑到可能会有同学同名同姓，故名字字段不设为唯一
    Gender = db.Column(db.String(64), index=True)
    Mobile = db.Column(db.String(64), index=True, unique=True)
    QQ = db.Column(db.String(64), index=True, unique=True)
    Birthday = db.Column(db.Date, index=True)
    Grade = db.Column(db.String(64), index=True)
    Faculty = db.Column(db.String(64), index=True)
    Class = db.Column(db.String(64), index=True)
    DormBuild = db.Column(db.String(64), index=True)
    Department = db.Column(db.String(64), index=True)
    GroupInDepart = db.Column(db.String(64), index=True)
    Occupation = db.Column(db.String(64), index=True)
    AUID = db.Column(db.String(64), index=True, unique=True)
    ArrivalTime = db.Column(db.Date, index=True)

    def __repr__(self):
        return '<Name %r>' % (self.Name)


class Admin(db.Model, UserMixin):
    """【HR系统 用户信息登记表】"""
    __tablename__ = "Admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    nickname = db.Column(db.String(80))
    password = db.Column(db.String(1024))       # 如此预留长度是为了包容加密后的密码字符串
    isPremiumUser = db.Column(db.Boolean)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.username)




