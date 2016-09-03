# -*- coding: UTF-8 -*-

#   Fix up the problem of UTF-8 decoding
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# ======================================================

from flask import Flask
from flask_sqlalchemy import SQLAlchemy     # 引入数据库模块
import os
from flask_login import LoginManager    # 引入登录管理模块
from config import basedir  # 引入基准目录变量，用于SQLAlchemy与OpenID

app = Flask(__name__)

app.config.from_object('config')

# 数据库：创建数据库对象
db = SQLAlchemy(app)

# 登录管理模块：创建初始化有关对象
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


from app import views
from app import models
