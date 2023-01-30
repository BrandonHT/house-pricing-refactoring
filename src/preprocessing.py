"""
    Hola
"""
import json
from typing import List

from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder


def __encode_variable(
            data: DataFrame,
            column_name: str,
            categories: List[str]
        ):
    """Performs the encoding of a variable on a given dataframe by using
        a list of categories.

    Args:
        data (DataFrame): a dataframe to be used for the encoding.
        column_name (str): the column desired to be encoded.
        categories (List[str]): the list of categories to encode the
        column of the dataframe given.

    Returns:
        pandas.core.series.Series: the column encoded with the categories given.
    """
    ordinal_encoder = OrdinalEncoder(categories=[categories])
    return ordinal_encoder.fit_transform(data[[column_name]])


def encode_variables(data: DataFrame):
    """Encode variables using predifined categories from a JSON file.

    Args:
        data (DataFrame): a dataframe to be encoded.

    Returns:
        data_encoded (DataFrame): the resulting dataframe after encoding
        the variables using the map_encoders.json file.
    """
    data_encoded = data.copy()
    with open("msc/map_encoders.json", encoding="utf-8") as encoders_json:
        encoders = json.load(encoders_json)
        for column, categories in encoders.items():
            data_encoded[column] = __encode_variable(
                data=data_encoded, column_name=column, categories=categories
            )
            print(type(data_encoded[column]))
        encoders_json.close()
    return data_encoded


def encode_catagorical_columns(data: DataFrame, columns: List[str]):
    """Encode given categorical variables using a label encoder.

    Args:
        data (DataFrame): a dataframe to be encoded.
        columns (List[str]): the list of the desired columns to encode.

    Returns:
        data (DataFrame): the resulting DataFrame after encoding the 
        given variables. 
    """
    data_encoded = data.copy()
    label_encoder = LabelEncoder()
    for column in columns:
        data_encoded[column] = label_encoder.fit_transform(
            data_encoded[column]
        )
    return data_encoded


def create_interactions(data: DataFrame):
    """Generates predefined interactions between variables on a given dataframe.

    Args:
        data (DataFrame): the dataframe on which the interactions will be created.

    Returns:
        data_interactions: the resulting dataframe with the columns created from the
        predefined interactions.
    """
    data_interactions = data.copy()
    # multiply columns
    data_interactions['BsmtRating'] = (
        data_interactions['BsmtCond'] * data_interactions['BsmtQual']
    )
    data_interactions['ExterRating'] = (
        data_interactions['ExterCond'] * data_interactions['ExterQual']
    )
    data_interactions['BsmtFinTypeRating'] = (
        data_interactions['BsmtFinType1'] * data_interactions['BsmtFinType2']
    )
    # sum columns
    data_interactions['BsmtBath'] = (
        data_interactions['BsmtFullBath'] + data_interactions['BsmtHalfBath']
    )
    data_interactions['Bath'] = (
        data_interactions['FullBath'] + data_interactions['HalfBath']
    )
    data_interactions['PorchArea'] = (
        data_interactions['OpenPorchSF'] +
        data_interactions['EnclosedPorch'] +
        data_interactions['3SsnPorch'] +
        data_interactions['ScreenPorch']
    )
    return data_interactions
