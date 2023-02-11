"""EDA testing

This script test all the functions related to the EDA process of the code.
Some fixtures were defined in order to return the paths associated to each
plot that will be generated when testing them.

The output of the tests will be stored under the *test_results* folder.

One last test function was included in order to remove all the content of
the *test_results* folder once the previuos tests were evaluated.
"""

import logging
import os

import pandas as pd
import pytest

from src import eda


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


@pytest.fixture(scope="module", name="heatmap_path")
def heatmap():
    """return the path where the heatmap is going to be saved."""
    return "test/test_results/heatmap_result.png"


@pytest.fixture(scope="module", name="collage_path")
def collage():
    """ return the path where the collage of plots is going to be saved."""
    return "test/test_results/collage_result.png"


def test_heatmap_of_nulls(data_path, heatmap_path):
    """test if the heatmap of nulls plot could be created from a dataset.

    Args:
        data_path (str): the path where the dataset is located.
        heatmap_path (str): the path where the plot is going to be saved.

    Raises:
        fnfe_data: FileNotFoundError if the dataset was not found.
        fnfe_res: FileNotFoundError if the output was not generated.
    """
    try:
        data = read_data(data_path)
    except FileNotFoundError as fnfe_data:
        logging.error("File to generate the heatmap plot not found.")
        raise fnfe_data
    try:
        eda.heatmap_of_nulls(data, heatmap_path)
        os.path.exists(heatmap_path)
    except FileNotFoundError as fnfe_res:
        logging.error("Heatmap was not generated.")
        raise fnfe_res


def test_collage(data_path, collage_path):
    """test if the collage of plots could be created from a dataset.

    Args:
        data_path (str): the path where the dataset is located.
        collage_path (str): the path where the plot is going to be saved.

    Raises:
        fnfe_data: FileNotFoundError if the dataset was not found.
        fnfe_res: FileNotFoundError if the output was not generated.
    """
    try:
        data = read_data(data_path)
    except FileNotFoundError as fnfe_data:
        logging.error("File to generate the heatmap plot not found.")
        raise fnfe_data
    try:
        eda.heatmap_of_nulls(data, collage_path)
        os.path.exists(collage_path)
    except FileNotFoundError as fnfe_res:
        logging.error("Collage of plots was not generated.")
        raise fnfe_res
