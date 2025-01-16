from Routers import Baseframe
from tkinter import Label, Canvas, Frame, Button
import tkinter.ttk as ttk
from typing import Callable

class ThemeWindow(Baseframe):
    def __init__(self,parent,theme,image_manager,available_themes,theme_changer_fxn: Callable):
        super().__init__('Theme',parent,theme,image_manager)
        self.width, self.height = 340,550
        self.available_themes = available_themes
        self.change_theme = theme_changer_fxn
        self._ui_setup()
        
    def _ui_setup(self):
        style = ttk.Style(self.frame)
        style.theme_use('vista')
        head = Label(self.frame,image = self.image_manager.get(self.name,"Theme_head"))
        canvas = Canvas(self.frame,bg="white",bd=0,highlightthickness=0)
        scroll_y = ttk.Scrollbar(self.frame,orient="vertical", command=canvas.yview)
        frame = Frame(canvas,bg="white",bd=0)
        
        idx = 0
        columns = 3
        for image, theme_name in zip(self.image_manager.get('Theme', 'icons'), self.available_themes):
            Button(
                frame,image=image,bd=0,
                command=lambda theme_name=theme_name: self.change_theme(theme_name)
            ).grid(row=idx // columns, column=idx % columns, padx=5, pady=10)
            idx += 1
        
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=scroll_y.set)          
        scroll_y.set(0.2,0.3)

        head.place(x=0,y=0,height=150,width=340)
        canvas.place(x=0,y=150,height=400,width=325)
        scroll_y.place(x=325,y=150,height=400)
        
    def show(self):
        super().show()
        __loading__ = Label(self.parent,image=self.image_manager.get("Theme","Loading"))
        __loading__.place(height=550,width=340,bordermode="outside")
        def end():
            __loading__.place_forget()
        self.parent.after(1000,end)