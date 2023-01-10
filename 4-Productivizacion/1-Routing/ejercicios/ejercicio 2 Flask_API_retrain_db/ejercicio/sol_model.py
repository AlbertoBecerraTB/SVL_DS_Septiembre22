'''
En este script se cargan los datos y entrena el modelo
'''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pickle
data = pd.read_csv('data/Advertising.csv')

X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=['sales']),
                                                    data['sales'],
                                                    test_size = 0.20,
                                                    random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

print("MSE: ", mean_squared_error(y_test, lin_reg.predict(X_test)))
print("RMSE: ", np.sqrt(mean_squared_error(y_test, lin_reg.predict(X_test))))