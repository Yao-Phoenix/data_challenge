import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot():
    df = sns.load_dataset('titanic')
#    df['age'].fillna(df['age'].median(), inplace=True) 缺失值填充
    sns.set_style('white') # 设置背景风格
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    #删除缺失值
    sns.distplot(df['age'].dropna(), ax=axes[0])
    sns.countplot(x='sex', hue='alive', data=df, ax=axes[1])
    sns.countplot(x='class', hue='alive', data=df, ax=axes[2])
    plt.show()

    return axes

if __name__ == '__main__':
    plot()
