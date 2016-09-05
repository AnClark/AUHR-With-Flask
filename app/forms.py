# -*- coding: UTF-8 -*-

""" 《《表单定义文件》》"""

from flask_wtf import Form
from wtforms.fields import StringField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class InputBasicInfoForm(Form):
    Name = StringField('Name', validators=[DataRequired("姓名必须填写")])
    Gender = StringField('Gender', validators=[DataRequired("请选择性别")])
    Mobile = StringField('Mobile', validators=[DataRequired("请输入手机号")])
    QQ = StringField('QQ')
    Birthday = DateField('Birthday')
    Grade = StringField('Grade', validators=[DataRequired("请输入年级")])
    Faculty = StringField('Faculty', validators=[DataRequired("请输入专业")])
    Class = StringField('Class')
    DormBuild = StringField('DormBuild')
    Department = StringField('Department', validators=[DataRequired("所在社联部门必须填写")])
    GroupInDepart = StringField('GroupInDepart')
    Occupation = StringField('Occupation', validators=[DataRequired("职务必须填写")])
    AUID = StringField('AUID')
    ArrivalTime = DateField('ArrivalTime', validators=[DataRequired("请输入加入社联的时间")])


class LoginForm(Form):
    username = StringField('username', validators=[Length(min=5, max=64), DataRequired("请输入用户名！")])
    password = PasswordField('password', validators=[Length(min=5, max=64), DataRequired("请输入密码！")])
    remember_me = BooleanField('remember_me')


class KeyWordQueryForm(Form):
    KeyWord = StringField('KeyWord', validators=[DataRequired("要检索资料，请输入关键字。。。")])


