# House pricing: code refactoring assignment

## Summary

This repository was created to manage the third assignment of the *Large scale methods* course of the M. Sc. Data science at ITAM. The main goal was the refactoring and improvement of a single Jupyter notebook found under the competence [Kaggle house price prediction](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). While the refactoring stands for creating Python modules and functions, the improvements were the application of the programming best practices and recommendations following the [PEP8](https://peps.python.org/pep-0008/) style guide.

## Repository structure

The repo is organized by single purpose folders as follows:

- **data**: should contain all the _.csv_ files to be used in the execution of the code (train.csv and test.csv).
- **images:** stores the resulting plots after executing the EDA functions over the train dataset. 
- **msc**: contains a single _JSON_ file with the column' names and their encoding levels. 
- **src:** is composed by 3 core Python scrips:
  - **cleaning.py**