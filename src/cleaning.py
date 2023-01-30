from typing import List, Any

import pandas as pd


def custom_fill_na_values(data: pd.DataFrame, variables: List[str], new_value: Any):
    data_filled = data.copy()
    for variable in variables:
        data_filled[variable].fillna(new_value, inplace=True)
    return data_filled

def fill_all_na_values(data: pd.DataFrame):
    data_imputed = data.copy()
    for col in data_imputed.columns:
        if(
            (data_imputed[col].dtype == 'float64') or 
            (data_imputed[col].dtype == 'int64')):
                data_imputed[col].fillna(data_imputed[col].mean(), inplace=True)
        else:
             data_imputed[col].fillna(data_imputed[col].mode()[0], inplace=True)
    return data_imputed