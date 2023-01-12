'''
En este script se cargan los datos y entrena el modelo
'''
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import pickle

root = '4-Productivizacion/1-Routing/ejercicios/ejercicio 2 Flask_API_retrain_db/ejercicio/'
data = pd.read_csv(root + 'Advertising.csv')

X = data.drop(columns=['sales'])
y = data['sales']

lin_reg = LinearRegression()
lin_reg.fit(X, y)

ls_metrics = -1 * cross_val_score(lin_reg, X, y, cv=5, scoring='neg_mean_squared_error')
mse = np.mean(ls_metrics)
rmse = mse ** .5

print("MSE: ", mse)
print("RMSE: ", rmse)

pickle.dump(lin_reg, open(root + 'advertising.model', 'wb'))