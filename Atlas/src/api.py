import os
from flask import request
from flask import Blueprint

from db.models import *

api = Blueprint("api", __name__, "templates")

__dir__ = os.path.dirname(os.path.abspath(__file__))
__db__ = os.path.join(os.path.dirname(__dir__), "db")


# 配合Flask的request返回参数
def get_parameter(label, default=None):
    tem = request.args.get(label)

    if tem is None:
        return default
    return tem.strip()


# flask配合datatables使用的类


# 返回Publish Article
@api.route('/publishes')
def published():
    """
    查询publish
    :return:
    """
    columns = [
        Publishes.project_id, Publishes.tissue, Publishes.title, Publishes.technology, Publishes.species
    ]
    publishes = Publishes.query.all()
    publishes_output = []
    for publish in publishes:
        publishes_output.append(publish.to_json())
    return jsonify(publishes_output)


if __name__ == '__main__':
    app.run()
    # app.run(threaded=True, host="127.0.0.1" , port=5000)
