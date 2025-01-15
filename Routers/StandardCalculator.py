from tkinter import Button
from Routers import BaseCalculater
from module import StandardPack

class StandardCalculator(BaseCalculater):
    def __init__(self,parent, theme, history_manager, image_manager):
        super().__init__("standard", parent,theme,image_manager,history_manager)
        self.height = 550
        self.width = 340
        self.replacement_dict = {"÷":"/","ᵡ":"*"}
        self._ui_setup()
    
    def _ui_setup(self):
        super()._ui_setup()
        
        fxn = StandardPack(self.display,self.displayf,self.replacement_dict)
        
        Buttons_config = [[("clear",fxn.clear_display),("Bracket",fxn.toggle_bracket),("Back_space",fxn.backspace),("divide",lambda: fxn.add_operator(' ÷ '))],
                   [("S7",lambda:fxn.add_number(7)),("S8",lambda:fxn.add_number(8)),("S9",lambda:fxn.add_number(9)),("mult",lambda: fxn.add_operator(' ᵡ '))],
                   [("S4",lambda:fxn.add_number(4)),("S5",lambda:fxn.add_number(5)),("S6",lambda:fxn.add_number(6)),("add",lambda: fxn.add_operator(' + '))],
                   [("S1",lambda:fxn.add_number(1)),("S2",lambda:fxn.add_number(2)),("S3",lambda:fxn.add_number(3)),("subtr",lambda: fxn.add_operator(' - '))],
                   [("Ss",fxn.change_sign),("S0",lambda:fxn.add_number(0)),("point",lambda:fxn.update_display('.')),("equal",fxn.calculate)]]
        
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
