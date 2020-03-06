import sqlite3
import pandas as pd

def count(file, user_id):
    sql_con = sqlite3.connect(file)
    df = pd.read_sql('select minutes, user_id from data', con=sql_con)
    if user_id in df['user_id']:
        sum_minutes = df[df['user_id'] == user_id]['minutes'].sum()
        return sum_minutes
    else:
        return 0

if __name__ == '__main__':
    print(count('users_data.sqlite', 8490))
