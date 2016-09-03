# -*- coding: UTF-8 -*-

#   【表单配置】
#   【警告！】 跨站点请求伪造保护功能（CSRF）是默认开启的！
CSRF_ENABLED = True
SECRET_KEY = 'the-blue-lotus'

#   【数据库配置系列代码】
database_name = 'AUHRSystem.db'     # 指定数据库文件名

#   获取并保存基准路径（即整个工程的根目录），以供SQLAlchemy使用
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#   指定数据库的一些路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, database_name)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#=========================================================
