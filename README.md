# House pricing: code refactoring assignment

## Summary

This repository was created to manage the third assignment of the *Large scale methods* course of the M. Sc. Data science at ITAM. The main goal was the refactoring and improvement of a single Jupyter notebook found under the competence [Kaggle house price prediction](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques). While the refactoring stands for creating Python modules and functions, the improvements were the application of the programming best practices and recommendations following the [PEP8](https://peps.python.org/pep-0008/) style guide.

## Required dependencies

All the scripts were developed using `Python 3.9.13` as programming language, and the following libraries: `pandas` for data manipulation, `json` for reading external data, `seaborn` and `matplotlib` for data visualization, `scikit-learn` for data processing and machine learning models, and `typing` for data type handling. 

## How to get the data

The data is available for free under the `data` tab of the [Kaggle competition](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data).

## Repository structure

The repo is organized by single purpose folders as follows:

- `data`: should contain all the _.csv_ files to be used in the execution of the code (train.csv and test.csv).
- `images:` stores the resulting plots after executing the EDA functions over the train dataset. 
- `msc`: contains a single _JSON_ file with the column' names and their encoding levels. 
- `results:` created with the objective of storing the resulting predictions using the trained model.  
- `src:` is composed by 3 core Python scrips:
  - `cleaning.py:` contains the functions related to fill and impute NA values based on the needs of the problem. 
  - `eda.py:` contains the functions to perform a single EDA and store the resulting plots. 
  - `preprocessing.py:` contains the functions to generate the encoding of the variables and to create pre-defined interactions.

In addition to those folders, a `main.py` file is located at the root of the repository. This file contains all the steps (described below) that will be executed, from taking the data to generate the plots and the final predictions. 

## Steps

1) The train and test datasets are being read, also the _Ids_ are obtained and stored in an independent variable.
2) A couple of plots are generated from the EDA process and are stored into the `images` folder. The first one is a heatmap of null values, which represents the presence or absence of the values for one or more variables in each register of the train dataset.
3) A pipeline is executed for each dataset. The pipeline is composed by:
        3.1) Drop the unwanted columns.
        3.2) Fill the _'NA'_ values of specific desired variables using a custom value.
        3.3) Fill the _'NA'_ values of the rest of the variables based on the type of each variable: numerical or categorical.
        3.4) Encode a predefined set of variables using the `Ordinal encoder` operation and the `map_encoders.json` file.
        3.5) Encode a predefined set of categorical variables using the `Label encoder` operation.
        3.6) Create a predefined set of variables by interactions between existing variables. 
        3.7) Drop the variables that are not used for the final prediction.
4) Set the input and output variables to perform the training process and the predictions.
5) Create a `Random Forest Regressor` model and train it using the train dataset and the input and output variables.
6) Calculate a list of average scores for the model by using the `cross validation` method.
7) Finally, calculate the predictions for the test dataset and save them into the `results` folder.

## How to execute the process

By using the command `python main.py` you could be able to execute the process and generate the plots and the predictions under the respective folders. 