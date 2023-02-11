"""Main module with pipeline implemented

This script performs all the operations related to the pipeline for
the data. The pipeline implements all the operations present in each
Python file under the src folder.

It uses pandas and scikit-learn libraries for data manipulation
and creation of machine learning models.

To execute this Python script just open a terminal and type the command:
python main.py.
"""
# importing needed libraries
import logging
from statistics import mean

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

# importing needed classes
from config import config

# importing needed modules
from src import cleaning as cln
from src import eda
from src import preprocessing as prcs

# defining predefined set of variables for data manipulation
COLS_TO_DROP = [
                "Id", "Alley", "PoolQC", "MiscFeature", "Fence",
                "MoSold", "YrSold", "MSSubClass", "GarageType",
                "GarageArea", "GarageYrBlt", "GarageFinish",
                "YearRemodAdd", "LandSlope", "BsmtUnfSF",
                "BsmtExposure", "2ndFlrSF", "LowQualFinSF",
                "Condition1", "Condition2", "Heating", "Exterior1st",
                "Exterior2nd", "HouseStyle", "LotShape",
                "LandContour", "LotConfig", "Functional", "BsmtFinSF1",
                "BsmtFinSF2", "FireplaceQu", "WoodDeckSF", "GarageQual",
                "GarageCond", "OverallCond"
           ]

ORDINAL_COLS = [
                "BsmtQual", "BsmtCond", "ExterQual", "ExterCond",
                "KitchenQual", "PavedDrive", "Electrical",
                "BsmtFinType1", "BsmtFinType2", "Utilities",
                "MSZoning", "Foundation", "Neighborhood", "MasVnrType",
                "SaleCondition", "RoofStyle", "RoofMatl"
            ]

FILL_CATEGORICAL = ["BsmtQual", "BsmtCond", "BsmtFinType1", "BsmtFinType2"]

CATEGORICAL_ENCODE = ["Street", "BldgType", "SaleType", "CentralAir"]

NOT_OUTPUT_VARIABLES = [
                        "OverallQual", "ExterCond", "ExterQual", "BsmtCond",
                        "BsmtQual", "BsmtFinType1", "BsmtFinType2",
                        "HeatingQC", "OpenPorchSF", "EnclosedPorch",
                        "3SsnPorch", "ScreenPorch", "BsmtFullBath",
                        "BsmtHalfBath", "FullBath", "HalfBath"
                    ]

GOAL_VARIABLE = "SalePrice"

# max number of leaf nodes for the random forest model
CANDIDATE_MAX_LEAF_NODES = 250


def init_logging():
    """Initialize the basic configuration parameters to save the log messages
        in a external log file.
    """
    try:
        logging.basicConfig(
                            filename='logs/logs.log',
                            level=logging.INFO,
                            filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s'
                        )
    except RuntimeError:
        logging.error("Logging could not start")


def pipeline(data: pd.DataFrame):
    """Performs all cleaning and preprocessing steps on a given dataframe.

    Args:
        data (pd.DataFrame): the dataframe to be processed.

    Returns:
        final_data (pd.DataFrame): a datagrame with no "NA" values and
        columns encoded.
    """
    aux_data = data.copy()
    # dropping variables that are not going to be used in the analysis
    # or predictions
    data_filtered = aux_data.drop(COLS_TO_DROP, axis=1)
    # fill NA values for custom variables with an specific value.
    data_cleaned = cln.custom_fill_na_values(
        data_filtered, FILL_CATEGORICAL, "No"
    )
    # fill all NA values
    data_cleaned = cln.fill_all_na_values(data_cleaned)
    # performs the encoding of some categorical variables
    preprocessed_data = prcs.encode_variables(data_cleaned)
    preprocessed_data = prcs.encode_categorical_columns(
        preprocessed_data, CATEGORICAL_ENCODE
    )
    # create the interactions between variables
    preprocessed_data = prcs.create_interactions(preprocessed_data)
    # drop variables that are not going to be used for the predictions.
    final_data = preprocessed_data.drop(NOT_OUTPUT_VARIABLES, axis=1)
    return final_data


def generate_submissions(
            ids: pd.core.series.Series,
            model: RandomForestRegressor,
            data: pd.DataFrame,
            path_to_save: str
        ):
    """Generate a new dataset with the predictions generated from the
        dataframe given.

    Args:
        ids (pd.core.series.Series): the ids to index the results.
        model (RandomForestRegressor): a pretrained random forest model.
        data (pd.DataFrame): the dataset which will be used to generate
        the predictions.
        path_to_save (str): the relative path where the results are going
        to be saved.

    Output:
        a csv file with the predictions indexed by the ids given.
    """
    # generate predictions using a given model
    price = model.predict(data)
    # create the predictions dataset using the ids to index each entry
    submission = pd.DataFrame({
        "Id": ids,
        "SalePrice": price
    })
    submission.to_csv(path_to_save, index=False)


if __name__ == "__main__":
    init_logging()
    config_values = config.ConfigValues()
    # read train and test data
    data_train = pd.DataFrame()
    data_test = pd.DataFrame()
    try:
        data_train = pd.read_csv(config_values.path_train())
        data_test = pd.read_csv(config_values.path_test())
    except FileNotFoundError:
        data_train, data_test = None, None
        logging.error("The path for train or test dataset is wrong.")
    if not (data_train.empty and data_test.empty):
        # separate the ids to index each entry
        output_ids = data_test["Id"]
        # generate the plots from EDA analysis
        try:
            eda.heatmap_of_nulls(data_train, config_values.path_heatmap())
            eda.collage_of_plots(data_train, config_values.path_collage())
        except FileNotFoundError:
            logging.error("The path to save one or both plots is wrong.")
        # execute the pipeline operations over each dataset
        final_data_train = pipeline(data_train)
        final_data_test = pipeline(data_test)
        # define the input and output variables
        y = final_data_train[GOAL_VARIABLE]
        X = final_data_train.drop(GOAL_VARIABLE, axis=1)
        # create a Random forest regressor model, train it and evalute it
        rf_model = RandomForestRegressor(
                                        max_leaf_nodes=CANDIDATE_MAX_LEAF_NODES
                                    )
        rf_model.fit(X, y)
        score = cross_val_score(rf_model, X, y, cv=10)
        logging.info('The mean score of 10 folds in '
                     'cross validation is: %s', mean(score))
        # generate a new file with the predictions of the test dataset
        try:
            generate_submissions(
                                output_ids,
                                rf_model,
                                final_data_test,
                                config_values.path_submissions()
                            )
        except OSError:
            logging.error("The path to save the submissions is wrong.")
