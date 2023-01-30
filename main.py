"""
    This module blah blah blah
"""
import pandas as pd

from src import cleaning as cln
from src import preprocessing as prcs

COLS_TO_DROP = [
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

FILL_CATEGORICAL = ["BsmtQual", "BsmtCond", "BsmtFinType1", "BsmtFinType2"]

ORDINAL_COLS = [
                "BsmtQual", "BsmtCond", "ExterQual", "ExterCond",
                "KitchenQual", "PavedDrive", "Electrical", "BsmtFinType1",
                "BsmtFinType2",
                "Utilities", "MSZoning", "Foundation", "Neighborhood",
                "MasVnrType",
                "SaleCondition", "RoofStyle", "RoofMatl"
            ]

CATEGORICAL_ENCODE = ["Street", "BldgType", "SaleType", "CentralAir"]

if __name__ == "__main__":
    # read train and test data from data folder
    data_train = pd.read_csv("data/train.csv")
    data_test = pd.read_csv("data/test.csv")

    # EDA HERE

    # drop unwanted columns
    data_train.drop(COLS_TO_DROP, axis=1, inplace=True)
    data_test.drop(COLS_TO_DROP, axis=1, inplace=True)

    # clean NA values from categorical variables
    cleaned_train_data = cln.custom_fill_na_values(
        data_train, FILL_CATEGORICAL, "No"
    )
    cleaned_test_data = cln.custom_fill_na_values(
        data_test, FILL_CATEGORICAL, "No"
    )

    # impute NA vales from numerical variables
    cleaned_train_data = cln.fill_all_na_values(cleaned_train_data)
    cleaned_test_data = cln.fill_all_na_values(cleaned_test_data)

    # preprocesing
    preprocessed_train_data = prcs.encode_variables(cleaned_train_data)
    preprocessed_test_data = prcs.encode_variables(cleaned_test_data)

    preprocessed_train_data = prcs.encode_catagorical_columns(
                                    preprocessed_train_data, CATEGORICAL_ENCODE
                                )
    preprocessed_test_data = prcs.encode_catagorical_columns(
                                preprocessed_test_data, CATEGORICAL_ENCODE
                            )
