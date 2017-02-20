import sqlite3
from db import db

class ItemModel(db.Model):

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(pricision=2))


    def __init__(self,name,price):
        self.name = name
        self.price = price

    def json(self):
        return {"name":self.name, "price":self.price}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first() # == SELECT * FROM items WHERE name = name LIMIT 1





    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

