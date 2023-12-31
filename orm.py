from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# MySQL所在主机名
HOSTNAME = "127.0.0.1"
# 监听端口号
PORT = "3306"
# 连接MySQL的用户名
USERNAME = "root"
# 连接MySQL的密码
PASSWORD = "anysysdy2697!"
# 数据库名称
DATABASE = "textdb_01"

# 在app.config当中配置好数据库的信息
app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset"
                                         f"=utf8mb4")

# 使用SQLAlchemy创建一个db对象
# SQLAlchemy会自动读取app.config中连接数据库的信息
db = SQLAlchemy(app)


# 测试连接是否成功
# with app.app_context():
#    with db.engine.connect() as conn:
#        rs = conn.execute(text("select 1"))
#        print(rs.fetchone())

# 创建设计新表
class User(db.Model):
    # 创建表名"user"
    __tablename__ = "user"
    # 主键，自动增加
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 字段为String型下的varchar，最大长度为100，不为null
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    # 创建表名"user"
    __tablename__ = "article"
    # 主键，自动增加
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # 添加作者的外键
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # Integer类型和user.id保持一致！
    # backref会自动给User模型添加一个articles的属性，用来获取文章列表
    author = db.relationship("User", backref="articles")


with app.app_context():
    db.create_all()


# CREATE
@app.route("/user/add")
def add_user():
    # 创建ORM对象
    user = User(username="MTY", password="0000")
    # 将ORM对象添加到db.session中
    db.session.add(user)
    # 将db.session同步到数据库中
    db.session.commit()
    return "用户创建成功！"


# READ
@app.route("/user/query")
def query_user():
    # 1.get: 根据主键查找
    # user = User.query.get(1)
    # print(f"{user.id}: {user.username}-{user.password}")
    # 2.filter_by
    users = User.query.filter_by(username="MTY")
    print(type(users))
    # Query: 它是一个类数组
    for user in users:
        print(user.username)
    return "Query Success"


# 表的关系（基于外键实现）


@app.route('/')
def hello_world():
    return 'Success Connect'


if __name__ == '__main__':
    app.run()
