from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
import sklearn
import pickle
import numpy as np

app = Flask(__name__)
app.config['DEBUG'] = True

root = '4-Productivizacion/1-Routing/ejercicios/ejercicio 2 Flask_API_retrain_db/ejercicio/'
model = pickle.load(open(root + 'advertising.model', 'rb'))

# POST {"TV":, "radio":, "newspaper":} -> It returns the sales prediction for input investments
@app.route('/predict', methods=['POST'])
def get_predict():

    # Get current time for the PREDICTIONS table
    str_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Establish SQLITE3 connection
    conn = sqlite3.connect(root + "advertising.db")
    crs = conn.cursor()

    # Get POST JSON data
    data = request.get_json()
    tv = data["TV"]
    radio = data["radio"]
    newspaper = data["newspaper"]

    # Model prediciton
    pred = model.predict(np.array([[tv, radio, newspaper]]))[0]

    # Save prediction in PREDICTIONS table
    crs.execute(''' INSERT INTO PREDICTIONS(pred_date,TV,radio,newspaper,prediction)
                    VALUES(?,?,?,?,?) ''', (str_time, tv, radio, newspaper, pred))
    conn.commit()
    conn.close()
    return str(pred), 200

# POST {"TV":, "radio":, "newspaper":, "sales":} -> Add rows to TRAINING table
@app.route("/update", methods=["POST"])
def update_training():
    # Get current time for the PREDICTIONS table
    conn = sqlite3.connect(root + "advertising.db")
    crs = conn.cursor()

    # Establish SQLITE3 connection
    str_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Get POST JSON data and write it
    data = request.get_json()
    for sample in data:
            crs.execute(''' INSERT INTO TRAINING(date,TV,radio,newspaper,sales)
                            VALUES(?,?,?,?,?) ''', (str_time,
                                                    sample["TV"], 
                                                    sample["radio"], 
                                                    sample["newspaper"], 
                                                    sample["sales"]))

    conn.commit()
    conn.close()
    return jsonify(data), 201

# PUT {"TV":, "radio":, "newspaper":, "sales":} -> Add rows to TRAINING table
@app.route("/retrain", methods=["PUT"])
def do_retrain():
    # Get current time for the PREDICTIONS table
    conn = sqlite3.connect(root + "advertising.db")
    crs = conn.cursor()
    data = crs.execute("SELECT TV, radio, newspaper, sales FROM TRAINING").fetchall()
    conn.close()

    data = np.array(data)
    model.fit(data[:,:-1], data[:,-1])
    
    pickle.dump(model, open(root + "advertising.model", "wb"))

    return jsonify({"Message":"Model trained successfully", "Path": root + 'advertising.model'}), 201

app.run(port=4000)