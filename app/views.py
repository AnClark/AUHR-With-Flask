# -*- coding: UTF-8 -*-
from app import app, db, lm, models
from flask import render_template, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from flask import flash

# from .models import Admin

from .forms import LoginForm
from .forms import InputBasicInfoForm

#   引入 Passlib 加密模块
from passlib.hash import sha256_crypt

#   用户权限开关
#   指示HR系统是否在高级用户状态下运行。
#   运用高级用户登录，就可以解锁信息录入、信息修改、信息删除等高级功能。否则，只能进行信息查询。
Premium_User_Switch = False


""" ####################################### 登 录 管 理 部 分 #######################################"""


@app.before_request
def before_request():
    # 全局用户名，在用户登录后指派于此，可为生命周期内所有页面共享
    g.user = current_user
    #   用户权限开关
    #   指示HR系统是否在高级用户状态下运行。
    #   运用高级用户登录，就可以解锁信息录入、信息修改、信息删除等高级功能。否则，只能进行信息查询。
    g.Premium_User_Switch = False

#   从数据库中加载HR用户信息
@lm.user_loader
def load_user(id):
    return models.Admin.query.get(int(id))


#   站点主入口。
#   直接进入登录页面
#   【友情提示】和Java类似，Python的对象允许先使用后定义！
@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('login'))


#   登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    if g.user is not None and g.user.is_authenticated():
        # 测试期间，登录成功页面暂时指向基本信息管理页面
        return redirect('/info')
    """
    form = LoginForm()

    if form.validate_on_submit():
        input_username = form.username.data
        input_password = form.password.data

        # 获取用户信息
        userinfo_loginer = models.Admin.query.filter_by(username=input_username).first()

        # 检测用户名是否存在
        if userinfo_loginer == None:
            form.username.errors.append("用户名不存在！")  # 直接将错误信息附加到表单验证器的错误列表中
            return render_template('login/login.html', form=form)

        # ============  密码验证过程  =============
        """从数据库中读取sha256加密后的密码字串
            和 PHP 类似，运行查询函数后获取到的对象并不是字符串，而是与资源有关的各种对象。
            操作备忘录：
            ① 执行 session.query(字段对象) 函数后：生成一个list，成员为按照字段筛选后的 SQLAlchemy 数据元组
            ② 由于我设置了用户名唯一，因此正常情况下，list中只有一个数据元组。
            ③ 元组的第一个元素即为查询而得的密码字串，但这是以SQLAlchemy数据串的方式存储的（字母u开头的字符串）。
                因此，必须使用str()函数，将它转换为字符串，方可得到我们需要的密码字串。
         """

        password_char = db.session.query(models.Admin.password).filter_by(username=str(input_username)).all()[0]
        password_char = str(password_char[0])
        #if(sha256_crypt.verify(input_password, password_char)):

        if input_password == password_char:
            pass
        else:
            form.password.errors.append("密码错误！")
            # flash("Queried password is: %s \n Your inputed password is: %s" % (password_char, input_password))
            return render_template('login/login.html', form=form)

        #   登录
        # 【警告！】当填入用户数据库中不存在的用户名时，如果不验证并拦截，就会触发异常！
        login_user(user=userinfo_loginer, remember=form.remember_me.data)

        # For debug
        #if g.user:
        #    flash("登陆成功！服务器用户名：%s" % g.user.username)
        # flash("当前你输入的登录信息——用户名：%s；密码：%s" % (input_username, input_password))

        # 登录通过，即进入主页面。
        # 主页面未建立，因此暂时以基本信息管理部分做之
        return redirect(url_for('info'))
        # return render_template('login/login.html', form=form)

    return render_template('login/login.html', form=form)


#   登出页面
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

"""#########################################################################################################"""


"""###################################### 基 本 信 息 管 理 部 分 ##########################################
        整个基本信息管理系统的核心，汇聚于此。
        所有页面都设置了@login_required装饰器，只允许登录后才能访问。
"""


#   基本信息录入程序之主页
@app.route('/info')
@login_required
def info():
    user = g.user
    return render_template('info/index.html', user=user, isPremiumUser=Premium_User_Switch)


#   基本信息录入页面
@app.route('/info/input', methods=['GET', 'POST'])
@login_required
def info_input():
    user = g.user

    form = InputBasicInfoForm()
    if form.validate_on_submit():
        #   <测试过程> 打印出表单提交的结果
        flash_form_submit(form)
        return redirect('/info/input')

    return render_template('info/input.html', user=user, isPremiumUser=Premium_User_Switch, form=form)


#   查询入口页面
#   在入口页面中，可以直接以关键字或部门分类进行查询（没有必要再去做二级页面）
@app.route('/info/query')
@login_required
def info_query():
    user = g.user

    return render_template('info/query.html', user=user, isPremiumUser=Premium_User_Switch)


#   查询结果集页面
#   查询结果显示在这里。
#   点击条目，即可以页面内弹窗的形式，展示单人信息报表
@app.route('/info/query_result')
@login_required
def info_query_result():
    user = g.user
    return render_template('info/query_result.html', user=user, isPremiumUser=Premium_User_Switch)


# <测试过程>
# 以flash模式输出表单提交的内容
def flash_form_submit(form):
    flash_str = """【刚才你提交的表单信息如下】
        姓名：%s
        性别：%s
        手机号码：%s
        QQ：%s
        生日：%s
        年级：%s
        专业：%s
        班级：%s
        寝室楼栋：%s
        所在部门：%s
        部门内组别：%s
        社联职务：%s
        社联编号：%s
        入社联时间：%s
    """ % (form.Name.data,
             form.Gender.data,
             form.Mobile.data,
             form.QQ.data,
             form.Birthday.data,
             form.Grade.data,
             form.Faculty.data,
             form.Class.data,
             form.DormBuild.data,
             form.Department.data,
             form.GroupInDepart.data,
             form.Occupation.data,
             form.AUID.data,
             form.ArrivalTime.data)
    flash(flash_str)

