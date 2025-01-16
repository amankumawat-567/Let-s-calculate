from tkinter import Button
from typing import List
from Routers import BaseCalculater
from FunctionPack import ScientificPack
from FunctionPack.MathFunction import angle_unit

class ScientificCalculator(BaseCalculater):
    def __init__(self,parent, theme, history_manager, image_manager):
        replacement_dict = dict(zip(["÷","^","ᵡ","e","ᴨ","³√(","√("],["/","**","*","2.718281828459045","3.141592653589793","cur(","sqr("]))
        super().__init__("scientific", parent,theme,image_manager,history_manager,replacement_dict)
        self.height = 550
        self.width = 595
        self.switchvar: bool = False
        self.angle_unit: str = 'Degrees'
        self.scientific_buttons: List[Button] = []
        self.fxn.append(ScientificPack(self.display))
        self._ui_setup()
    
    def _ui_setup(self):
        super()._ui_setup()
        
        standard_Buttons_config = [[("clear",self.fxn[0].clear_display),("Bracket",self.fxn[0].toggle_bracket),("Back_space",self.fxn[0].backspace),("divide",lambda: self.fxn[0].add_operator(' ÷ '))],
                   [("S7",lambda:self.fxn[0].add_number(7)),("S8",lambda:self.fxn[0].add_number(8)),("S9",lambda:self.fxn[0].add_number(9)),("mult",lambda: self.fxn[0].add_operator(' ᵡ '))],
                   [("S4",lambda:self.fxn[0].add_number(4)),("S5",lambda:self.fxn[0].add_number(5)),("S6",lambda:self.fxn[0].add_number(6)),("add",lambda: self.fxn[0].add_operator(' + '))],
                   [("S1",lambda:self.fxn[0].add_number(1)),("S2",lambda:self.fxn[0].add_number(2)),("S3",lambda:self.fxn[0].add_number(3)),("subtr",lambda: self.fxn[0].add_operator(' - '))],
                   [("Ss",self.fxn[0].change_sign),("S0",lambda:self.fxn[0].add_number(0)),("point",lambda:self.fxn[0].update_display('.')),("equal",self.calculate)]]

        scientific_Buttons_config = [[[("Root", lambda:self.fxn[1].add_function("√"))],
                    [("sin", lambda:self.fxn[1].add_function("sin")),('cos', lambda:self.fxn[1].add_function("cos")),('Tan', lambda:self.fxn[1].add_function("tan"))],
                    [('ln', lambda:self.fxn[1].add_function("ln")),('log', lambda:self.fxn[1].add_function("log")),('Bix', lambda:self.fxn[1].add_function("1÷"))],
                    [('ex', lambda:self.fxn[1].add_function("e^")),('X2', lambda:self.fxn[1].add_expression("^(2)")),('Xy', lambda:self.fxn[1].add_expression("^"))],
                    [('mod', lambda:self.fxn[1].add_function("abs")),('pi', lambda:self.fxn[1].add_expression("ᴨ")),('e', lambda:self.fxn[1].add_expression("e"))]],
                    [[("cuberoot", lambda:self.fxn[1].add_function("³√"))],
                    [("Asin", lambda:self.fxn[1].add_function("asin")),('Acos', lambda:self.fxn[1].add_function("acos")),('Atan', lambda:self.fxn[1].add_function("atan"))],
                    [("sinh", lambda:self.fxn[1].add_function("sinh")),('cosh', lambda:self.fxn[1].add_function("cosh")),('Tanh', lambda:self.fxn[1].add_function("tanh"))],
                    [("Asinh", lambda:self.fxn[1].add_function("asinh")),('Acosh', lambda:self.fxn[1].add_function("acosh")),('Atanh', lambda:self.fxn[1].add_function("atanh"))],
                    [('exp2', lambda:self.fxn[1].add_function("2^")),('X3', lambda:self.fxn[1].add_expression("^(3)")),('X!', lambda:self.fxn[1].add_function("fac"))]]]
        
        y_pointer  = 200
        width,height = 85,70
        for buttons in standard_Buttons_config:
            x_pointer = 255
            for image, function in buttons:
                Button(
                    self.frame,image = self.image_manager.get(self.name,image),
                    bd=0,activebackground=self.theme['buttonactivebg'], command= function
                    ).place(y=y_pointer, x=x_pointer, width=width, height=height)
                x_pointer += width
            y_pointer += height
            
        for sets in scientific_Buttons_config:
            Button_set = []
            for row in sets:
                r = []
                for image, function in row:
                    button = Button(self.frame, image=self.image_manager.get(self.name,image),
                                    bd=0, activebackground=self.theme['buttonactivebg'], command=function)
                    r.append(button)
                Button_set.append(r)
            self.scientific_buttons.append(Button_set)           

        change_but = Button(self.frame, image=self.image_manager.get(self.name,"swap"), 
                            activebackground=self.theme['buttonactivebg'], bd=0, 
                            command=self.__switch)

        self.rad_deg_but = Button(self.frame, image=self.image_manager.get(self.name,"Deg"), 
                                  activebackground=self.theme['buttonactivebg'], bd=0, 
                                  command=self.__rad_deg)
        
        change_but.place(y=200, x=0, width=85, height=70)
        self.rad_deg_but.place(y=200, x=85, width=85, height=70)
        self.__place_scientic_buttons()
    
    def __switch(self):
            self.switchvar = not self.switchvar
            self.__place_scientic_buttons()
    
    def __rad_deg(self):
            if self.angle_unit== "Radians":
                self.rad_deg_but.configure(image=self.image_manager.get(self.name,"Deg"))
                self.angle_unit = "Degrees"
            else :
                self.rad_deg_but.configure(image=self.image_manager.get(self.name,"Rad"))
                self.angle_unit = "Radians"
                
    def __place_scientic_buttons(self):
        state = self.switchvar
        button_width, button_height = 85, 70
        for Button_set in self.scientific_buttons:
            y_offset = 130
            for row in Button_set:
                x_offset = (0 if state else 255)
                y_offset += button_height
                for button in row[::-1]:
                    x_offset -= button_width
                    button.place(x=x_offset, y=y_offset, width=button_width, height=button_height)
            state = not state

