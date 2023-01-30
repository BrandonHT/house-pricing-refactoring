"""
    Hola
"""
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
        if data_imputed[col].dtype in ("float64", "int64"):
            data_imputed[col].fillna(data_imputed[col].mean(), inplace=True)
        else:
            data_imputed[col].fillna(data_imputed[col].mode()[0], inplace=True)
    return data_imputed
