import json
import os
from typing import List, Dict, Optional

class HistoryManager:
    """
    A class to manage the history of calculations with permanent storage in a JSON file.
    It supports adding, retrieving, deleting entries, and clearing the entire history.

    Attributes:
        file_name (str): The name of the JSON file to store the history.
        history (List[Dict[str, str]]): A list of dictionaries representing the history of calculations.
    """

    def __init__(self, file_name: str) -> None:
        """
        Initializes the HistoryManager with a specified file name and loads any existing history from the file.

        Args:
            file_name (str): The name of the file to store the history. Defaults to "history.json".
        """
        self.file_name: str = file_name
        self.history: List[Dict[str, str]] = self.load_history()

    def load_history(self) -> List[Dict[str, str]]:
        """
        Loads the history from the JSON file if it exists, otherwise returns an empty list.

        Returns:
            List[Dict[str, str]]: A list of history entries (questions and answers).
        """
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        return []

    def save_history(self) -> None:
        """
        Saves the current history to the JSON file.

        This method is called every time an entry is added or deleted to ensure the history is persistent.
        """
        with open(self.file_name, "w") as file:
            json.dump(self.history, file, indent=4)

    def add(self, question: str, answer: float) -> None:
        """
        Adds a new entry to the history.

        Args:
            question (str): The question (e.g., "5 + 3").
            answer (float): The result of the calculation.
        """
        self.history.append({"Ques": question, "Ans": answer})
        self.save_history()

    def get_all(self) -> List[Dict[str, str]]:
        """
        Retrieves all history entries.

        Returns:
            List[Dict[str, str]]: A list of all history entries in the format [{"Ques": ..., "Ans": ...}].
        """
        return self.history

    def get(self, index: int) -> Optional[Dict[str, str]]:
        """
        Retrieves a specific entry by index.

        Args:
            index (int): The index of the history entry to retrieve.

        Returns:
            Optional[Dict[str, str]]: The history entry at the given index, or None if the index is invalid.
        """
        if 0 <= index < len(self.history):
            return self.history[index]
        return None

    def delete_all(self) -> None:
        """
        Deletes all entries from the history.
        """
        self.history.clear()
        self.save_history()

    def delete(self, index: int) -> bool:
        """
        Deletes a specific entry by index.

        Args:
            index (int): The index of the history entry to delete.

        Returns:
            bool: True if the entry was successfully deleted, False if the index was invalid.
        """
        if 0 <= index < len(self.history):
            del self.history[index]
            self.save_history()
            return True
        return False