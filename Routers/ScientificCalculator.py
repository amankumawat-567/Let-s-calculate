from tkinter import Button
from typing import List
from Routers import BaseCalculater

class ScientificCalculator(BaseCalculater):
    def __init__(self,parent, theme, history_manager, image_manager):
        super().__init__("scientific", parent,theme,image_manager,history_manager)
        self.height = 550
        self.width = 595
        self.replacement_dict = dict(zip(["÷","^","ᵡ","e","ᴨ","³√(","√("], 
                                         ["/","**","*","2.718281828459045","3.141592653589793","cur(","sqr("]))
        self.switchvar: bool = False
        self.angle_unit: str = 'Degrees'
        self.scientific_buttons: List[Button] = []
        self._ui_setup()

    
    def _ui_setup(self):
        super()._ui_setup()
        
        standard_Buttons_config = [[("clear"),("Bracket"),("Back_space"),("divide")],
                   [("S7"),("S8"),("S9"),("mult")],
                   [("S4"),("S5"),("S6"),("add")],
                   [("S1"),("S2"),("S3"),("subtr")],
                   [("Ss"),("S0"),("point"),("equal")]]
        
        scientific_Buttons_config = [[[("Root")],
                    [("sin"),('cos'),('Tan')],
                    [('ln'),('log'),('Bix')],
                    [('ex'),('X2'),('Xy')],
                    [('mod'),('pi'),('e')]],
                    [[("cuberoot")],
                    [("Asin"),('Acos'),('Atan')],
                    [("sinh"),('cosh'),('Tanh')],
                    [("Asinh"),('Acosh'),('Atanh')],
                    [('exp2'),('X3'),('X!')]]]
        
        y_pointer  = 200
        width,height = 85,70
        for buttons in standard_Buttons_config:
            x_pointer = 255
            for button in buttons:
                Button(
                    self.frame,image = self.image_manager.get(self.name,button),
                    bd=0,activebackground=self.theme['buttonactivebg']
                    ).place(y=y_pointer, x=x_pointer, width=width, height=height)
                x_pointer += width
            y_pointer += height
            
        for sets in scientific_Buttons_config:
            Button_set = []
            for row in sets:
                r = []
                for button_image in row:
                    button = Button(self.frame, image=self.image_manager.get(self.name,button_image),
                                    bd=0, activebackground=self.theme['buttonactivebg'])
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

