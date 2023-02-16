# House pricing: code refactoring assignment

## Summary

This repository was created to manage a couple of assignments of the *Large scale methods* course of the M. Sc. Data science at ITAM. The main goal was the refactoring and improvement of a single Jupyter notebook found under the competence [Kaggle house price prediction](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques). While the refactoring stands for creating Python modules and functions, the improvements were the application of the programming best practices and recommendations following the [PEP8](https://peps.python.org/pep-0008/) style guide. Also the migration of the code to production style was considered under the activities of improving the structure of the code. 

## Dependencies and conda environment

All the scripts were developed using `Python 3.9.13` as programming language, and the following libraries: `pandas` and `numpy` for data manipulation, `json` for reading external data, `seaborn` and `matplotlib` for data visualization, `scikit-learn` for data processing and machine learning models, `typing` for data type handling, `pylint` and `flake8` for PEP8 style code formatting, and `pytest` for testing of functions and modules.

To reproduce the environment described above, an `environments.yaml` file was created at the root of the project to use with `conda`. The following command should be executed in order to re-create the `house-pricing` conda environment:

`conda env create --file environments.yaml`

## How to get the data

The data and its dictionary is available for free under the `app` tab of the [Kaggle competition](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data).

## Repository structure

The `app` folder contains all the code and required configurations to execute the application. Under this folder there are several single purpose folders ordered as follows:

- `config:` is related to basic configs to use execute the main code. A **config-sample.ini** file was added to take it as an example of the content that the actual **config.ini** file should have. 
- `data:` should contain all the _.csv_ files to be used in the execution of the code (train.csv and test.csv).
- `images:` stores the resulting plots after executing the EDA functions over the train dataset.
- `logs:` stores the logs and messages of the current execution of the code. 
- `msc`: contains a single _JSON_ file with the column' names and their encoding levels. 
- `results:` created with the objective of storing the resulting predictions using the trained model.  
- `src:` is composed by 3 core Python scrips:
  - `cleaning.py:` contains the functions related to fill and impute NA values based on the needs of the problem. 
  - `eda.py:` contains the functions to perform a single EDA and store the resulting plots. 
  - `preprocessing.py:` contains the functions to generate the encoding of the variables and to create pre-defined interactions.
- `test:` contains the modules used to test each function of the modules defined under the *src* folder.

In addition to those folders, a `main.py` file is located under the app folder. This file contains all the steps (described below) that will be executed, from taking the data to generate the plots and the final predictions. 

## How to execute the process

By using the command `python main.py <num_max_leaf_nodes>` from terminal you could be able to execute the process and generate the plots and the predictions under the respective folders. The `<num_max_leaf_nodes>` argument is required for the training process of the random forest model. An example of how to execute the code is as follows: `python main.py 250`.

## Steps

1) The `num_max_leaf_nodes` argument is retrieved and the logging basic configuration is loaded.
2) The config values are loaded from the `config.ini` file by using the `ConfigValues` class.
3) The train and test datasets are being read, also the _Ids_ are obtained and stored in an independent variable.
4) A couple of plots are generated from the EDA process and are stored into the `images` folder. The first one is a heatmap of null values, which represents the presence or absence of values for one or more variables in each register of the train dataset. The second one is a mix of plots to make explicit the dispersion and distribution of the values for some variables. 
5) A pipeline is executed for each dataset. The pipeline is composed by:
        3.1) Drop the unwanted columns.
        3.2) Fill the _'NA'_ values of specific desired variables using a custom value.
        3.3) Fill the _'NA'_ values of the rest of the variables based on the type of each variable: numerical or categorical.
        3.4) Encode a predefined set of variables using the `Ordinal encoder` operation and the `map_encoders.json` file.
        3.5) Encode a predefined set of categorical variables using the `Label encoder` operation.
        3.6) Create a predefined set of variables by interactions between existing variables. 
        3.7) Drop the variables that are not used for the final prediction.
6) Set the input and output variables to perform the training process and the predictions.
7) Create a `Random Forest Regressor` model and train it using the train dataset and the input and output variables.
8) Calculate a list of average scores for the model by using the `cross validation` method.
9) Finally, calculate the predictions for the test dataset and save them into the `results` folder.

# Run by using Docker

Two Dockerfiles were created to execute the application on a single Docker container. If you want to deploy the application in a separate container, the `Dockerfile` file should be used. If you want to deploy the application mounting the disk, the `Dockerfile.mount` file should be used. 

No matter what option you choose to deploy the application, the Dockerfile to use has to be named as `Dockerfile`, and should be the only one file with this name, so be careful when renaming the Dockerfile that you don't want to use.

The commands to deploy the application in a separate container are the following: 
1. `docker build -t house-pricing .` (this command will compile the Docker image and will be named as *house_pricing*).
2. `docker run -it --rm house-pricing` (this command will run the application on a separate container and will remove it when the code finished).

The commands to deploy the application mounting the disk are the following: 
1. `docker build -t house-pricing .` (this command will compile the Docker image and will be named as *house_pricing*).
2. `docker run -it --rm -v <absolute>/<path>/<to>/<repo>/house-pricing-refactoring/app:/app house-pricing` (this command will run the application by mounting the disk to execute the code and will remove it when the code finished).