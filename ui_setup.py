from tkinter import Tk

def initialize_main_window(geo: str) -> Tk:
    window = Tk()
    window.geometry(geo)
    window.wait_visibility(window)
    window.wm_attributes("-alpha",0.9)
    window.title("Calculater")
    return window