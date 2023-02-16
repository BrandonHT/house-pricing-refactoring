"""Dataset cleaner

This script allows the user to fill NA values by two functions.
The first one allows to fill NA values from desired variables using
an specific value. The second one fills all NA values on a given
datafram based on the data type of each column. Both functions
receives a dataframe as parameter and uses the pandas library for
data manipulation.

This script can also be imported as a module.
"""

# importing needed libraries
from typing import Any, List

import pandas as pd


def custom_fill_na_values(
            data: pd.DataFrame,
            variables: List[str],
            new_value: Any
        ):
    """Fill 'NA' values for a given list of variables on a dataframe.

    Args:
        data (pd.DataFrame): the dataframe to be filled.
        variables (List[str]): the variables desired to be filled.
        new_value (Any): the value to be used to fill.

    Returns:
        data_filled (pd.DataFrame): the resulting dataframe after filling
        the custom variables with the given value.
    """
    data_filled = data.copy()
    # for each of the given variables, fill the NA values with the
    # new_value proposed
    for variable in variables:
        data_filled[variable].fillna(new_value, inplace=True)
    return data_filled


def fill_all_na_values(data: pd.DataFrame):
    """Main function to fill 'NA' values of a given dataframe by predifined rules.

    Args:
        data (pd.DataFrame): the dataframe to be filled.

    Returns:
        data_imputed (pd.DataFrame): the resulting dataframe after filling
        the 'NA' values of all columns.
    """
    data_imputed = data.copy()
    for col in data_imputed.columns:
        # for each variable of the dataset, check whether is a numerical or
        # categorical variable.
        if data_imputed[col].dtype in ("float64", "int64"):
            #  For numerical variables, impute the NA with the mean.
            data_imputed[col].fillna(data_imputed[col].mean(), inplace=True)
        else:
            # For categorical variables, impute the NA with the mode.
            data_imputed[col].fillna(data_imputed[col].mode()[0], inplace=True)
    return data_imputed
