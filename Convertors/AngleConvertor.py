import math

class AngleConvertor:
    """
    A class to convert between different angle units.
    Supported units: Degrees, Radians, Gradians
    """

    @staticmethod
    def degrees_to_radians(degrees: float) -> float:
        """
        Converts Degrees to Radians.

        Args:
            degrees (float): Angle in Degrees.

        Returns:
            float: Angle in Radians.
        """
        return degrees * math.pi / 180

    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        """
        Converts Radians to Degrees.

        Args:
            radians (float): Angle in Radians.

        Returns:
            float: Angle in Degrees.
        """
        return radians * 180 / math.pi

    @staticmethod
    def degrees_to_gradians(degrees: float) -> float:
        """
        Converts Degrees to Gradians.

        Args:
            degrees (float): Angle in Degrees.

        Returns:
            float: Angle in Gradians.
        """
        return degrees * 10 / 9

    @staticmethod
    def gradians_to_degrees(gradians: float) -> float:
        """
        Converts Gradians to Degrees.

        Args:
            gradians (float): Angle in Gradians.

        Returns:
            float: Angle in Degrees.
        """
        return gradians * 9 / 10

    @staticmethod
    def radians_to_gradians(radians: float) -> float:
        """
        Converts Radians to Gradians.

        Args:
            radians (float): Angle in Radians.

        Returns:
            float: Angle in Gradians.
        """
        return radians * 200 / math.pi

    @staticmethod
    def gradians_to_radians(gradians: float) -> float:
        """
        Converts Gradians to Radians.

        Args:
            gradians (float): Angle in Gradians.

        Returns:
            float: Angle in Radians.
        """
        return gradians * math.pi / 200

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Converts an angle value from one unit to another.

        Args:
            value (float): Angle value to convert.
            from_unit (str): Unit to convert from (e.g., "Degrees", "Radians", "Gradians").
            to_unit (str): Unit to convert to (e.g., "Degrees", "Radians", "Gradians").

        Returns:
            float: Converted angle value.
        """
        if from_unit == "Degrees":
            if to_unit == "Radians":
                return self.degrees_to_radians(value)
            elif to_unit == "Gradians":
                return self.degrees_to_gradians(value)
            else:
                return value
        elif from_unit == "Radians":
            if to_unit == "Degrees":
                return self.radians_to_degrees(value)
            elif to_unit == "Gradians":
                return self.radians_to_gradians(value)
            else:
                return value
        elif from_unit == "Gradians":
            if to_unit == "Degrees":
                return self.gradians_to_degrees(value)
            elif to_unit == "Radians":
                return self.gradians_to_radians(value)
            else:
                return value
        else:
            raise ValueError("Invalid angle units provided.")
        
        raise ValueError("Conversion between the specified units is not supported.")
