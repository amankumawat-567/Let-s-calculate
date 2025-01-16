from tkinter import Button
from Routers import BaseCalculater

class StandardCalculator(BaseCalculater):
    def __init__(self,parent, theme, history_manager, image_manager):
        super().__init__("standard", parent,theme,image_manager,history_manager,{"÷":"/","ᵡ":"*"})
        self.height = 550
        self.width = 340
        self._ui_setup()
    
    def _ui_setup(self):
        super()._ui_setup()
        
        Buttons_config = [[("clear",self.fxn[0].clear_display),("Bracket",self.fxn[0].toggle_bracket),("Back_space",self.fxn[0].backspace),("divide",lambda: self.fxn[0].add_operator(' ÷ '))],
                   [("S7",lambda:self.fxn[0].add_number(7)),("S8",lambda:self.fxn[0].add_number(8)),("S9",lambda:self.fxn[0].add_number(9)),("mult",lambda: self.fxn[0].add_operator(' ᵡ '))],
                   [("S4",lambda:self.fxn[0].add_number(4)),("S5",lambda:self.fxn[0].add_number(5)),("S6",lambda:self.fxn[0].add_number(6)),("add",lambda: self.fxn[0].add_operator(' + '))],
                   [("S1",lambda:self.fxn[0].add_number(1)),("S2",lambda:self.fxn[0].add_number(2)),("S3",lambda:self.fxn[0].add_number(3)),("subtr",lambda: self.fxn[0].add_operator(' - '))],
                   [("Ss",self.fxn[0].change_sign),("S0",lambda:self.fxn[0].add_number(0)),("point",lambda:self.fxn[0].update_display('.')),("equal",self.calculate)]]
        
        y_pointer  = 200
        width,height = 85,70
        for buttons in Buttons_config:
            x_pointer = 0
            for image, function in buttons:
                Button(
                    self.frame,image = self.image_manager.get(self.name,image),
                    bd=0,activebackground=self.theme['buttonactivebg'], command= function
                    ).place(y=y_pointer, x=x_pointer, width=width, height=height)
                x_pointer += width
            y_pointer += height
