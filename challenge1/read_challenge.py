import pandas as pd

def convert(file):
    df = pd.read_json(file)[:1000]
    return df.to_hdf('user_study.h5', key='data')

if __name__ == '__main__':
    convert('users_data.json')
