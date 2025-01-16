from Routers import Baseframe
from tkinter import StringVar, Entry, Button
import tkinter.ttk as ttk
from FunctionPack import ConverterPack
from Convertors import UnitConvertor, CurrencyConvertor, CurrencyDataUpdater

class Convertor(Baseframe):
    def __init__(self,name:str, parent, theme, image_manager, Convertor_function):
        super().__init__(name, parent, theme, image_manager)
        self.combo1 = StringVar()
        self.combo2 = StringVar()
        self.display1 = StringVar()
        self.display2 = StringVar()
        self.Convertor = ConverterPack(self.display1, self.display2, self.combo1, self.combo2, Convertor_function)
        
    def _ui_setup(self):
        super()._ui_setup()
        cstyle = ttk.Style()
        cstyle.theme_use('vista')
        
        display1_view = Entry(self.frame,font=("Comic Sans MS",20),textvariable = self.display1,
                              bg=self.theme['displaybg'],bd=0,fg=self.theme['displayfg'])
        
        display2_view = Entry(self.frame,font=("Comic Sans MS",20),textvariable = self.display2,
                              bg=self.theme['displaybg'],bd=0,fg=self.theme['displayfg'])
        
        display1_view.bind("<FocusIn>",lambda event: self.Convertor.active_entry(1))
        display2_view.bind("<FocusIn>",lambda event: self.Convertor.active_entry(2))
        
        self.combobox1 = ttk.Combobox(self.frame,width=15,textvariable=self.combo1)
        self.combobox2 = ttk.Combobox(self.frame,width=15,textvariable=self.combo2)            
            
        self.combobox1['state'] = "readonly"
        self.combobox2['state'] = "readonly"
        
        button_config = [[("S7",lambda: self.Convertor.add_number(7)),("S8",lambda: self.Convertor.add_number(8)),("S9",lambda: self.Convertor.add_number(9)),("Back_space",self.Convertor.back_space)],
                         [("S4",lambda: self.Convertor.add_number(4)),("S5",lambda: self.Convertor.add_number(5)),("S6",lambda: self.Convertor.add_number(6)),("Ss",self.Convertor.change_sign)],
                         [("S1",lambda: self.Convertor.add_number(1)),("S2",lambda: self.Convertor.add_number(2)),("S3",lambda: self.Convertor.add_number(3))],
                         [("clear",self.Convertor.clear),("S0",lambda: self.Convertor.add_number(0)),("point",self.Convertor.add_point),("equal",self.Convertor.equals)]]
        
        
        y_offset  = self.height - 280
        width,height = 85,70
        for buttons in button_config:
            x_offset = 0
            for image, function in buttons:
                Button(
                    self.frame,image = self.image_manager.get(self.name,image),
                    bd=0,activebackground=self.theme['buttonactivebg'], command=function
                    ).place(y=y_offset, x=x_offset, width=width, height=height)
                x_offset += width
            y_offset += height
            
        display1_view.place(x=23,y=55,width=294)
        display2_view.place(x=23,y=165,width=294)
        self.combobox1.place(x=21,y=117)
        self.combobox2.place(x=21,y=227)
        
class Currency_convertor(Convertor):
    def __init__(self, parent, theme, image_manager, Convertor_function: CurrencyConvertor, data_updater: CurrencyDataUpdater):
        super().__init__('currency convertor', parent, theme, image_manager, Convertor_function)
        self.height = 595
        self.width = 340
        self.Convertor_function = Convertor_function
        self.data_updater = data_updater
        self.Convertor.set_type('currency')
        self._ui_setup()
        
    def _ui_setup(self):
        super()._ui_setup()
        upgrade_button = Button(self.frame,image=self.image_manager.get(self.name,'cur_data_upg'),
                                    bd=0,activebackground=self.theme['displaybg'],command=self.update_and_refresh)
        upgrade_button.place(x=22,y=272,height=26,width=156)
            
        currencies = self.Convertor_function.get_all_currencies()
        self.combo1.set(currencies[0])
        self.combo2.set(currencies[0])
        self.combobox1['values']=currencies
        self.combobox2['values']=currencies
        
    def update_and_refresh(self):
        self.data_updater.run()
        self.Convertor_function.Refresh()
        
class Unit_convertor(Convertor):
    def __init__(self, parent, theme, image_manager, Convertor_function: UnitConvertor):
        super().__init__('convertor', parent, theme, image_manager, Convertor_function)
        self.height = 550
        self.width = 340
        self.Convertor_function = Convertor_function
        self._ui_setup()
        
    def set_type(self,type):
        self.Convertor.set_type(type)
        units = self.Convertor_function.get_units_by_category(type)
        self.combo1.set(units[0])
        self.combo2.set(units[0])
        self.combobox1['values']=units
        self.combobox2['values']=units