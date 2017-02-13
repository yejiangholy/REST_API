from flask import Flask,jsonify

app = Flask(__name__)

# jason is mainly a dictionary in a long string format , which is useful to transfer data
# A REST API returns json after some processing
#stores is a list of dictionary

stores = [
    {
        "name":"my store",
        'items':[
            {
                "name":"item1",
                'price':17.99
            },
            {
                "name":"item2",
                "price":39.00
            }

        ]
    }
]

#POST /store data: {name:}
@app.route('/store', methods =['POST'])
def create_store():
    pass


#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass


#GET /store/
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


#POST /store/<string:name>/item {name: , price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_store_inStore(name):
    pass

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_inStore(name):
    pass


app.run(port=5000)