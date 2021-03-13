import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_boston
boston_data = load_boston()

X = pd.DataFrame(boston_data.data, columns = boston_data.feature_names)
Y = pd.DataFrame(boston_data.target)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

lin_reg = linear_model.LinearRegression()
lin_reg.fit(x_train, y_train)

print(lin_reg.coef_)

y_pred = lin_reg.predict(x_test)
print(y_pred)

from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred))
