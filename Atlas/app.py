# 从flask包中导入Flask类
import os
from flask import redirect
from flask import render_template
from flask import url_for
from flask import send_from_directory
from flask_wtf import CSRFProtect
from db.models import *
from src.api import api

# 使用Flask类创建一个app对象
# __name__: 代表当前app.py这个模块
# 1. 出现bug，可以帮助快速定位
# 2. 对于寻找模版文件，有一个相对路径
__dir__ = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=os.path.join(__dir__, 'static'))
__author__ = "Ma Tianyu"

# 建立app
app = Flask(__name__, static_folder=os.path.join(__dir__, 'static'))
# app.debug = True

# 指定密钥
# app.config['SECRET_KEY'] = 'lcbb.swjtu.edu.cn'

# 启用csrf加密保护措施
csrf = CSRFProtect(app)
csrf.init_app(app)

# 每次访问之前，首先生成一个url列表，供details页面的datatables使用

app.register_blueprint(api, url_prefix="/api")


# 错误处理
@app.errorhandler(401)
def no_tissue_eid(error):
    u"""
    401是自定义的错误选项，没有组织也没有eid，就要查看表达量的错误
    """
    return redirect(url_for('index')), 401


# 404
@app.errorhandler(404)
def not_response(error):
    u"""
    404
    """
    return render_template('error.html', error_code=404), 404


# 500
@app.errorhandler(500)
def internal_error():
    u"""
    500
    """
    return render_template("error.html"), 500


# 创建路由和视图函数的映射
# '/': 代表根路由;
# https://www.xxx.com;
# /home/user/xx;

# serve statics
@app.route("/static/<path:filename>")
def static_by_self(filename):
    """
    供应静态文件，服务器上太多站点，不好统一管理
    :return:
    """
    directory = os.path.join(__dir__, "static")
    return send_from_directory(directory=directory, filename=filename)


# serve images
@app.route("/image/<path:filename>")
def image(filename):
    u"""
    serve images
    :return:
    """
    directory = os.path.join(__dir__, "image")
    return send_from_directory(directory=directory, filename=filename)


@app.route('/')
def index():
    u"""
    主页
    :return:
    """
    return render_template("index.html",
                           page="index"
                           )


@app.route("/download")
def download():
    u"""
    Download页面
    :return:
    """
    return render_template("blank.html",
                           type="download",
                           page="download"
                           )


@app.route("/help")
def help():
    u"""
    HELP页面
    :return:
    """
    return render_template("blank.html",
                           type="help",
                           page="help")


@app.route("/publish")
def publish():
    return render_template("blank.html",
                           type="publish",
                           page="publish"
                           )


if __name__ == '__main__':
    app.run()
    # app.run(threaded=True, host="127.0.0.1" , port=5000)
