
'''
En este script desarrollaremos los endpoints de api2.py.
Empezamos por
    1. Get all stores
    2. Despues implementamos POST store. Necesitamos request para acceder
    a los datos del POST
    3. GET una tienda concreta.
    4. GET los items de una tienda concreta
    5. Render HTML template
'''
# jsonify convierte un diccionario en un json para devolerlo
from flask import Flask, jsonify, request, render_template

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
Para renderizar un HTML directamente desde un archivo
Flask se vva a buscar a la carpeta templates, donde lo tenemos alojado.
'''
@app.route('/')
def home():
    return render_template('index.html')


'''
POST /store data: {name}
'''
@app.route('/store', methods=['POST'])
def create_store():

    # Recogemos los datos
    request_data = request.get_json()

    # Creamos una nueva tienda
    new_store = {
        'name': request_data['name'],
        'items' : []
    }

    # La guardamos en la "base de datos"
    stores.append(new_store)

    # La devolvemos como return
    return jsonify(new_store)

'''
GET /store/<string:name>
http://127.0.0/store/some_name
'''
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': "Store not found"})


'''
GET /store
'''
@app.route('/store')
def get_stores():
    # Tenemos una lista que no acepta jsonify. Acepta diccionarios.
    return jsonify({'stores': stores})

'''
POST /store/<string>:name/item {name:, price:}
'''
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }

            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': "Store not found"})


'''
GET /store/<string>:name/item
'''
@app.route('/store/<string>:name/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': "Store not found"})



app.run(port=5000)