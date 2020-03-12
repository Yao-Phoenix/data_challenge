import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot():
    df = sns.load_dataset('titanic')
    df['age'].fillna(df['age'].median(), inplace=True)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    sns.distplot(df['age'], ax=axes[0])
    sns.countplot(x='sex', hue='alive', data=df, ax=axes[1])
    sns.countplot(x='class', hue='alive', data=df, ax=axes[2])
    plt.show()

    return axes

if __name__ == '__main__':
    plot()
