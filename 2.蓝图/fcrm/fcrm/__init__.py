from flask import Flask


app = Flask(__name__)

from .views import account
from .views import order

app.register_blueprint(account.account)
app.register_blueprint(order.order)