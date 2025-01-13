import json
import os
from typing import Dict, List
from Convertors.AngleConvertor import AngleConvertor
from Convertors.TemperatureConvertor import TemperatureConvertor

class UnitConvertor:
    """
    A class to load unit conversion data from a JSON file and perform unit conversions.
    """

    def __init__(self, data_dir: str):
        """
        Initializes the UnitConvertor by loading the conversion data from a JSON file.

        Args:
            json_file (str): Path to the JSON file containing unit conversion data.
        """
        self.json_file = os.path.join(data_dir, 'conversion_data.json')
        self.conversion_data = self.load_conversion_data()
        self.temperature_convertor = TemperatureConvertor()
        self.angle_convertor = AngleConvertor()

    def load_conversion_data(self) -> Dict[str, Dict[str, float]]:
        """
        Loads the unit conversion data from the JSON file.

        Returns:
            dict: A dictionary with unit categories as keys and unit conversion data as values.
        """
        with open(self.json_file, 'r') as f:
            return json.load(f)
    
    def get_units_by_category(self, category: str) -> List[str]:
        """
        Retrieves a list of all units for a specific category.

        Args:
            category (str): The category to get units for (e.g., "length", "mass").

        Returns:
            list: A list of unit names in the specified category.
        """
        # Handle special categories like "temperature" and "angle"
        if category == "temperature":
            return ["Celsius","Kelvin","Fahrenheit"]
        
        if category == "angle":
            return ["Degrees","Radians","Gradians"]
        
        if category in self.unit_data:
            units = self.unit_data[category]
            return [unit["unit"] for unit in units]
        else:
            raise ValueError(f"Category '{category}' not found in the unit data.")

    def convert(self, category: str, from_unit: str, to_unit: str, value: float) -> float:
        """
        Converts a value from one unit to another within the specified category.

        Args:
            category (str): The category of units (e.g., "length", "area").
            from_unit (str): The unit to convert from.
            to_unit (str): The unit to convert to.
            value (float): The value to be converted.

        Returns:
            float: The converted value.

        Raises:
            ValueError: If the units are not found in the conversion data or the category is invalid.
        """
        # Handle special categories like "temperature" and "angle"
        if category == "temperature":
            return self.temperature_convertor.convert(value, from_unit, to_unit)
        
        if category == "angle":
            return self.angle_convertor.convert(value, from_unit, to_unit)
        
        if category not in self.conversion_data:
            raise ValueError(f"Category '{category}' not found in the conversion data.")
        
        units_data = self.conversion_data[category]

        if from_unit not in units_data or to_unit not in units_data:
            raise ValueError(f"One or both units '{from_unit}' or '{to_unit}' not found in category '{category}'.")

        # Retrieve the conversion values for the from and to units
        from_value = units_data[from_unit]
        to_value = units_data[to_unit]

        # Conversion formula
        converted_value = value * (to_value / from_value)

        return converted_value