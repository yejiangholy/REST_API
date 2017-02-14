from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

# jason is mainly a dictionary in a long string format , which is useful to transfer data
# A REST API returns json after some processing
#stores is a list of dictionary

stores = [
    {
        "name":"my store",
        "items":[
            {
                "name":"item1",
                "price":17.99
            },
            {
                "name":"item2",
                "price":39.00
            }

        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

#POST /store data: {name:}
@app.route('/store', methods =['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name":request_data["name"],
        "items":[]
    }
    stores.append(new_store)
    return jsonify(new_store)


#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message":"store not exist"})


#GET /store/
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


#POST /store/<string:name>/item {name: , price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_store_inStore(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_Item = {
                "name": request_data["name"],
                "price":request_data["price"]
            }
            store["items"].append(new_Item)
            return jsonify(new_Item)

    return jsonify({"message":"store not exist"})





#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_inStore(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items":store["items"]})

    return jsonify({"message":"store not exist"})


app.run(port=5000)