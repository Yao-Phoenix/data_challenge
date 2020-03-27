import pandas as pd
from datetime import datetime

def quarter_volume():

    df = pd.read_csv('GOOGL.csv')
    df.set_index('Date', inplace=True)
    df.index = pd.to_datetime(df.index)
    
    df = df.resample('Q').agg({'Open': 'mean', 'High': 'mean',
        'Low': 'mean', 'Close': 'mean',
        'Adj Close': 'mean', 'Volume': 'sum'})
    df = df.sort_values(by='Volume', ascending=False)
    
    return df


if __name__ == '__main__':
    print(quarter_volume())
