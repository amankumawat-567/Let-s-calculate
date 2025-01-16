class TemperatureConvertor:
    """
    A class to convert between different temperature units.
    Supported units: Celsius, Fahrenheit, Kelvin
    """

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Converts Celsius to Fahrenheit.

        Args:
            celsius (float): Temperature in Celsius.

        Returns:
            float: Temperature in Fahrenheit.
        """
        return celsius * 9/5 + 32

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """
        Converts Celsius to Kelvin.

        Args:
            celsius (float): Temperature in Celsius.

        Returns:
            float: Temperature in Kelvin.
        """
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """
        Converts Fahrenheit to Celsius.

        Args:
            fahrenheit (float): Temperature in Fahrenheit.

        Returns:
            float: Temperature in Celsius.
        """
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit: float) -> float:
        """
        Converts Fahrenheit to Kelvin.

        Args:
            fahrenheit (float): Temperature in Fahrenheit.

        Returns:
            float: Temperature in Kelvin.
        """
        return (fahrenheit - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """
        Converts Kelvin to Celsius.

        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature in Celsius.
        """
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin: float) -> float:
        """
        Converts Kelvin to Fahrenheit.

        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature in Fahrenheit.
        """
        return (kelvin - 273.15) * 9/5 + 32

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Converts a temperature value from one unit to another.

        Args:
            value (float): Temperature value to convert.
            from_unit (str): Unit to convert from (e.g., "Celsius", "Fahrenheit", "Kelvin").
            to_unit (str): Unit to convert to (e.g., "Celsius", "Fahrenheit", "Kelvin").

        Returns:
            float: Converted temperature value.
        """
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return self.celsius_to_fahrenheit(value)
            elif to_unit == "Kelvin":
                return self.celsius_to_kelvin(value)
            else:
                return value
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return self.fahrenheit_to_celsius(value)
            elif to_unit == "Kelvin":
                return self.fahrenheit_to_kelvin(value)
            else:
                return value
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return self.kelvin_to_celsius(value)
            elif to_unit == "Fahrenheit":
                return self.kelvin_to_fahrenheit(value)
            else:
                return value
        else:
            raise ValueError("Invalid temperature units provided.")
        
        raise ValueError("Conversion between the specified units is not supported.")
