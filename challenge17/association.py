import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules as rules

def rule():

    df = pd.read_csv('shopping_data.csv')
    dataset = df.stack().groupby(level=0).apply(list).tolist()

    te = TransactionEncoder()  
    te_ary = te.fit_transform(dataset)

    data = pd.DataFrame(te_ary, columns=te.columns_)
                        
    frequent_itemsets = apriori(data, min_support=0.05, use_colnames=True)

    association_rules = rules(
            frequent_itemsets, metric="confidence", min_threshold=0.2)

    return frequent_itemsets, association_rules


if __name__ == '__main__':
    print(rule())
