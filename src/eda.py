import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def heatmap_of_nulls(data: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(25,10))
    sns.heatmap(data=data.isnull(), yticklabels=False, ax=ax)
    fig.savefig("images/heatmap_of_nulls.png")

def collage_of_plots(data: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(25,10))
    sns.countplot(x=data['SaleCondition'])
    sns.histplot(x=data['SaleType'], kde=True, ax=ax)
    sns.violinplot(x=data['HouseStyle'], y=data['SalePrice'],ax=ax)
    sns.scatterplot(x=data["Foundation"], y=data["SalePrice"], palette='deep', ax=ax)
    plt.grid()
    fig.savefig("images/collage_of_plots.png")