from copyreg import pickle
from turtle import pd
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import csv, sqlite3, json
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
app.config["DEBUG"] = True

'''
La petición sería:
http://127.0.0.1:5000/api/v1/adv/create_db
'''
@app.route('/api/v1/adv/create_db', methods = ['GET'])
def createdb():

    con = sqlite3.connect('1-Flask/1-Routing/ejercicios/ejercicio 2 Flask_API_retrain_db\ejercicio/advertising.db')
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS t;")
    cur.execute("CREATE TABLE t (TV, radio, newspaper, sales);")

    with open('1-Flask/1-Routing/ejercicios/ejercicio 2 Flask_API_retrain_db\ejercicio/advertising.csv', 'r') as fin:
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['TV'], i['radio'], i['newspaper'], i['sales']) for i in dr]

        cur.executemany("INSERT INTO t (TV, radio, newspaper, sales) VALUES (?,?,?,?);", to_db)

    con.commit()
    con.close()

    return jsonify(list({'TV': i[0], 'radio': i[1], 'newspaper': i[2], 'sales': i[3]} for i in to_db))




"""
La petición sería:
http://127.0.0.1:5000/api/v1/adv_model/predict?TV=180&radio=15&newspaper=60
"""
@app.route('/api/v1/adv_model/predict', methods = ['GET'])
def predict():

    args = request.args
    if 'TV' in args and 'radio' in args and 'newspaper' in args:
        with open('1-Flask/1-Routing/ejercicios/ejercicio 2 Flask_API_retrain_db\ejercicio/advertising.model', 'rb') as archivo_entrada:
            model = pickle.load(archivo_entrada)

        tv = args.get('TV', None)
        radio = args.get('radio', None)
        newspaper = args.get('newspaper', None)

        if tv is None or radio is None or newspaper is None:
            return "Error. Args empty"
        else:
            predictions = model.predict([[float(tv),
            float(radio),
            float(newspaper)]])

            return jsonify({"predictions": list(predictions)})

    else:
        return "Error in args"


'''
http://127.0.0.1:5000/api/v1/adv_model/register?TV=180&radio=15&newspaper=60&sales=12000
'''
@app.route('/api/v1/adv_model/register', methods=['GET', 'POST'])
def new_register():
    args = request.args
    if 'TV' in args and 'radio' in args and 'newspaper' in args and 'sales' in args:

        tv = args.get('TV', None)
        radio = args.get('radio', None)
        newspaper = args.get('newspaper', None)
        sales = args.get('sales', None)

        if tv is None or radio is None or newspaper is None or sales is None:
            return "Error. Args empty"
        else:

            new_register_dict = {'TV': [tv],
                                 'radio': [radio],
                                 'newspaper': [newspaper],
                                 'sales': [sales]}

            con = sqlite3.connect('1-Flask/1-Routing/ejercicios/ejercicio 2 Flask_API_retrain_db\ejercicio/advertising.db')
            cur = con.cursor()

            cur.execute("INSERT INTO t (TV , radio , newspaper , sales) VALUES (?, ?, ?, ?);", (tv, radio, newspaper, sales))
    
            con.commit()
            con.close()          

            return jsonify(new_register_dict)
    else:
        return "Error in args"







'''
http://127.0.0.1:5000/api/v1/adv_model/retrain
'''
@app.route('/api/v1/adv_model/retrain', methods=['GET', 'PUT'])
def retrain():
    try:

        con = sqlite3.connect('1-Flask/1-Routing/ejercicios/ejercicio 2 Flask_API_retrain_db\ejercicio/advertising.db')
        cur = con.cursor()
        data = cur.execute("SELECT * FROM t").fetchall()

        data = pd.DataFrame(data = data, columns = ['TV', 'radio', 'newspaper', 'sales'])

        X_train, X_test, y_train, y_test = train_test_split(data.drop(['sales'],1),
                                                            data['sales'],
                                                            test_size=0.20,
                                                            random_state=42)

        lin_reg = LinearRegression()
        lin_reg.fit(X_train, y_train)

        pickle.dump(lin_reg, open('1-Flask/1-Routing/ejercicios/ejercicio 2 Flask_API_retrain_db\ejercicio/advertising.model', 'wb'))

        return "Finished train successfully"
    except:
        return "Error training"



app.run()