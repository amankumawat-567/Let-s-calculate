from tkinter import Tk, Button
from module import CredentialsThemplate
from module import ThemeManager, ImageManager, HistoryManager
from Routers import StandardCalculator, ScientificCalculator, ProgrammingCalculator, Convertor, Pannel, Baseframe

class FrameWork:
    def __init__(self):
        self.Active_frame: Baseframe|None = None
        self.pannel_active = False
    
    def get_managers(self,Credentials: CredentialsThemplate):
        self.Theme_manager = ThemeManager(theme_dir=Credentials.THEME_DIRECTORY, data_dir=Credentials.DATA_DIRECTORY)
        self.Iamge_manager = ImageManager(Credentials.DATA_DIRECTORY,Credentials.THEME_DIRECTORY,self.Theme_manager.available_themes)
        self.history_manager = HistoryManager(Credentials.HISTORY)
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
        
    def switch_frame(self,window,Next_frame):
        self.Active_frame.hide()
        self.Active_frame = getattr(self,Next_frame)
        self.Active_frame.show()
        self.__open_pannel()
        window.maxsize(self.Active_frame.width,self.Active_frame.height)
        window.minsize(self.Active_frame.width,self.Active_frame.height)
        
    def __open_pannel(self):
        if self.pannel_active:
            self.pannel.hide()
            self.pannel_active = False
        else:
            self.pannel.show()
            self.pannel_active = True
    
    def __get_slider(self,window):
        self.slider = Button(window ,image = self.Iamge_manager.get("Basic comp","Slider_image"),
                             bd=0,command=self.__open_pannel,activebackground=self.ACTIVE_THEME['HeadButtonActiveBg'])
        self.slider.place(width=40,height=40)
        
    def __get_frames(self,window):
        self.standard_calculator = StandardCalculator(parent=window, theme=self.ACTIVE_THEME,
                                             history_manager = self.history_manager,
                                             image_manager = self.Iamge_manager)
    
        self.scientific_calculater = ScientificCalculator(parent=window, theme=self.ACTIVE_THEME,
                                                history_manager = self.history_manager,
                                                image_manager = self.Iamge_manager)
        
        self.programming_caculator = ProgrammingCalculator(parent=window, theme=self.ACTIVE_THEME,
                                                image_manager = self.Iamge_manager)
        
        self.currency_convertor = Convertor(name='currency convertor', parent=window, theme=self.ACTIVE_THEME,
                                    image_manager=self.Iamge_manager)
        
        self.convertor = Convertor(name='convertor', parent=window, theme=self.ACTIVE_THEME,
                                    image_manager=self.Iamge_manager)
        
        self.pannel = Pannel(parent=window,theme=self.ACTIVE_THEME,image_manager=self.Iamge_manager
                             , switch_fxn = lambda Next_frame: self.switch_frame(window,Next_frame))
        
    def ui_setup(self,window: Tk):
        self.__get_frames(window=window)
        self.__get_slider(window=window)

        self.Active_frame = self.standard_calculator
        self.Active_frame.show()