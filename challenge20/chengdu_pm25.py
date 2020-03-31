import pandas as pd
from fbprophet import Prophet

def additive():
    
    df = pd.read_csv('Chengdu_HourlyPM25.csv')
    df_nan = df.replace({-999: pd.np.nan})
    df_fill = df_nan.fillna(method='ffill').fillna(method='bfill')
    df_fill.index = pd.to_datetime(df_fill['Date (LST)'])

    df_fill = df_fill.resample('D').mean()
    data = df_fill.reset_index()
    data.columns = ['ds', 'y']
    
    m = Prophet()
    m.fit(data)

    future = m.make_future_dataframe(periods=365, freq='D')
    forecast = m.predict(future)
    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].iloc[len(data):, :]
    forecast.set_index('ds', inplace=True)
    
    forecast.to_csv('forecast.csv')

    return forecast

if __name__ == '__main__':
    print(additive())
