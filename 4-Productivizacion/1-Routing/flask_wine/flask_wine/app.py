from flask import Flask, request, jsonify
import numpy as np
import pickle as pkl
import json


app = Flask(__name__)
app.config['DEBUG'] = True

modelfile = '4-Productivizacion\\1-Routing\\flask_wine\\flask_wine\\models\\final_prediction.pickle'
model = pkl.load(open(modelfile, 'rb'))
d_wines = {0: "tinto", 1: "blanco", 2: "rosado"}

@app.route('/health', methods=['GET'])
def health():
    return "everything OK here"

@app.route('/score', methods=['POST'])
def makecalc():
    data = request.get_json().values()
    data = np.array(list(data)).reshape(1, -1)
    prediction = int(model.predict(data)[0])
    prediction = d_wines[prediction]
    return f'<h1>¿Cuál es mi vino favorito?</h1><p>Mi Vino favorito es el {prediction}</p>'

if __name__ == "__main__":
    print("hello")
    app.run(debug=False)