# 从flask包中导入Flask类
from flask import Flask
from flask import render_template

# 使用Flask类创建一个app对象
# __name__: 代表当前app.py这个模块
# 1. 出现bug，可以帮助快速定位
# 2. 对于寻找模版文件，有一个相对路径
app = Flask(__name__)


# 创建路由和视图函数的映射
# '/': 代表根路由;
# https://www.xxx.com;
# /home/user/xx;

@app.route('/')
def index():
    u"""
    主页
    :return:
    """
    return render_template("index.html")


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
