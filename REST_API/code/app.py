from flask import Flask, request
from flask_restful import Resource,Api

app = Flask(__name__)

app.secret_key = "Secret"
api = Api(app)

items = []  # item list


class Item(Resource):
    def get(self,name):
        # for item in items:
        #     if item["name"] == name:
        #         return item
        item = next(filter(lambda x: x["name"] == name, items),None) # next will give us the first --> but we only have one

        return {"item":item},200 if item  else 404


    def post(self,name):
        if  next(filter(lambda x: x["name"] == name, items),None) is not None:
            return {"message":"An item with name  '{}' already exist.".format(name)},400 # bad request


        data = request.get_json(silent = True)
        price = data["price"]
        item = {"name": name, "price": price}
        items.append(item)
        return item, 201 # creating success # 201 ||  # 202 --> accepted but not excuted



class ItemList(Resource):
    def get(self):
        return {"items": items}



api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList, "/items")


app.run(port=5000, debug=True)

