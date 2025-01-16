from typing import Callable
from tkinter import Tk, Button, Label
from module import CredentialsThemplate
from module import ThemeManager, ImageManager, HistoryManager
from Routers import StandardCalculator, ScientificCalculator, ProgrammingCalculator, Currency_convertor, Unit_convertor, Pannel, Baseframe, About, ThemeWindow
from Convertors import UnitConvertor, CurrencyConvertor, CurrencyDataUpdater

def __loading__(function: Callable):
    def wrapper(frame_work, window: Tk):
        __loading__ = Label(window,image=frame_work.Iamge_manager.get("Basic comp","Base")
                            )
        __loading__.place(height=550,width=340,bordermode="outside")
        def end():
            __loading__.place_forget()
            frame_work.Active_frame.show()
            frame_work.slider.place(width=40,height=40)
        window.after(1000,end)
        function(frame_work, window)
    return wrapper
    

class FrameWork:
    def __init__(self):
        self.Active_frame: Baseframe|None = None
        self.pannel_active = False
    
    def get_managers(self,Credentials: CredentialsThemplate):
        self.Theme_manager = ThemeManager(theme_dir=Credentials.THEME_DIRECTORY, data_dir=Credentials.DATA_DIRECTORY)
        self.Iamge_manager = ImageManager(Credentials.DATA_DIRECTORY,Credentials.THEME_DIRECTORY,self.Theme_manager.available_themes)
        self.history_manager = HistoryManager(Credentials.HISTORY)
        self.currency_convertor_function = CurrencyConvertor(Credentials.DATA_DIRECTORY)
        self.currency_data_updater = CurrencyDataUpdater(Credentials.API_URL,Credentials.DATA_DIRECTORY)
        self.unit_convertor = UnitConvertor(Credentials.DATA_DIRECTORY)
        self.ACTIVE_THEME = self.Theme_manager.get_theme()
        
    def initialize_main_window(self) -> Tk:
        window = Tk()
        geo = self.Theme_manager.get_locus()
        window.geometry(geo)
        window.wait_visibility(window)
        window.wm_attributes("-alpha",0.9)
        window.title("Calculater")
        return window
    
    def load_icon(self,main_window: Tk):
        main_window.iconphoto(False, self.Iamge_manager.get(dir='Icons', image='Calculater_icon(16x16)'))
    
    def load_data(self):
        self.Iamge_manager.load(theme = self.ACTIVE_THEME['name'])
        self.history_manager.load_history()
        
    def switch_frame(self,window,Next_frame: str):
        self.Active_frame.hide()
        Next_frame = Next_frame.split()
        if Next_frame[-1] == 'convertor':
            self.convertor.set_type(Next_frame[0])
        self.Active_frame = getattr(self,Next_frame[-1])
        self.Active_frame.show()
        self.__open_pannel()
        window.maxsize(self.Active_frame.width,self.Active_frame.height)
        window.minsize(self.Active_frame.width,self.Active_frame.height)
        
    def change_theme(self, theme: str, window: Tk):
        self.Theme_manager.change_theme(theme)
        self.Iamge_manager.refresh(theme)
        self.ACTIVE_THEME = self.Theme_manager.get_theme()
        self._ui_setup(window)
               
    def __open_pannel(self):
        if self.pannel_active:
            self.pannel.hide()
            if self.Active_frame.name == 'About':
                self.slider.config(image=self.Iamge_manager.get("About","slider"))
            elif self.Active_frame.name == 'Theme':
                self.slider.config(image=self.Iamge_manager.get("Theme","Back_but_image"))
            else:
                self.slider.config(image=self.Iamge_manager.get("Basic comp","Slider_image"))
            self.pannel_active = False
        else:
            self.pannel.show()
            self.slider.config(image=self.Iamge_manager.get("PannelButton","slider_close"))
            self.pannel_active = True
    
    def __get_slider(self,window):
        self.slider = Button(window ,image = self.Iamge_manager.get("Basic comp","Slider_image"),
                             bd=0,command=self.__open_pannel,activebackground=self.ACTIVE_THEME['HeadButtonActiveBg'])
        
    def __get_frames(self,window):
        self.standard_calculator = StandardCalculator(parent=window, theme=self.ACTIVE_THEME,
                                             history_manager = self.history_manager,
                                             image_manager = self.Iamge_manager)
    
        self.scientific_calculater = ScientificCalculator(parent=window, theme=self.ACTIVE_THEME,
                                                history_manager = self.history_manager,
                                                image_manager = self.Iamge_manager)
        
        self.programming_caculator = ProgrammingCalculator(parent=window, theme=self.ACTIVE_THEME,
                                                image_manager = self.Iamge_manager)
        
        self.currency_convertor = Currency_convertor(parent=window, theme=self.ACTIVE_THEME,
                                    image_manager=self.Iamge_manager, Convertor_function=self.currency_convertor_function,
                                    data_updater=self.currency_data_updater)
        
        self.convertor = Unit_convertor( parent=window, theme=self.ACTIVE_THEME,
                                    image_manager=self.Iamge_manager, Convertor_function=self.unit_convertor)
        
        self.about = About(parent=window,theme=self.ACTIVE_THEME,image_manager=self.Iamge_manager)
        
        self.Theme_window = ThemeWindow(parent=window,theme=self.Theme_manager,image_manager=self.Iamge_manager,
                                    available_themes=self.Theme_manager.available_themes,theme_changer_fxn= lambda theme: self.change_theme(theme,window))
        
        self.pannel = Pannel(parent=window,theme=self.ACTIVE_THEME,image_manager=self.Iamge_manager
                             , switch_fxn = lambda Next_frame: self.switch_frame(window,Next_frame))
     
    @__loading__
    def _ui_setup(self,window: Tk):
        self.__get_frames(window=window)
        self.__get_slider(window=window)
        self.Active_frame = self.standard_calculator