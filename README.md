# House pricing: code refactoring assignment

## Summary

This repository was created to manage the third assignment of the *Large scale methods* course of the M. Sc. Data science at ITAM. The main goal was the refactoring and improvement of a single Jupyter notebook found under the competence [Kaggle house price prediction](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). While the refactoring stands for creating Python modules and functions, the improvements were the application of the programming best practices and recommendations following the [PEP8](https://peps.python.org/pep-0008/) style guide.

## Required dependencies

All the scripts were developed using `Python 3.9.13` as programming language, and the following libraries: `pandas` for data manipulation, `json` for reading external data, `seaborn` and `matplotlib` for data visualization, `scikit-learn` for data processing and machine learning models, and `typing` for data type handling. 

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

## How to execute the process

Just 