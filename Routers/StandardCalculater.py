from tkinter import Button
from typing import Dict
from Routers import BaseCalculater

class StandardCalculator(BaseCalculater):
    def __init__(self,parent,theme: Dict[str, str] , history_manager, image_manager):
        super().__init__(parent,theme,image_manager,history_manager)
        self.name = "standard"
        self.height = 550
        self.width = 340
        self.replacement_dict = {"÷":"/","ᵡ":"*"}
        self._ui_setup()

    
    def _ui_setup(self):
        super()._ui_setup()
        
        Buttons_config = [[("clear"),("Bracket"),("Back_space"),("divide")],
                   [("S7"),("S8"),("S9"),("mult")],
                   [("S4"),("S5"),("S6"),("add")],
                   [("S1"),("S2"),("S3"),("subtr")],
                   [("Ss"),("S0"),("point"),("equal")]]
        
        y_pointer  = 200
        width,height = 85,70
        for buttons in Buttons_config:
            x_pointer = 0
            for button in buttons:
                Button(
                    self.frame,image = self.image_manager.get(self.name,button),
                    bd=0,activebackground=self.theme['buttonactivebg']
                    ).place(y=y_pointer, x=x_pointer, width=width, height=height)
                x_pointer += width
            y_pointer += height
