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
# importing needed libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def heatmap_of_nulls(data: pd.DataFrame):
    """Create a heatmap with the NA values for each variable of a
        given dataframe.

    Args:
        data (pd.DataFrame): a dataset to be analysed.

    Output:
        an image with the plot generated.
    """
    # create a space for the plot
    fig, axis = plt.subplots(figsize=(25, 10))
    # generate the heatmap and save it
    sns.heatmap(data=data.isnull(), yticklabels=False, axis=axis)
    fig.savefig("images/heatmap_of_nulls.png")


def collage_of_plots(data: pd.DataFrame):
    """Create a mix of plots for specific variables from a dataset given.

    Args:
        data (pd.DataFrame): a dataset to be analysed.

    Output:
        an image with the mix of plots generated.
    """
    # create a space for the plot
    fig, axis = plt.subplots(figsize=(25, 10))
    # generate several plots of specific variables of the dataset
    sns.countplot(x=data['SaleCondition'])
    sns.histplot(x=data['SaleType'], kde=True, axis=axis)
    sns.violinplot(x=data['HouseStyle'], y=data['SalePrice'], axis=axis)
    sns.scatterplot(x=data["Foundation"], y=data["SalePrice"],
                    palette='deep', axis=axis)
    # integrate all plots in a single image and save it
    plt.grid()
    fig.savefig("images/collage_of_plots.png")
