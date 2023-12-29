# 从flask包中导入Flask类
import os

import export
from flask import Flask
from flask import render_template
from flask import url_for
from flask import send_from_directory

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

# 把 app 写在 flask_study.py 中，必须设置 FLASK_APP=flask_study.py ，如果没有指定FLASK_APP环境变量，flask 运行的时候首先会尝试自动去项目的根目录下的 wsgi.py 文件 或者 app.py 文件里面去找。
# window
# set FLASK_APP=app.py
# linux
# export FLASK_APP=app.py


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


if __name__ == '__main__':
    app.run()
    # app.run(threaded=True, host="127.0.0.1" , port=5000)
