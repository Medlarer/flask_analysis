from flask import Blueprint

order = Blueprint("order",__name__)

@order.route("/index")
def login():
    return "index"