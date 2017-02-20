import sqlite3

class ItemModel:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def json(self):
        return {"name":self.name, "price":self.price}


    def insert(self):
        connection = sqlite3.connect("data.db")  # 1. connect db create cursor
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?,?)"  # 2. create query and execute it
        cursor.execute(query, (self.name, self.price))

        connection.commit()  # 3. commit change and close connection
        connection.close()



    @classmethod
    def find_by_name(cls, name):
        connetion = sqlite3.connect("data.db")
        cursor = connetion.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connetion.close()

        if row:
            return cls(row[0],row[1])


    def update(self):
        connection = sqlite3.connect("data.db")  # 1. connect db create cursor
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"  # 2. create query and execute it
        cursor.execute(query, (self.price, self.name))

        connection.commit()  # 3. commit change and close connection
        connection.close()
