import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

def beijing(n):

    df = pd.read_csv('beijing_house_price.csv')
    df_drop = df.dropna().drop_duplicates()
    feature = df_drop.corr().sort_values(by='每平米价格', ascending=False
            ).iloc[1:4].index
    X = df_drop[feature]
    y = df_drop['每平米价格']

    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=10)
    poly = PolynomialFeatures(degree=n, include_bias=True)
    poly_X_train = poly.fit_transform(X_train)
    poly_X_test = poly.fit_transform(X_test)
    model = LinearRegression()
    model.fit(poly_X_train, y_train)
    pred = model.predict(poly_X_test)
    mae = mean_absolute_error(y_test, pred)

    return mae

if __name__ == '__main__':
    print(beijing(2))
