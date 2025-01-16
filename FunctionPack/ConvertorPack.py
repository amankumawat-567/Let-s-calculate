from tkinter import StringVar
from typing import Callable, Optional
from Convertors import UnitConvertor, CurrencyConvertor

# Define a decorator for exception handling
def handle_exceptions(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Log or handle the exception as needed
            pass
    return wrapper

def change_sign(display: StringVar) -> None:
    """
    Toggle the sign of the numeric value in the given StringVar.

    Args:
        display (StringVar): The display variable to update.
    """
    current = display.get()
    if current.startswith("-"):
        display.set(current[1:])
    else:
        display.set("-" + current)

class ConverterPack:
    """
    A class to handle conversion-related operations between two displays and combo boxes.

    Attributes:
        display1 (StringVar): The first display variable.
        display2 (StringVar): The second display variable.
        combo1 (StringVar): The first combo box variable.
        combo2 (StringVar): The second combo box variable.
        convertor (Callable): A callable to handle the conversion logic.
        action (int): Tracks the active display for input (1 or 2).
    """

    def __init__(
        self, 
        display1: StringVar, 
        display2: StringVar, 
        combo1: StringVar, 
        combo2: StringVar, 
        convertor: CurrencyConvertor|UnitConvertor
    ) -> None:
        self.display1 = display1
        self.display2 = display2
        self.combo1 = combo1
        self.combo2 = combo2
        self.convertor = convertor
        self.action = 2
        self._converter_type: Optional[str] = None

    @handle_exceptions
    def convert_data(self, text: str) -> None:
        """
        Perform the conversion based on the current action and input.

        Args:
            text (str): The input text to append and convert.
        """
        active_display = self.display2 if self.action == 2 else self.display1
        passive_display = self.display1 if self.action == 2 else self.display2
        base_combo = self.combo2 if self.action == 2 else self.combo1
        target_combo = self.combo1 if self.action == 2 else self.combo2

        active_display.set(active_display.get() + text)
        base = base_combo.get()
        target = target_combo.get()
        if self._converter_type == 'currency':
            result = self.convertor.convert(base, target, float(active_display.get()))
        else:
            result = self.convertor.convert(
                self._converter_type, base, target, float(active_display.get())
            )
        passive_display.set(str(result))

    @handle_exceptions
    def back_space(self) -> None:
        """Remove the last character from the active display and update the result."""
        active_display = self.display2 if self.action == 2 else self.display1
        active_display.set(active_display.get()[:-1])
        self.equals()

    def set_type(self, type_: str) -> None:
        """
        Set the type of conversion.

        Args:
            type_ (str): The type of conversion.
        """
        self._converter_type = type_

    def add_number(self, number: int) -> None:
        """
        Add a number to the active display.

        Args:
            number (int): The number to add.
        """
        self.convert_data(str(number))

    def add_point(self) -> None:
        """Add a decimal point to the active display."""
        self.convert_data(".")

    def equals(self) -> None:
        """Recalculate and update the conversion results."""
        self.convert_data("")

    def clear(self) -> None:
        """Clear both display variables."""
        self.display1.set("")
        self.display2.set("")

    def change_sign(self) -> None:
        """Toggle the sign of both display variables."""
        change_sign(self.display1)
        change_sign(self.display2)
        
    def active_entry(self,number: int):
        """Set the active entry to the given number."""
        self.action = number