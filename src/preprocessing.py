import json
from typing import List

from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder


def __encode_variable(data: DataFrame, column_name: str, categories: List[str]):
    ordinal_encoder = OrdinalEncoder(categories=[categories])
    return ordinal_encoder.fit_transform(data[[column_name]])


def encode_variables(data: DataFrame):
    data_encoded = data.copy()
    with open("msc/map_encoders.json") as encoders_json:
        encoders = json.load(encoders_json)
        for column, categories in encoders.items():
            data_encoded[column] = __encode_variable(data_encoded, column, categories)
        encoders_json.close()
    return data_encoded


def encode_catagorical_columns(data: DataFrame, columns: List[str]):
    data_encoded = data.copy()
    label_encoder = LabelEncoder()
    for column in columns:
        data_encoded[column] = label_encoder.fit_transform(data_encoded[column])
    return data_encoded


def create_interactions(data: DataFrame):
    data_interactions = data.copy()
    
    # multiply columns
    data_interactions['BsmtRating'] = data_interactions['BsmtCond'] * data_interactions['BsmtQual']
    data_interactions['ExterRating'] = data_interactions['ExterCond'] * data_interactions['ExterQual']
    data_interactions['BsmtFinTypeRating'] = data_interactions['BsmtFinType1'] * data_interactions['BsmtFinType2']
    
    # sum columns
    data_interactions['BsmtBath'] = data_interactions['BsmtFullBath'] + data_interactions['BsmtHalfBath']
    data_interactions['Bath'] = data_interactions['FullBath'] + data_interactions['HalfBath']
    data_interactions['PorchArea'] = data_interactions['OpenPorchSF'] + data_interactions['EnclosedPorch'] + data_interactions['3SsnPorch'] + data_interactions['ScreenPorch']
    return 