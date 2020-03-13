import pandas as pd


def clean():
    df = pd.read_csv('earthquake.csv')
    df_clean = df[['time', 'latitude', 'longitude', 'depth', 'mag']]
    region = []
    for line in df.place.values:
        region.append(line.split(',')[-1])
    region = pd.DataFrame(region, columns=['region'])
    df_clean = pd.concat([df_clean, region], axis=1)
    df_clean = df_clean.drop_duplicates().dropna()
    return df_clean


def mag_region():
    df_clean = clean()
     
    df_clean['times'] = 0
    bins = [0, 2, 5, 7, 9, 100]
    df_clean.mag = pd.cut(df_clean.mag, bins=bins, right=False, labels=[
        'micro', 'light', 'strong', 'major', 'great'])
    df_final = df_clean.groupby(by=['mag', 'region'])['times'].count().reset_index()
    df_final.columns = ['mag', 'region', 'times']
    df_final.sort_values(by='times', ascending=False, inplace=True)
    df_final.drop_duplicates('mag', inplace=True)
    df_final.set_index(df_final.mag, inplace=True)
    df_final.drop('mag', axis=1, inplace=True)
    return df_final

if __name__ == '__main__':
    print(mag_region())
