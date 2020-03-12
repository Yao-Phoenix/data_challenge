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

if __name__ == '__main__':
    clean()
