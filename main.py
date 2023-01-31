"""Main module with pipeline implemented

This script performs all the op

"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

from src import cleaning as cln
from src import eda
from src import preprocessing as prcs

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

CANDIDATE_MAX_LEAF_NODES = 250


def pipeline(data: pd.DataFrame):
    """Performs all cleaning and preprocessing steps on a given dataframe.

    Args:
        data (pd.DataFrame): the dataframe to be processed.

    Returns:
        final_data (pd.DataFrame): a datagrame with no "NA" values and
        columns encoded.
    """
    aux_data = data.copy()
    data_filtered = aux_data.drop(COLS_TO_DROP, axis=1)
    data_cleaned = cln.custom_fill_na_values(
        data_filtered, FILL_CATEGORICAL, "No"
    )
    data_cleaned = cln.fill_all_na_values(data_cleaned)
    preprocessed_data = prcs.encode_variables(data_cleaned)
    preprocessed_data = prcs.encode_catagorical_columns(
        preprocessed_data, CATEGORICAL_ENCODE
    )
    final_data = preprocessed_data.drop(NOT_OUTPUT_VARIABLES, axis=1)
    return final_data


def generate_submissions(
            ids: pd.core.series.Series,
            model: RandomForestRegressor,
            data: pd.DataFrame
        ):
    """Generate a new dataset with the predictions generated from the
        dataframe given.

    Args:
        ids (pd.core.series.Series): the ids to index the results.
        model (RandomForestRegressor): a pretrained random forest model.
        data (pd.DataFrame): the dataset which will be used to generate
        the predictions.

    Output:
        a csv file with the predictions indexed by the ids given.
    """
    price = model.predict(data)
    submission = pd.DataFrame({
        "Id": ids,
        "SalePrice": price
    })
    submission.to_csv("results/submission.csv", index=False)


if __name__ == "__main__":
    data_train = pd.read_csv("data/train.csv")
    data_test = pd.read_csv("data/test.csv")
    output_ids = data_test["Id"]

    eda.heatmap_of_nulls(data_train)
    eda.collage_of_plots(data_train)

    final_data_train = pipeline(data_train)
    final_data_test = pipeline(data_test)

    # random forest model
    y = final_data_train[GOAL_VARIABLE]
    X = final_data_train.drop(GOAL_VARIABLE, axis=1)
    rf_model = RandomForestRegressor(max_leaf_nodes=CANDIDATE_MAX_LEAF_NODES)
    rf_model.fit(X, y)
    score = cross_val_score(rf_model, X, y, cv=10)
    generate_submissions(output_ids, rf_model, final_data_test)
