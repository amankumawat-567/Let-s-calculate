from tkinter import Tk, Frame, Label, StringVar, Entry, Button
from typing import Dict
from module import ImageManager, HistoryManager
from FunctionPack import StandardPack
from Routers import History

class Baseframe:
    def __init__(self,name:str , parent:Tk, theme: Dict[str,str],image_manager: ImageManager):
        self.parent = parent
        self.theme = theme
        self.image_manager = image_manager
        self.name = name
        
        self.frame = Frame(self.parent)
        self.height: int = 0
        self.width: int = 0
        
    def _ui_setup(self):
        head = Label(self.frame,image = self.image_manager.get(self.name,"head"))
        head.place(x=38,y=0,height=40)
        backlabel = Label(self.frame,image = self.image_manager.get(self.name,self.name))
        backlabel.place(x=0,y=40,height=self.height-40,width=self.width)
        
    def show(self):
        self.frame.place(x=0,y=0,height=self.height,width=self.width)

    def hide(self):
        self.frame.place_forget()
        
class BaseCalculater(Baseframe):
    def __init__(self, name:str, parent:Tk, theme: Dict[str,str],image_manager: ImageManager, history_manager: HistoryManager, replacement_dict = Dict[str,str]):
        super().__init__(name, parent, theme, image_manager)
        self.history_manager = history_manager
        
        self.display = StringVar()
        self.displayf = StringVar()
        self.history_is_active:bool = False  
        self.replacement_dict = replacement_dict
        self.fxn = [StandardPack(self.display,self.displayf,self.replacement_dict)]
        
    def _ui_setup(self):
        super()._ui_setup()
        
        displayf_view = Label(self.frame, font=('Bookman Old Style',12),
                              justify='right', textvariable = self.displayf,
                              bg=self.theme['displayfbg'],fg=self.theme['displayffg'])
        
        display_view = Entry(self.frame, font=('Bookman Old Style',30),
                             justify='right',bd=0, textvariable = self.display,
                             bg=self.theme['displaybg'],fg=self.theme['displayfg'])
        
        history_button = Button(self.frame,image = self.image_manager.get("Basic comp","History"),
                             bd=0,activebackground=self.theme["HeadButtonActiveBg"])
        
        history_label = Label(self.frame,image=self.image_manager.get("History","hist"))
        
        displayf_view.place(x=13, y=72, width=self.width - 27, height=25)
        display_view.place(x=23, y=118, width=self.width - 46, height=50)
        
        history_label.place(x=self.width, y=0, width=360, height=40)
        history_button.place(x=self.width - 60, y=0, width=60, height=40)
        
        history_button.configure(command=self.__open_history)
        self.history = History(display=self.display, frame=self.frame,frame_width=self.width ,
                history_manager= self.history_manager, image_manager= self.image_manager, 
                replacement_dict= self.replacement_dict)
        
    def calculate(self):
        if self.display:
            ques,ans = self.fxn[0].calculate()
            if ans != "Error":
                self.history.add_history_entry(question=ques,answer=ans)
                
        
    def __open_history(self):
        if self.history_is_active:
            self.history_is_active = False
            self.parent.maxsize(self.width,self.height)
            self.parent.minsize(self.width,self.height)
        else:
            self.history_is_active = True
            self.parent.maxsize(self.width + 360,self.height)
            self.parent.minsize(self.width + 360,self.height)
        
    def show(self):
        self.frame.place(x=0,y=0,height=self.height,width=self.width + 360)