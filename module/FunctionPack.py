# Functional Module
import math

class StandardPack:
    def __init__(self,display,displayf,replacement_dict,max_length=None):
        self.display = display
        self.displayf = displayf
        self.replacement_dict = replacement_dict
        self.max_length = max_length

    def update_display(self, text):
        """
        Update the display text, ensuring it doesn't exceed the max length.
        """
        current = self.display.get()
        if self.max_length and len(current) >= self.max_length:
            self.display.set(current[:self.max_length - 1])
        self.display.set(current + text)

    def clear_display(self):
        """
        Clear both the main display and secondary display.
        """
        self.display.set("")
        self.displayf.set("")

    def toggle_bracket(self):
        """
        Add or toggle brackets based on the current display state.
        """
        operators = [" ÷ ", " ᵡ ", " + ", " - ", "(", "sin", "cos", "tan", 
                    "asin", "acos", "atan", "sinh", "cosh", "tanh", 
                    "asinh", "acosh", "atanh"]
        current = self.display.get()
        if not current:
            self.display.set("(")
        elif any(current.endswith(op) for op in operators):
            self.display.set(current + "(")
        else:
            self.display.set(current + ")")

    def backspace(self):
        """
        Remove the last character from the display.
        """
        current = self.display.get()
        if current:
            self.display.set(current[:-1])

    def add_operator(self, operator):
        """
        Add an operator to the display, handling special cases.
        """
        operators = [" ÷ ", " ᵡ ", " + ", " - "]
        current = self.display.get()
        full_expr = self.displayf.get() + current
        self.displayf.set(full_expr)
        self.display.set("")
        if full_expr and full_expr[-3:] in operators:
            self.displayf.set(full_expr[:-3] + f" {operator} ")
        else:
            self.update_display( f" {operator} ")

    def calculate(self):
        """
        Evaluate the current mathematical expression.
        """
        expression = self.displayf.get() + self.display.get()
        self.displayf.set(expression)
        if expression:
            for func, repl in self.replacement_dict.items():
                expression = expression.replace(func, repl)
            try:
                result = eval(expression)
            except Exception:
                result = "Error"
            self.display.set(result)

    def add_number(self, number):
        """
        Add a number to the display.
        """
        self.update_display(str(number))

    def add_function(self, function):
        """
        Add a mathematical function to the display.
        """
        self.update_display( function + "(")
        
    def change_sign(self):
        current = self.display.get()
        if not current:
            self.display.set("-" + current)  
        elif current[0] == "-" :
            self.display.set(current[1:])
        else :
            self.display.set("-" + current)

def square(display):
    """
    Add square operation to the display.
    """
    display.set(display.get() + "^(2)")

def cube(display):
    """
    Add cube operation to the display.
    """
    display.set(display.get() + "^(3)")

def factorial(display):
    """
    Add factorial operation to the display.
    """
    display.set("fac(" + display.get() + ")")

# Math helper functions
def log(x):
    return math.log10(x)

def ln(x):
    return math.log(x)
