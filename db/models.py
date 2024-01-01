from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict
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
DATABASE = "eRNA"

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

class EntityBase(object):
    def to_json(self):
        u"""
        将每个数据查询后的对象转换为JSON对象返回
        :return:
        """
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]

        return fields


# Publish表格设计
class Publishes(db.Model, EntityBase):
    # 创建表名"publish"
    __tablename__ = "publish"
    # 主键，自动增加
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 字段为String型下的varchar，最大长度为100，不为null
    species = db.Column(db.String(100), nullable=False)
    title = db.Column(db.Text, nullable=False)
    project_id = db.Column(db.String(100), nullable=False)
    tissue = db.Column(db.String(100), nullable=False)
    # description = db.Column(db.Text, nullable=False)
    technology = db.Column(db.String(100), nullable=False)


"""
    def publish_to_dict(self):
        
        定义函数_to_dict，将publishes对象（Publish的实例）转换为dict格式
        :param self:
        :return:
        
        return OrderedDict(
            id=self.id,
            species=self.species,
            title=self.title,
            project_id=self.project_id,
            tissue=self.tissue,
            technology=self.technology
        )
"""


@app.route('/publishes')
def list_publishes():
    u"""
    定义list_publishes函数返回全部收集文献的结果到 publishes 变量中
    利用publish_to_dict函数将 publishes变量作为函数的参数，输出dict结构
    :return:
    """
    publishes = Publishes.query.all()
    publishes_output = []
    for publish in publishes:
        publishes_output.append(publish.to_json())
    return jsonify(publishes_output)


@app.route('/publishes/<publish_id>')
def find_publish(publish_id):
    u"""
    定义find_publish函数返回查询id返回的文献结果；
    :param publish_id:
    :return:
    """
    publish = Publishes.query.get(publish_id)
    return jsonify(publish.to_json())


# 如果有多表联查；引入第三方模块Flask-Marshmallow

# READ
"""
@app.route("/read")
def query_user():
    # 1.get: 根据主键查找
    # user = User.query.get(1)
    # print(f"{user.id}: {user.username}-{user.password}")
    # 2.filter_by
    publishes = Publishes.query.filter_by(species="Human")
    print(type(publishes))
    # Query: 它是一个类数组
    for publish in publishes:
        print(publish.technology)
    return "Query Success"
"""

# with app.app_context():
#    db.create_all()

"""
# 创建设计新表

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
"""


@app.route('/')
def hello_world():
    return 'Success Connect'


if __name__ == '__main__':
    app.run()
