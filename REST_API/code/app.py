from flask import Flask, request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT , jwt_required
from REST_API.code.security import authenticate, identity

app = Flask(__name__)

app.secret_key = "Secret"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []  # item list


class Item(Resource):
    # parse the request
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be left blank")
    data = parser.parse_args()
    def get(self,name):
        item = next(filter(lambda x: x["name"] == name, items),None) # next will give us the first --> but we only have one

        return {"item":item},200 if item  else 404

    @jwt_required()
    def post(self,name):
        if  next(filter(lambda x: x["name"] == name, items),None) is not None:
            return {"message":"An item with name  '{}' already exist.".format(name)},400 # bad request


        data = Item.parser.parse_args()
        price = data["price"]
        item = {"name": name, "price": price}
        items.append(item)
        return item, 201 # creating success # 201 ||  # 202 --> accepted but not excuted

    @jwt_required()
    def delete(self,name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "item deleted"}

    @jwt_required()
    def put(self,name):

        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name , items),None)
        if item is None:
            item = {"name":name, "price":data["price"]}
            items.append(item)
        else:
            item.update(item)
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}



api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList, "/items")


app.run(port=5000, debug=True)

