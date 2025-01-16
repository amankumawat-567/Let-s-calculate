from tkinter import Tk, Frame, Canvas, Label, Button
import tkinter.ttk as ttk
from typing import Dict
from module import ImageManager

class Pannel:
    def __init__(self, parent: Tk, theme: Dict[str,str], image_manager: ImageManager, switch_fxn):
        self.parent = parent
        self.frame = Frame(self.parent,bg="#0d1528")
        self.name = "PannelButton"
        self.image_manager = image_manager
        self.theme = theme
        self.switch_fxn = switch_fxn
        self._ui_setup()
        
    def _ui_setup(self):        
        self.canvas = Canvas(self.frame,bg="#0d1528",bd=0,highlightthickness=0)
        astyle = ttk.Style(self.frame)
        astyle.theme_use('clam')
        astyle.configure("Vertical.TScrollbar", gripcount=0,background="#00b0f0",
                         darkcolor="#0d1528",lightcolor="#0d1528",troughcolor="#0d1528",
                         bordercolor="#0d1528",arrowcolor="#0d1528")
        
        self.scroll_y = ttk.Scrollbar(self.frame,orient="vertical", command=self.canvas.yview)
        frame = Frame(self.canvas,bg="#0d1528",bd=0)
        
        # Calculaters
        Calculater = Label(frame,image = self.image_manager.get(self.name,"CAL"),
                           height=51,bg="#0d1528",bd=0).grid(row=0,column=0,columnspan=2)
        Standard = Button(frame, image=self.image_manager.get(self.name,"Standard"),bd=0,command=lambda:self.switch_fxn('standard_calculator'),
                          bg="#0d1528",height=238,width=115,activebackground="#0d1528").grid(row=1,column=0,rowspan=2,padx=2,pady=2)
        Scientific = Button(frame, image=self.image_manager.get(self.name,"Scientific"),bd=0,command=lambda:self.switch_fxn('scientific_calculater'),
                            bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=1,column=1,padx=2,pady=2)
        Programmer = Button(frame, image=self.image_manager.get(self.name,"Programmer"),bd=0,command=lambda:self.switch_fxn('programming_caculator'),
                            bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=2,column=1,padx=2,pady=2)
        
        # Convertors
        Convertor = Label(frame,image = self.image_manager.get(self.name,"conver"),
                          height=51,bg="#0d1528",bd=0).grid(row=4,column=0,columnspan=2)
        Currency = Button(frame, image=self.image_manager.get(self.name,"Currency"),command=lambda:self.switch_fxn('currency_convertor'),
                          bd=0,bg="#0d1528",height=115,width=234,activebackground="#0d1528").grid(row=5,column=0,columnspan=2,padx=2,pady=2)
        Volume = Button(frame, image=self.image_manager.get(self.name,"Volume"),command=lambda:self.switch_fxn('volume convertor'),
                        bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=6,column=0,padx=2,pady=2)
        Length = Button(frame, image=self.image_manager.get(self.name,"Length"),command=lambda:self.switch_fxn('length convertor'),
                        bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=6,column=1,padx=2,pady=2)
        Weight_and_Mass = Button(frame, image=self.image_manager.get(self.name,"Weight and Mass"),command=lambda:self.switch_fxn('mass convertor'),
                                 bd=0,bg="#0d1528",height=238,width=115,activebackground="#0d1528").grid(row=7,column=0,rowspan=2,padx=2,pady=2)
        Temperature = Button(frame, image=self.image_manager.get(self.name,"Temperature"),command=lambda:self.switch_fxn('temperature convertor'),
                             bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=7,column=1,padx=2,pady=2)
        Energy = Button(frame, image=self.image_manager.get(self.name,"Energy"),command=lambda:self.switch_fxn('energy convertor'),
                        bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=8,column=1,padx=2,pady=2)
        Area = Button(frame, image=self.image_manager.get(self.name,"Area"),command=lambda:self.switch_fxn('area convertor'),
                      bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=9,column=0,padx=2,pady=2)
        Speed= Button(frame, image=self.image_manager.get(self.name,"Speed"),command=lambda:self.switch_fxn('speed convertor'),
                      bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=9,column=1,padx=2,pady=2)
        Time = Button(frame, image=self.image_manager.get(self.name,"Time"),command=lambda:self.switch_fxn('time convertor'),
                      bd=0,bg="#0d1528",height=115,width=234,activebackground="#0d1528").grid(row=10,column=0,columnspan=2,padx=2,pady=2)
        Data = Button(frame, image=self.image_manager.get(self.name,"Data"),command=lambda:self.switch_fxn('data convertor'),
                      bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=11,column=0,padx=2,pady=2)
        Power= Button(frame, image=self.image_manager.get(self.name,"power"),command=lambda:self.switch_fxn('power convertor'),
                      bd=0,bg="#0d1528",height=238,width=115,activebackground="#0d1528").grid(row=11,column=1,rowspan=2,padx=3,pady=2)
        Pressure = Button(frame, image=self.image_manager.get(self.name,"Pressure"),command=lambda:self.switch_fxn('pressure convertor'),
                          bd=0,bg="#0d1528",height=238,width=115,activebackground="#0d1528").grid(row=12,column=0,rowspan=2,padx=2,pady=2)
        Angle = Button(frame, image=self.image_manager.get(self.name,"Angle"),command=lambda:self.switch_fxn('angle convertor'),
                       bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=13,column=1,padx=2,pady=2)
        
        self.canvas.create_window(0, 0, anchor='nw', window=frame)

        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'),yscrollcommand=self.scroll_y.set)
                            
        self.scroll_y.set(0.2,0.3)

        self.About = Button(self.frame,image=self.image_manager.get(self.name,"About"),
                       bd=0,bg="#0d1528",activebackground="#0d1528")

        self.theme_but = Button(self.frame,image=self.image_manager.get(self.name,"Themes"),
                           bd=0,bg="#0d1528",activebackground="#0d1528")        
        
    def show(self):
        parent_height = self.parent.winfo_height()
        self.About.place(x=0,y=parent_height-38, width=215,height=38)
        self.theme_but.place(x=218,y=parent_height-40,width=38,height=38)
        self.canvas.place(x=0,y=50,height=parent_height-92,width=244)
        self.scroll_y.place(x=244,y=50,height=parent_height-92)
        self.frame.place(x=0,y=0,height=parent_height,width=260)
        
    def hide(self):
        self.About.place_forget()
        self.theme_but.place_forget()
        self.canvas.place_forget()
        self.scroll_y.place_forget()
        self.frame.place_forget()