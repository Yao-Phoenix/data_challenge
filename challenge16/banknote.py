import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

def selection():
    
    df_train = pd.read_csv('banknote_train.csv')
    X_train, X_test, y_train, y_test = train_test_split(
            df_train.iloc[:, :-1], df_train['class'], test_size=0.3)
    algorithm_name = [
            'LogisticRegression',
            'RandomForestClassifier',
            'DecisionTreeClassifier',
            'KNeighborsClassifier',
            'SVC'
            ]
    algorithm = [
            LogisticRegression(),
            RandomForestClassifier(),
            DecisionTreeClassifier(),
            KNeighborsClassifier(n_neighbors=2),
            SVC()
            ]

    acc = []
    for alg in algorithm:
        model = alg
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        acc.append(accuracy_score(y_test, pred))

    model = algorithm[np.argmax(acc)]
    return model

def identify():
    
    df_train = pd.read_csv('banknote_train.csv')
    df_test = pd.read_csv('banknote_test.csv')
    model = selection()
    model.fit(df_train.iloc[:, :-1], df_train['class'])
    df_test['class'] = model.predict(df_test)
    
    return df_test

if __name__ == '__main__':
    identify()
