from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from REST_API.code.security import authenticate, identity
from REST_API.code.user import UserRegister
from REST_API.code.item import ItemList, Item


app = Flask(__name__)

app.secret_key = "Secret"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister,"/register")

app.run(port=5000, debug=True)

