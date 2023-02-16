"""Configuration info loader

This class allows the current execution to load the main configurations defined
by the user to use them as environment variables. The class uses the
configparser library to read the config.ini file. Also, several functions
related to paths to save outputs have been defined.

To instantiate a new ConfigValues class is as follows:
example_of_configvalues = ConfigVales()
"""

from configparser import ConfigParser


class ConfigValues:
    """The ConfigValues class loads the config.ini file to use its values during
        the current execution.
    """
    def __init__(self) -> ConfigParser:
        """Instantiate a new ConfigParser and then load the config.ini file.
        """
        self.config = ConfigParser()
        self.config.read("config/config.ini")

    def path_train(self) -> str:
        """Takes the name of the folder where the data is located and the name
        of the file which is associated to the train dataset.

        Returns:
            path_to_return (str): the relative path for the train dataset.
        """
        folder = self.config["DATA"]["folder"]
        train_name = self.config["DATA"]["train"]
        path_to_return = f'{folder}/{train_name}'
        return path_to_return

    def path_test(self) -> str:
        """Takes the name of the folder where the data is located and the name
        of the file which is associated to the test dataset.

        Returns:
            path_to_return (str): the relative path for the test dataset.
        """
        folder = self.config["DATA"]["folder"]
        test_name = self.config["DATA"]["test"]
        path_to_return = f'{folder}/{test_name}'
        return path_to_return

    def path_heatmap(self) -> str:
        """Takes the name of the folder where the plot is going to be saved and
        the name that the plot will take as a new file.

        Returns:
            path_to_return (str): the relative path where the plot is going to
            be saved.
        """
        folder = self.config["EDA"]["folder"]
        plot_name = self.config["EDA"]["heatmap"]
        path_to_return = f'{folder}/{plot_name}'
        return path_to_return

    def path_collage(self) -> str:
        """Takes the name of the folder where the plot is going to be saved and
        the name that the plot will take as a new file.

        Returns:
            path_to_return (str): the relative path where the plot is going to
            be saved.
        """
        folder = self.config["EDA"]["folder"]
        plot_name = self.config["EDA"]["collage"]
        path_to_return = f'{folder}/{plot_name}'
        return path_to_return

    def path_submissions(self) -> str:
        """Takes the name of the folder where the submission dataset is going to
        be saved and the name that the dataset will take as a new file.

        Returns:
            path_to_return (str): the relative path where the dataset is going
            to be saved.
        """
        folder = self.config["RESULTS"]["folder"]
        results_name = self.config["RESULTS"]["name"]
        path_to_return = f'{folder}/{results_name}'
        return path_to_return
