from tkinter import StringVar
from typing import Callable, List

# Define a utility function for limiting input length
def limit_length(display: StringVar, max_length: int = 14) -> None:
    """
    Truncate the content of the StringVar if it exceeds the maximum length.

    Args:
        display (StringVar): The display variable to update.
        max_length (int): The maximum allowed length.
    """
    content = display.get()
    if len(content) > max_length:
        display.set(content[:max_length])

class ProgrammingPack:
    """
    A class to handle number system conversions and related operations.

    Attributes:
        dece (StringVar): The decimal representation.
        hexa (StringVar): The hexadecimal representation.
        octa (StringVar): The octal representation.
        bine (StringVar): The binary representation.
        action (str): The current active number system ("decimal", "hexadecimal", "octadecimal", or "binary").
    """

    def __init__(
        self, 
        dece: StringVar, 
        hexa: StringVar, 
        octa: StringVar, 
        bine: StringVar
    ) -> None:
        self.dece = dece
        self.hexa = hexa
        self.octa = octa
        self.bine = bine
        self.action = "decimal"

    def operation(self, txt: str) -> None:
        """
        Perform the conversion based on the current action and input.

        Args:
            txt (str): The input text to append and convert.
        """
        try:
            if self.action == "decimal":
                limit_length(self.dece)
                self.dece.set(self.dece.get() + txt)
                value = int(self.dece.get())

            elif self.action == "hexadecimal":
                limit_length(self.hexa)
                self.hexa.set(self.hexa.get() + txt)
                value = int(self.hexa.get(), 16)

            elif self.action == "octadecimal":
                limit_length(self.octa)
                self.octa.set(self.octa.get() + txt)
                value = int(self.octa.get(), 8)

            elif self.action == "binary":
                limit_length(self.bine)
                self.bine.set(self.bine.get() + txt)
                value = int(self.bine.get(), 2)

            self.update_displays(value)

        except ValueError:
            pass

    def update_displays(self, value: int) -> None:
        """
        Update all number system displays based on the given integer value.

        Args:
            value (int): The integer value to convert and display.
        """
        self.dece.set(str(value))
        self.hexa.set(hex(value).replace("0x", ""))
        self.octa.set(oct(value).replace("0o", ""))
        self.bine.set(bin(value).replace("0b", ""))

    def clear(self) -> None:
        """Clear all number system displays."""
        for display in [self.dece, self.hexa, self.octa, self.bine]:
            display.set("")

    def backspace(self) -> None:
        """Remove the last character from the active display and update conversions."""
        active_display = {
            "decimal": self.dece,
            "hexadecimal": self.hexa,
            "octadecimal": self.octa,
            "binary": self.bine
        }.get(self.action, self.dece)

        content = active_display.get()
        if content:
            active_display.set(content[:-1])
            try:
                value = int(active_display.get(), {
                    "decimal": 10,
                    "hexadecimal": 16,
                    "octadecimal": 8,
                    "binary": 2
                }[self.action])
                self.update_displays(value)
            except ValueError:
                self.clear()

    def add_number(self, number: int) -> None:
        """Add a number to the active display."""
        self.operation(str(number))

    def add_character(self, char: str) -> None:
        """Add a character to the active display."""
        self.operation(char)

    def toggle_sign(self) -> None:
        """Toggle the sign of all number system displays."""
        for display in [self.dece, self.hexa, self.octa, self.bine]:
            content = display.get()
            if content.startswith("-"):
                display.set(content[1:])
            else:
                display.set("-" + content)

    def set_active_entry(self, mode: str) -> None:
        """
        Set the active number system for input.

        Args:
            mode (str): The mode to set ("decimal", "hexadecimal", "octadecimal", or "binary").
        """
        self.action = mode
