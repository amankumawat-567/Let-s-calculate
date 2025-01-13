import json
import os
from typing import List

class ThemeManager:
    """
    A manager for handling theme and locus data. 

    Features:
    - Create, update, and switch themes stored in JSON files.
    - Manage a single locus value stored in a plain text file.

    Attributes:
        theme_dir (str): Directory where theme JSON files are stored.
        data_dir (str): Directory where data files (theme and locus) are stored.
    """

    def __init__(self, theme_dir: str, data_dir: str) -> None:
        """
        Initialize the ThemeManager with the specified directories.

        Args:
            theme_dir (str): Path to the directory containing theme JSON files.
            data_dir (str): Path to the directory where data files will be stored.
        """
        self.theme_dir = theme_dir
        self.data_dir = data_dir
        self.available_themes = self.__available_themes()
        
    def __available_themes(self) -> List[str]:
        """
        Retrieve all the available themes in theme directory.

        Returns:
            List[str]: list of all the the available themes.

        Raises:
            FileNotFoundError: If there are no themes available in the theme directory.
        """
        entries = os.listdir(self.theme_dir)
        Themes = [entry for entry in entries if os.path.isdir(os.path.join(self.theme_dir, entry))]
        if not Themes:
            raise FileNotFoundError("No themes available in the theme directory.")
        return Themes

    def change_theme(self, theme_name: str) -> None:
        """
        Change the current theme by copying a theme JSON file from the theme directory.

        Args:
            theme_name (str): Name of the theme to switch to.

        Raises:
            FileNotFoundError: If the specified theme JSON file does not exist.
        """
        theme_path = os.path.join(self.theme_dir, theme_name, 'theme.json')
        if not os.path.exists(theme_path):
            raise FileNotFoundError(f"Theme file not found: {theme_path}")

        with open(theme_path, 'r') as file:
            theme_data = json.load(file)

        target_path = os.path.join(self.data_dir, 'current_theme.json')
        with open(target_path, 'w') as file:
            json.dump(theme_data, file, indent=4)

    def update_locus(self, position: str) -> None:
        """
        Update the locus position stored in the plain text file.

        Args:
            position (str): The new locus position to save.
        """
        locus_path = os.path.join(self.data_dir, 'locus.txt')
        with open(locus_path, 'w') as file:
            file.write(position)
            
    def get_theme(self) -> dict[str, str]:
        """
        Retrieve the current theme data from the JSON file.

        Returns:
            dict: The current theme data.

        Raises:
            FileNotFoundError: If the theme JSON file does not exist.
        """
        theme_path = os.path.join(self.data_dir, 'current_theme.json')
        if not os.path.exists(theme_path):
            raise FileNotFoundError(f"Theme file not found: {theme_path}")

        with open(theme_path, 'r') as file:
            return json.load(file)
        
    def get_locus(self) -> str:
        """
        Retrieve the current locus position from the plain text file.

        Returns:
            str: The current locus position.

        Raises:
            FileNotFoundError: If the locus text file does not exist.
        """
        locus_path = os.path.join(self.data_dir, 'locus.txt')
        if not os.path.exists(locus_path):
            raise FileNotFoundError(f"Locus file not found: {locus_path}")

        with open(locus_path, 'r') as file:
            return file.read().strip()