#!/bin/bash

# 华中科技大学学生社团联合会 人力资源管理系统 - 基于 Flask 开发
# 为了保障正常运行，请你在部署时运行这个脚本，以安装我们所需要的依赖环境：
#	■ Flask 框架，包括主体及附属的必备插件。（参考 Flask Mega Tutorial）
#	■ Passlib。 用于登录密码验证。
#●安装过程需要 pip 工具支持。本脚本会自动为你安装。


if [ -e /usr/bin/pip ]; then
        echo "***	计算机中已安装了 pip"
else
        echo "***	未安装pip！现在将为你安装。。。"
	sudo apt install python-pip
fi


echo "***********************安装 Flask 环境***********************"
pip install flask
pip install flask-login
pip install flask-openid
pip install flask-mail
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf
pip install flask-babel
pip install guess_language
pip install flipflop
pip install coverage

echo "*******************安装 Passlib 加密组件*******************"
pip install passlib


