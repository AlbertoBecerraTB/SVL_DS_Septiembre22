'''
AUTHENTICATION
Necesitamos el paquete Flask-JWT
JWT (Json Web Toolkit). Lo usaremos para codificar datos de usuarios.
'''
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'dani' # Esto si se sube, deberia estar oculto
api = Api(app)

items = []
'''
Cada recurso es una clase. Hereda de Resource
'''
class Item(Resource):
    def get(selfs, name):
        # Devuelve el primer item, no tendremos mas. None si esta vacio
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404


    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}
        # Si no tiene el content-type json, dará error
        # a no ser que pongamos el force=True
        # silent=True, devuelve None si no está la cabecera
        data = request.get_json(force=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/item/<string:name>')

# Debug=True añade una pagina de error
app.run(debug=True)



