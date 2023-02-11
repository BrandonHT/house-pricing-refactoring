"""Data preprocessing and pipeline testing

This script test all the functions related to the EDA process of the code.
Some fixtures were defined in order to return the paths associated to each
plot that will be generated when testing them.

The output of the tests will be stored under the *test_results* folder.

One last test function was included in order to remove all the content of
the *test_results* folder once the previuos tests were evaluated.
"""

import logging

import pandas as pd
import pytest

from src import cleaning as cln
from src import preprocessing as prcs


def cols_to_drop():
    """return a set of columns to be dropped from a dataframe."""
    return [
            "Id", "Alley", "PoolQC", "MiscFeature", "Fence", "MoSold",
            "YrSold", "MSSubClass", "GarageType", "GarageArea",
            "GarageYrBlt", "GarageFinish", "YearRemodAdd", "LandSlope",
            "BsmtUnfSF", "BsmtExposure", "2ndFlrSF", "LowQualFinSF",
            "Condition1", "Condition2", "Heating", "Exterior1st",
            "Exterior2nd", "HouseStyle", "LotShape", "LandContour",
            "LotConfig", "Functional", "BsmtFinSF1", "BsmtFinSF2",
            "FireplaceQu", "WoodDeckSF", "GarageQual", "GarageCond",
            "OverallCond"
           ]


def not_output_variables():
    """return a set of columns that are not of interest in the problem."""
    return [
            "OverallQual", "ExterCond", "ExterQual", "BsmtCond", "BsmtQual",
            "BsmtFinType1", "BsmtFinType2", "HeatingQC", "OpenPorchSF",
            "EnclosedPorch", "3SsnPorch", "ScreenPorch", "BsmtFullBath",
            "BsmtHalfBath", "FullBath", "HalfBath"
        ]


def categorical_encode():
    """return a set of columns to be encoded."""
    return ["Street", "BldgType", "SaleType", "CentralAir"]


def read_data(data_path):
    """Read a dataset from a path given and return it.

    Args:
        data_path (str): path where the data is located.

    Returns:
        data (DataFrame): the dataset read with Pandas library.
    """
    data = pd.read_csv(data_path)
    return data


@pytest.fixture(scope="module", name="data_path")
def path():
    """return the path of the train dataset."""
    return "data/train.csv"


def test_pipeline(data_path):
    """Simulates the pipeline process from cleaning to encoding.

    Args:
        data_path (str): the path where the dataset is located.

    Raises:
        fnfe: FileNotFoundError if the dataset was not found.
        asserr: AssertionError if it was not possible to drop the
        columns.
        asserr: AssertionError if the encoding process was not
        successfully executed.
        asserr: AssertionError if the interactions could no be created.
        asserr: AssertionError if the final dataframe has at least one
        non-numerical variables.
    """
    try:
        data = read_data(data_path)
    except FileNotFoundError as fnfe:
        logging.error("The source dataset was not found.")
        raise fnfe
    try:
        data_filtered = data.drop(cols_to_drop(), axis=1)
    except AssertionError as asserr:
        logging.error("The columns to drop cannot be deleted.")
        raise asserr
    try:
        data_cleaned = cln.fill_all_na_values(data_filtered)
        preprocessed_data = prcs.encode_variables(data_cleaned)
        encoded_data = prcs.encode_categorical_columns(
                                                        preprocessed_data,
                                                        categorical_encode()
                                                    )
    except AssertionError as asserr:
        logging.error("The encoding process was not executed successfully.")
        raise asserr
    try:
        interacted_data = prcs.create_interactions(encoded_data)
    except AssertionError as asserr:
        logging.error("The interactions were not created successfully.")
        raise asserr
    try:
        final_data = interacted_data.drop(not_output_variables(), axis=1)
        assert len(final_data.select_dtypes("object").columns) == 0
    except AssertionError as asserr:
        logging.error("The final dataframe has at least one non-numerical column \
            after the preprocessing of the data.")
        raise asserr
