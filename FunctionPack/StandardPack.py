from FunctionPack import PackTemplate
from FunctionPack.MathFunction import *

class StandardPack(PackTemplate):
    def __init__(self,display,displayf,replacement_dict,max_length=None):
        super().__init__(display,max_length)
        self.displayf = displayf
        self.replacement_dict = replacement_dict

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

        return expression, result

    def add_number(self, number):
        """
        Add a number to the display.
        """
        self.update_display(str(number))
        
    def change_sign(self):
        current = self.display.get()
        if not current:
            self.display.set("-" + current)  
        elif current[0] == "-" :
            self.display.set(current[1:])
        else :
            self.display.set("-" + current)
