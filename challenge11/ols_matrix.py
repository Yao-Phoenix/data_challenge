import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from decimal import Decimal

def calculate_w():

    df = pd.read_csv('nyc-east-river-bicycle-counts.csv')
    X = df['Brooklyn Bridge']
    y = df['Manhattan Bridge']
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = LinearRegression()
    model.fit(X.values.reshape(len(X), 1), y.values)
    w = np.round(model.coef_[0], 2)
    b = np.round(model.intercept_, 2)
    w = Decimal(w).quantize('0.00')
    b = Decimal(b).quantize('0.00')
    return w, b

'''
def calculate_w():

    df = pd.read_csv('nyc-east-river-bicycle-counts.csv')
    X = df['Brooklyn Bridge'].values
    y = df['Manhattan Bridge'].values

    n = len(X)
    w = np.round(float((n*sum(X*y) - sum(X)*sum(y))/(n*sum(X*X) - sum(X)*sum(X))), 2)
    b = np.round(float((sum(X*X)*sum(y) - sum(X)*sum(X*y))/(n*sum(X*X)-sum(X)*sum(X))), 2)
    return w, b
'''

if __name__ == '__main__':
    print(calculate_w())
