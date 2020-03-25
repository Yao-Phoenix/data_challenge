import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def gradient_descent():
    
    df = pd.read_csv('nyc-east-river-bicycle-counts.csv')
    x = df['Brooklyn Bridge'].values
    y = df['Manhattan Bridge'].values

    w = 0
    b = 0
    lr = 0.000000001
    num_iter = 1000
    n = len(x)

    for i in range(num_iter):
        y_has = w * x + b
        gradient_w = -(2/n) * sum(x*(y - y_has))
        gradient_b = -(2/n) * sum(y - y_has)
        w -= lr * gradient_w
        b -= lr * gradient_b

    # plt.scatter(x, y)
    # plt.plot(x, b + w * x, c='r')
    # plt.show()

    return w, b


if __name__ == '__main__':
    print(gradient_descent())
