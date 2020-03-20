import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from decimal import Decimal

def caculate_w():

    df = pd.read_csv('nyc-east-river-bicycle-counts.csv')
    X = df['Brooklyn Bridge']
    y = df['Manhattan Bridge']
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = LinearRegression()
    model.fit(X.values.reshape(len(X), 1), y.values)
    w = float(Decimal(model.coef_[0]).quantize(Decimal('0.00')))
    b = float(Decimal(model.intercept_).quantize(Decimal('0.00')))
    return w, b

'''
def caculate_w():

    df = pd.read_csv('nyc-east-river-bicycle-counts.csv')
    X = df['Brooklyn Bridge'].values
    y = df['Manhattan Bridge'].values

    n = len(X)
    w1 = ((n*sum(X*y) - sum(X)*sum(y))/(n*sum(X*X) - sum(X)*sum(X)))
    w0 = ((sum(X*X)*sum(y) - sum(X)*sum(X*y))/(n*sum(X*X)-sum(X)*sum(X)))
    w = float(Decimal(w1).quantize(Decimal('0.00')))
    b = float(Decimal(w0).quantize(Decimal('0.00')))
    return w, b


def caculate_w():
    
    df = pd.read_csv("nyc-east-river-bicycle-counts.csv", index_col=0)

    x = df['Brooklyn Bridge'].values
    x = x.reshape(len(x), 1)
    x = np.matrix(np.concatenate((np.ones_like(x), x), axis=1))

    y = df['Manhattan Bridge'].values
    y = np.matrix(y.reshape(len(y), 1)) 

    W = (x.T * x).I * x.T * y 
    b = round(float(W[0]), 2)
    w = round(float(W[1]), 2)
                                            
    return w, b
'''

if __name__ == '__main__':
    print(caculate_w())
