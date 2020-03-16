import pandas as pd

def co2():

    df_data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')
    df_series = df_data[df_data['Series code'] == 'EN.ATM.CO2E.KT'
            ].set_index('Country name')
    df_series.drop(df_series.columns[:5], axis=1, inplace=True)
    df_series = df_series.replace({'..': pd.np.nan})
    data = df_series.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data.dropna(how='all', inplace=True)
    df_sum = data.sum(axis=1)

    df_country = pd.read_excel('ClimateChange.xlsx', sheetname='Country'
            ).set_index('Country name')
    df_con = pd.concat([df_sum, df_country['Income group']], axis=1).reset_index()
    df_con.columns = ['Country name', 'Sum emissions', 'Income group']
    df_highest = df_con.sort_values(by='Sum emissions', ascending=False
            ).groupby('Income group').head(1).set_index('Income group')
    df_highest.columns = ['Highest emission country', 'Highest emissions']
    df_lowest = df_con.sort_values(by='Sum emissions') .groupby('Income group'
            ).head(1).set_index('Income group')
    df_lowest.columns = ['Lowest emission country', 'Lowest emissions']
    df_Sum = df_con.groupby('Income group')['Sum emissions'].sum()

    results = pd.concat([df_Sum, df_highest, df_lowest], axis=1)
    return results

if __name__ == '__main__':
    print(co2())

