from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel



class Item(Resource):
    # parse the request
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be left blank")
    #data = parser.parse_args()
    def get(self,name):
       item = ItemModel.find_by_name(name)
       if item:
           return item.json()
       return {"message":"Item not found"},404


    @jwt_required()
    def post(self,name):
        if ItemModel.find_by_name(name):
            return {"message":"An item with name  '{}' already exist.".format(name)},400 # bad request


        data = Item.parser.parse_args()
        price = data["price"]

        item = ItemModel(name,data["price"])

        try:
            item.insert()
        except:
            return {"message":"An error when inserting the item"},500 # internal server error

        return item.json(), 201 # creating success # 201 ||  # 202 --> accepted but not excuted




    @jwt_required()
    def delete(self,name):
        connection = sqlite3.connect("data.db")  # 1. connect db create cursor
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"  # 2. create query and execute it
        cursor.execute(query, (name,))

        connection.commit()  # 3. commit change and close connection
        connection.close()
        return {"message": "item deleted"}

    @jwt_required()
    def put(self,name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        updated_item = ItemModel(name,data["price"])

        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message": "An error when inserting the item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message": "An error when updating the item"}, 500
        return updated_item.json()



class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")  # 1. connect db create cursor
        cursor = connection.cursor()

        query = "SELECT * FROM items"  # 2. create query and execute it
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({"name":row[0], "price":row[1]})

        connection.close()
        return {"items": items}