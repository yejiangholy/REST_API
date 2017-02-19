from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3



class Item(Resource):
    # parse the request
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be left blank")
    #data = parser.parse_args()
    def get(self,name):
       item = self.find_by_name(name)
       if item:
           return item
       return {"message":"Item not found"},404



    @classmethod
    def find_by_name(cls,name):
        connetion = sqlite3.connect("data.db")
        cursor = connetion.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connetion.close()

        if row:
            return {"item": {"name": row[0], "price": row[1]}}


    @jwt_required()
    def post(self,name):
        if self.find_by_name(name):
            return {"message":"An item with name  '{}' already exist.".format(name)},400 # bad request


        data = Item.parser.parse_args()
        price = data["price"]
        item = {"name": name, "price": price}

        connection = sqlite3.connect("data.db")    # 1. connect db create cursor
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?,?)"    # 2. create query and execute it
        cursor.execute(query,(item["name"],item["price"]))

        connection.commit()             #3. commit change and close connection
        connection.close()


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