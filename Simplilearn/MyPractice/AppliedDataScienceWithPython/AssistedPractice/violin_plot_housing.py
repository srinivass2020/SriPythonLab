"""
Step 1: Create a violin plot for a feature like SalePrice to visualize its distribution and understand its characteristics.
Step 2: Use a pair plot to visualize the relationships between different numerical variables like LotArea, YearBuilt, and SalePrice.
Step 3: Create a heatmap of the correlation matrix to understand the relationships between different numerical features.
Step 4: Use a joint plot to visualize the relation between two numerical variables and their individual distributions, for example, LotArea and SalePrice.
Step 5: Create a swarm plot for a categorical variable like Neighborhood against SalePrice to understand the distribution of prices in each neighborhood.
"""
# python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\housing_data.csv'

def load_data(path=DATA_PATH):
    return pd.read_csv(path)

def plot_violin(df):
    col = 'SalePrice'
    if col not in df:
        print(f"Column {col} not found; skipping violin plot.")
        return
    sns.set_theme(style='whitegrid')
    plt.figure(figsize=(8, 6))
    #sns.violinplot(y=df[col], inner='quartile', color='skyblue')
    #create new dataframe group by neighborhood and sales price
    data_price_neighborhood = df[['Neighborhood', 'SalePrice']].dropna()
    print("Hello ",data_price_neighborhood.head())
    sns.violinplot(x='Neighborhood', y='SalePrice', data=data_price_neighborhood)

    plt.title('Violin plot: SalePrice distribution')
    plt.ylabel('SalePrice')
    plt.tight_layout()
    plt.show()
    plt.close()

def plot_pairplot(df):
    cols = ['LotArea', 'YearBuilt', 'SalePrice']
    present = [c for c in cols if c in df]
    if len(present) < 2:
        print("Not enough columns for pairplot; need at least two of", cols)
        return
    sns.pairplot(df[present].dropna(), diag_kind='kde', plot_kws={'alpha': .6})
    plt.suptitle('Pairplot for numerical features', y=1.02)
    plt.show()
    plt.close()

def plot_heatmap(df):
    num = df.select_dtypes(include=[np.number])
    if num.shape[1] < 2:
        print("Not enough numerical columns for heatmap.")
        return
    corr = num.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='vlag', center=0)
    plt.title('Correlation heatmap (numerical features)')
    plt.tight_layout()
    plt.show()
    plt.close()

def plot_jointplot(df):
    x, y = 'LotArea', 'SalePrice'
    if x not in df or y not in df:
        print(f"Columns {x} and/or {y} not found; skipping jointplot.")
        return
    sns.jointplot(data=df, x=x, y=y, kind='reg', height=8, marginal_kws=dict(bins=30, fill=True))
    plt.suptitle(f'Joint plot: {x} vs {y}', y=1.02)
    plt.show()
    plt.close()

def plot_swarmplot(df):
    cat, val = 'Neighborhood', 'SalePrice'
    if cat not in df or val not in df:
        print(f"Columns {cat} and/or {val} not found; skipping swarmplot.")
        return
    # reduce points per category if dataset is large
    sample_df = df[[cat, val]].dropna()
    if sample_df.shape[0] > 5000:
        sample_df = sample_df.groupby(cat).apply(lambda g: g.sample(n=min(200, len(g)), random_state=0)).reset_index(drop=True)
    plt.figure(figsize=(12, 6))
    sns.swarmplot(x=cat, y=val, data=sample_df, size=3)
    plt.title('Swarm plot: Neighborhood vs SalePrice')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    plt.close()

def main():
    df = load_data()
    plot_violin(df)
    #plot_pairplot(df)
    #plot_heatmap(df)
    #plot_jointplot(df)
    #plot_swarmplot(df)

if __name__ == '__main__':
    main()
