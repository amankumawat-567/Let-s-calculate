from tkinter import Frame, Button, Canvas, StringVar
import tkinter.ttk as ttk
from typing import Dict
from module import ImageManager, HistoryManager

class History:
    def __init__(self,display: StringVar, frame:Frame, frame_width:int, history_manager: HistoryManager,image_manager: ImageManager, replacement_dict: Dict[str,str]):
        self.frame = frame
        self.frame_width = frame_width
        self.canvas = Canvas(self.frame, bg="#0d1528", bd=0, highlightthickness=0)
        self.hisrory_frame = Frame(self.canvas, bg="#0D1528", bd=0)
        self.display = display
        self.history_manager = history_manager
        self.image_manager = image_manager
        self.replacement_dict = replacement_dict
        self._ui_setup()
        
    def _ui_setup(self):
        style = ttk.Style(self.frame)
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", gripcount=0, 
                           background="#00b0f0", darkcolor="#0d1528", 
                           lightcolor="#0d1528", troughcolor="#0d1528", 
                           bordercolor="#0d1528", arrowcolor="#0d1528")

        scroll_bar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)

        # Get all history from the HistoryManager
        history_entries = self.history_manager.get_all()
        
        # Create buttons for all history entries
        buttons = []
        for entry in history_entries:
            question = entry['Ques']
            answer = entry['Ans']

            # Replace any placeholders or formatting
            for key, value in self.replacement_dict.items():
                question = question.replace(value, key)

            # Create question and answer buttons
            question_button = Button(self.hisrory_frame, bg="#0d1528", fg="white",
                                     font=('Bookman Old Style', 10), width=43,
                                     bd=0, text=question, activebackground="#0d1528",
                                     command=lambda q=question: self.display.set(self.display.get() + q))
            
            answer_button = Button(self.hisrory_frame, bg="#0d1528", fg="cyan", 
                                   font=('Bookman Old Style', 20), width=20, 
                                   bd=0, text=str(answer), activebackground="#0d1528", 
                                   command=lambda ans=str(answer): self.display.set(self.display.get() + ans))

            buttons.extend([question_button, answer_button])
        
        # Pack all buttons at once
        for button in buttons:
            button.pack()

        self.canvas.create_window(0, 0, anchor='nw', window=self.hisrory_frame)
        self.canvas.update_idletasks()

        # Configure the scrollbar after all content is added
        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=scroll_bar.set)
        
        clear_hist_but = Button(self.frame, bg="#0D1528", activebackground="#0D1528",
                                bd=0, image=self.image_manager.get("History","clear_hist"),
                                command=self.clear_history)
        
        clear_hist_but.place(x=self.frame_width, y=505, height=45, width=360)

        # Place canvas and scrollbar
        self.canvas.place(x=self.frame_width, y=40, height=465, width=360)
        scroll_bar.place(x=self.frame_width + 342, y=40, height=465)
        scroll_bar.set(0.2, 0.3)
        
    def clear_history(self):
        # Clear the history from the JSON file
        self.history_manager.delete_all()

        # Clear the history from the UI
        for widget in self.hisrory_frame.pack_slaves():
            widget.destroy()