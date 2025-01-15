from tkinter import Label, StringVar, Entry, Button
from Routers import Baseframe

class ProgrammingCalculator(Baseframe):
    def __init__(self, parent, theme, image_manager):
        super().__init__("programming", parent, theme, image_manager)
        self.height = 510
        self.width = 425
        self.dece = StringVar()
        self.hexa = StringVar()
        self.octa = StringVar()
        self.bine = StringVar()
        self.Mode = StringVar()
        self.Mode.set("decimal")
        self.Buttons = []
        self._ui_setup()
        self.__change_mode(None, Mode = self.Mode.get())
        
    def _ui_setup(self):
        super()._ui_setup()
        Decbox = Entry(self.frame,font=("Comic Sans MS",20),
                       textvariable = self.dece,bd=0,
                       bg=self.theme["displaybg"],fg=self.theme["displayfg"])
        
        Hexbox = Entry(self.frame,font=("Comic Sans MS",12),
                       textvariable = self.hexa,bd=0,
                       bg=self.theme["HOBbg"],fg=self.theme["HOBfg"])
        
        Octbox = Entry(self.frame,font=("Comic Sans MS",12),
                       textvariable = self.octa,bd=0,
                       bg=self.theme["HOBbg"],fg=self.theme["HOBfg"])
        
        Binbox = Entry(self.frame,font=("Comic Sans MS",12),
                       textvariable = self.bine,bd=0,
                       bg=self.theme["HOBbg"],fg=self.theme["HOBfg"])

        hexlab = Label(self.frame,image = self.image_manager.get(self.name,"H"))
        octlab = Label(self.frame,image = self.image_manager.get(self.name,"Oc"))
        binlab = Label(self.frame,image = self.image_manager.get(self.name,"Bi"))
        
        button_config = [[("clear"),("Back_space"),("S7"),("S8"),("S9")],
                         [("A"),("B"),("S4"),("S5"),("S6")],
                         [("C"),("D"),("S1"),("S2"),("S3")],
                         [("EE_"),("F"),("Ss"),("S0"),("equal")]]
        
        y_offset  = 230
        width,height = 85,70
        for row in button_config:
            x_offset = 0
            buttons = []
            for image in row:
                button = Button(self.frame, image = self.image_manager.get(self.name,image),
                                activebackground=self.theme["buttonactivebg"],bg=self.theme["buttonactivebg"]
                                ,bd=0)
                buttons.append(button)
                button.place(y=y_offset, x=x_offset, width=width, height=height)
                x_offset += width
            self.Buttons.append(buttons)
            y_offset += height
            
        Decbox.bind("<FocusIn>",lambda event: self.__change_mode(event, 'decimal'))
        Hexbox.bind("<FocusIn>",lambda event: self.__change_mode(event, 'hexadecimal'))
        Octbox.bind("<FocusIn>",lambda event: self.__change_mode(event, 'octadecimal'))
        Binbox.bind("<FocusIn>",lambda event: self.__change_mode(event, 'binary'))
        
        hexlab.place(x=3,y=122,width=45,height=25)
        octlab.place(x=3,y=154,width=45,height=25)
        binlab.place(x=3,y=186,width=45,height=25)

        Decbox.place(x=23,y=60,height=50,width=379)
        Hexbox.place(x=64,y=122,width=347,height=25)
        Octbox.place(x=64,y=154,width=347,height=25)
        Binbox.place(x=64,y=186,width=347,height=25)
        
    def __change_mode(self,event, Mode:str):
        self.Mode.set(Mode)
        state_map = States_map.get_state_map(Mode)
        for button_row, state_row in zip(self.Buttons, state_map):
            for button, state in zip(button_row, state_row):
                button['state'] = state
        
class States_map:
    states_map = [
        [
            [("normal"), ("normal"), ("normal"), ("normal"), ("normal")],
            [("disabled"), ("disabled"), ("normal"), ("normal"), ("normal")],
            [("disabled"), ("disabled"), ("normal"), ("normal"), ("normal")],
            [("disabled"), ("disabled"), ("normal"), ("normal"), ("normal")]
        ],
        [
            [("normal"), ("normal"), ("normal"), ("normal"), ("normal")],
            [("normal"), ("normal"), ("normal"), ("normal"), ("normal")],
            [("normal"), ("normal"), ("normal"), ("normal"), ("normal")],
            [("normal"), ("normal"), ("normal"), ("normal"), ("normal")]
        ],
        [
            [("normal"), ("normal"), ("normal"), ("disabled"), ("disabled")],
            [("disabled"), ("disabled"), ("normal"), ("normal"), ("normal")],
            [("disabled"), ("disabled"), ("normal"), ("normal"), ("normal")],
            [("disabled"), ("disabled"), ("normal"), ("normal"), ("normal")]
        ],
        [
            [("normal"), ("normal"), ("disabled"), ("disabled"), ("disabled")],
            [("disabled"), ("disabled"), ("disabled"), ("disabled"), ("disabled")],
            [("disabled"), ("disabled"), ("normal"), ("disabled"), ("disabled")],
            [("disabled"), ("disabled"), ("normal"), ("normal"), ("normal")]
        ]
    ]
    
    @staticmethod
    def get_state_map(Mode: str):
        if Mode == 'decimal':
            return States_map.states_map[0]
        elif Mode == 'hexadecimal':
            return States_map.states_map[1]
        elif Mode == 'octadecimal':
            return States_map.states_map[2]
        else:
            return States_map.states_map[3]