"""Explaratory data analysis

This script performs a simple EDA using the matplotlib and seaborn
libraries for data visualization. Also this script allows the user
to save the resulting plots into the images folder in the same project.

The EDA is composed by a single heatmap of null values, which represents
the presence or absence of values for one or more variables in each 
register of a dataset given. The second one is a mix of plots to
make explicit the dispersion and distribution of the values for
some variables. 

This script can also be imported as a module.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def heatmap_of_nulls(data: pd.DataFrame):
    fig, axis = plt.subplots(figsize=(25, 10))
    sns.heatmap(data=data.isnull(), yticklabels=False, axis=axis)
    fig.savefig("images/heatmap_of_nulls.png")


def collage_of_plots(data: pd.DataFrame):
    fig, axis = plt.subplots(figsize=(25, 10))
    sns.countplot(x=data['SaleCondition'])
    sns.histplot(x=data['SaleType'], kde=True, axis=axis)
    sns.violinplot(x=data['HouseStyle'], y=data['SalePrice'], axis=axis)
    sns.scatterplot(x=data["Foundation"], y=data["SalePrice"],
                    palette='deep', axis=axis)
    plt.grid()
    fig.savefig("images/collage_of_plots.png")
