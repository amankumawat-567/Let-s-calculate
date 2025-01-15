from Routers import Baseframe
from tkinter import StringVar, Entry, Button
import tkinter.ttk as ttk

class Convertor(Baseframe):
    def __init__(self,name:str, parent, theme,image_manager):
        super().__init__(name, parent, theme, image_manager)
        self.combo1 = StringVar()
        self.combo2 = StringVar()
        self.display1 = StringVar()
        self.display2 = StringVar()
        self.action: int = 1
        self.set_dim()
        self._ui_setup()
        
    def _ui_setup(self):
        super()._ui_setup()
        cstyle = ttk.Style()
        cstyle.theme_use('vista')
        
        display1_view = Entry(self.frame,font=("Comic Sans MS",20),textvariable = self.display1,
                              bg=self.theme['displaybg'],bd=0,fg=self.theme['displayfg'])
        
        display2_view = Entry(self.frame,font=("Comic Sans MS",20),textvariable = self.display2,
                              bg=self.theme['displaybg'],bd=0,fg=self.theme['displayfg'])
        
        combobox1 = ttk.Combobox(self.frame,width=15,textvariable=self.combo1)
        combobox2 = ttk.Combobox(self.frame,width=15,textvariable=self.combo2)
        
        if self.name == 'currency convertor':
            upgrade_button = Button(self.frame,image=self.image_manager.get(self.name,'cur_data_upg'),
                                    bd=0,activebackground=self.theme['displaybg'])
            upgrade_button.place(x=22,y=272,height=26,width=156)
        
        button_config = [[("S7"),("S8"),("S9"),("Back_space")],
                         [("S4"),("S5"),("S6"),("Ss")],
                         [("S1"),("S2"),("S3")],
                         [("clear"),("S0"),("point"),("equal")]]
        
        
        y_offset  = 270
        if self.name == 'currency convertor':
            y_offset += 45
        width,height = 85,70
        for buttons in button_config:
            x_offset = 0
            for button in buttons:
                Button(
                    self.frame,image = self.image_manager.get(self.name,button),
                    bd=0,activebackground=self.theme['buttonactivebg']
                    ).place(y=y_offset, x=x_offset, width=width, height=height)
                x_offset += width
            y_offset += height
            
        display1_view.place(x=23,y=55,width=294)
        display2_view.place(x=23,y=165,width=294)
        combobox1.place(x=21,y=117)
        combobox2.place(x=21,y=227)
            
    def set_dim(self):
        if self.name == 'currency convertor':
            self.height = 595
        else:
            self.height = 550
        self.width = 340