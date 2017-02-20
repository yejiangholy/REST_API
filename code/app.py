from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import ItemList, Item


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "Secret"

api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister,"/register")

if __name__ == "__main__": #prevent run app if not appropriate
    from db import  db
    db.init_app(app)
    app.run(port=5000, debug=True)
