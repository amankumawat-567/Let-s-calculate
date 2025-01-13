import requests
import json
import os
from typing import Dict


class CurrencyDataUpdater:
    """
    A class to get current exchange rates using an API and store the data in a JSON file.

    Attributes:
        api_url (str): The API URL to fetch the exchange rates.
        json_file_path (str): The path to store the updated currency data in JSON format.
    """

    def __init__(self, api_url: str, data_dir: str):
        """
        Initialize the CurrencyDataUpdater with the API URL and file path.

        Args:
            api_url (str): The API URL to fetch the exchange rates.
            json_file_path (str): The path to store the JSON file.
        """
        self.api_url = api_url
        self.json_file_path = os.path.join(data_dir, 'currency_data.json')

    def fetch_exchange_rates(self) -> Dict:
        """
        Fetch the current exchange rates from the API.

        Returns:
            dict: The exchange rates data.
        """
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data: {response.status_code}")
            return {}

    def update_json(self, data: Dict) -> None:
        """
        Update the JSON file with the fetched currency data.

        Args:
            data (dict): The fetched currency data.
        """
        # Ensure the directory for the JSON file exists
        os.makedirs(os.path.dirname(self.json_file_path), exist_ok=True)

        # Write data to the JSON file
        with open(self.json_file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def run(self) -> None:
        """
        Run the full update process: fetch and update the JSON file.
        """
        print("Fetching exchange rates...")
        data = self.fetch_exchange_rates()
        if data:
            print("Fetched exchange rates successfully.")
            self.update_json(data)
            print(f"Updated JSON file at {self.json_file_path}.")


class CurrencyConvertor:
    """
    A class to load currency conversion rates from a JSON file and perform currency conversions.
    """

    def __init__(self, data_dir: str):
        """
        Initializes the CurrencyConvertor by loading the conversion data from a JSON file.

        Args:
            json_file (str): Path to the JSON file containing currency conversion data.
        """
        self.json_file = os.path.join(data_dir, 'currency_data.json')
        self.conversion_data = self.load_conversion_data()

    def load_conversion_data(self) -> Dict[str, float]:
        """
        Loads the currency conversion data from the JSON file.

        Returns:
            dict: A dictionary with currency codes as keys and conversion rates as values.
        """
        with open(self.json_file, 'r') as f:
            data = json.load(f)
            return data['conversion_rates']
        
    def Refresh(self):
        self.conversion_data = self.load_conversion_data()
        
    def get_all_currencies(self) -> list:
        """
        Retrieves a list of all available currencies from the conversion rates data.

        Returns:
            list: A list of currency codes.
        """
        return list(self.conversion_data.keys())

    def convert(self, from_currency: str, to_currency: str, amount: float) -> float:
        """
        Converts an amount from one currency to another.

        Args:
            from_currency (str): The currency to convert from (e.g., "USD", "EUR").
            to_currency (str): The currency to convert to (e.g., "INR", "GBP").
            amount (float): The amount to be converted.

        Returns:
            float: The converted amount.

        Raises:
            ValueError: If the currencies are not found in the conversion data.
        """
        if from_currency not in self.conversion_data or to_currency not in self.conversion_data:
            raise ValueError(f"One or both currencies '{from_currency}' or '{to_currency}' not found in the conversion data.")

        # Retrieve the conversion rates for the from and to currencies
        from_rate = self.conversion_data[from_currency]
        to_rate = self.conversion_data[to_currency]

        # Conversion formula
        converted_amount = amount * (to_rate / from_rate)

        return converted_amount