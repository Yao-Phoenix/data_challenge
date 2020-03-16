import pandas as pd

def min_max(data):
    return ((data - data.min()) / (data.max() - data.min()))

def data_clean(Series, name):
    df_data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')
    df = df_data[df_data['Series code'] == Series].set_index('Country code'
            ).iloc[:, 5:]
    df_nan = df.replace({'..': pd.np.nan})
    df_fill = df_nan.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1
            ).fillna(0)
    df_fill[name] = df_fill.sum(axis=1)
    df_sum = df_fill[name]   
    return df_sum

def co2_gdp_plot():

   df_co2 = data_clean('EN.ATM.CO2E.KT', 'CO2-SUM')
   df_gdp = data_clean('NY.GDP.MKTP.CD', 'GDP-SUM')
