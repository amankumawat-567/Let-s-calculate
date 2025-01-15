from module import CREDENTIALS
from ui_setup import FrameWork

def main():
    Calculator = FrameWork()
    Calculator.get_managers(Credentials=CREDENTIALS)
    
    Window = Calculator.initialize_main_window()
    
    Calculator.load_data()
    Calculator.load_icon(Window)
    Calculator.ui_setup(Window)
    
    Window.mainloop()

if __name__ == "__main__":
    main()