import math
from FunctionPack import PackTemplate

class ScientificPack(PackTemplate):
    def __init__(self,display,max_length=None):
        super().__init__(display,max_length)
        
    def add_function(self, function):
        """
        Add a mathematical function to the display.
        """
        self.update_display( function + "(")

    def add_expression(self, exp:str):
        """
        Add a number to the display.
        """
        self.update_display(exp)