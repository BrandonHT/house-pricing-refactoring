"""Cleaning testing

This script test all the functions related to the cleaning process of the code.
Some fixtures were defined in order to return the path associated to the
source dataset and some custom variables to remove their NA values.

The expected result of each function is to get a number of zero NA values after
the cleaning process.
"""

import logging

import pandas as pd
import pytest

from src import cleaning


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


@pytest.fixture(scope="module", name="variables")
def variables_to_fill():
    """return the list of variables to fill the NA values"""
    return ["BsmtQual", "BsmtCond", "BsmtFinType1", "BsmtFinType2"]


def test_custom_fill_na_values(data_path, variables):
    """Fill the NA valaues for a given variables with a predefined value.

    Args:
        data_path (str): the path where the dataset is located.
        variables (List[str]): the variables of the dataset that will be
        filled.

    Raises:
        fnfe_data: FileNotFoundError if the dataset was not found.
        asserr: AssertionError if there are NA values after the
        filling process.
    """
    try:
        data = read_data(data_path)
    except FileNotFoundError as fnfe_data:
        logging.error("The source dataset was not found.")
        raise fnfe_data
    try:
        cleaned_data = cleaning.custom_fill_na_values(data, variables, "No")
        subsampled_data = cleaned_data[variables]
        assert subsampled_data.isna().sum().sum() == 0
    except AssertionError as asserr:
        logging.error("The NA values were not filled well.")
        raise asserr


def test_fill_all_na_values(data_path):
    """Fill all the NA values of a dataset with the most popular value
    of each variable.

    Args:
        data_path (str): the path where the dataset is located.

    Raises:
        fnfe_data: FileNotFoundError if the dataset was not found.
        asserr: AssertionError if there are NA values after the
        filling process.
    """
    try:
        data = read_data(data_path)
    except FileNotFoundError as fnfe_data:
        logging.error("The source dataset was not found.")
        raise fnfe_data
    try:
        cleaned_data = cleaning.fill_all_na_values(data)
        assert cleaned_data.isna().sum().sum() == 0
    except AssertionError as asserr:
        logging.error("The NA values were not filled well.")
        raise asserr
