
''''
Script inicial basico donde hacemos un hola mundo



En Anaconda viene ya instalado Flask
Importamos la clase Flask del paquete flask.
'''
from flask import Flask


'''
Instanciamos un objeto de Flask
El __name__ simplemente le asigna un normbre único aleatorio a la app.
'''
app = Flask(__name__)

'''
Utilizamos un decorator para enrutar las peticiones. '/' significa que está
accediendo a la home page de la API, a la raiz. Al ser un decorator, utilizará
acciones dentro del metodo route de Flask, después llamará a la funcion
que creamos debajo y finalmente acabará con otras acciones de la funcion route.
'''
@app.route('/')
def home():
    return "Hello world!"

'''
Dejamos corriendo la app. Podemos especificar el puerto, aunque no es obligatorio.
Si esto da algun error, es que igual tenemos un puerto ya ocupado
Asegurate que estas en la carpeta correcta y ejecuta "python api1.py"
127.0.0.1 es una dirección del propio ordenador, como locahost. Es el edpoint.
'''
app.run(port=5000)