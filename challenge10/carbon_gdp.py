import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    df_con = pd.concat([df_co2, df_gdp], axis=1)

    df_max_min = min_max(df_con)

    china = []
    for i in df_max_min[df_max_min.index == 'CHN'].values:
       china.extend(np.round(i, 3).tolist())
    
    xtick_name = []
    xtick_position = []

    for i in range(len(df_max_min)):
        if df_max_min.index[i] in ['CHN', 'USA', 'GBR', 'FRA', 'RUS']:
            xtick_name.append(df_max_min.index[i])
            xtick_position.append(i)

    fig, axes = plt.subplots()

    df_max_min.plot(kind='line', title='GDP-CO2', ax=axes)
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(xtick_position, xtick_name, rotation='vertical')
    plt.show()
    return axes, china

if __name__ == '__main__':
    co2_gdp_plot()

