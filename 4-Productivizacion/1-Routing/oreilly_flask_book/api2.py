
'''
En este script crearemos los primeros GETs y POSTs.
de tiendas. Solo los endpoints, en el siguiente script los desarrollamos.
'''
from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }

]
'''
POST /store data: {name}
'''
@app.route('/store', methods=['POST'])
def create_store():
    pass

'''
GET /store/<string:name>
http://127.0.0/store/some_name
'''
@app.route('/store/<string:name>')
def get_store(name):
    pass

'''
GET /store
'''
@app.route('/store')
def get_stores():
    pass

'''
POST /store/<string>:name/item {name:, price:}
'''
@app.route('/store/<string>:name/item', methods=['POST'])
def create_item_in_store():
    pass


'''
GET /store/<string>:name/item
'''
@app.route('/store/<string>:name/item')
def get_items_in_store(name):
    pass



app.run(port=5000)