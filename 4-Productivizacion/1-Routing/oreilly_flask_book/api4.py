'''
Necesitamos instalar Flask-RESTFul
Resource es todo lo que devuelve la api, tal y como lo modelemos nosotros
    1. Primero montamos la clase, que heredará de Resource
    2. Realizamos el add_resource para indicar que todo lo enrutado en esa sentencia, pertenece a esa clase
    3. Vamos añadiendo metodos dentro de la clase, correspondientes a los get, post...
'''
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []
'''
Cada recurso es una clase. Hereda de Resource
'''
class Item(Resource):
    def get(selfs, name):
        for item in items:
            if item['name'] == name:
                return item # No hace falta jsonify
        # Para que no devuelva null
        # Devuelve 404 de elemento no encontrado
        return {'item': None}, 404
    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        # Para que la app sepa que se ha posteado
        # 201 para crear
        return item, 201

'''
Ahora el recurso Student estará accesible por la API
http://127.0.0.1:5000/student/Rolf
'''
api.add_resource(Item, '/item/<string:name>')

app.run()



