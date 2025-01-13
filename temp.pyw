from module.GetCredentials import *
from ui_setup import initialize_main_window
from module import ThemeManager, ImageManager, HistoryManager
from Routers import StandardCalculator, ScientificCalculater

def main():
    Theme_manager = ThemeManager(theme_dir=THEME_DIRECTORY, data_dir=DATA_DIRECTORY)
    Iamge_manager = ImageManager(DATA_DIRECTORY,THEME_DIRECTORY,Theme_manager.available_themes)
    history_manager = HistoryManager(HISTORY)
    
    ACTIVE_THEME = Theme_manager.get_theme()
    
    window = initialize_main_window(geo=Theme_manager.get_locus())
    
    Iamge_manager.load(theme = ACTIVE_THEME['name'])
    history_manager.load_history()
    
    window.iconphoto(False, Iamge_manager.get(dir='Icons', image='Calculater_icon(16x16)'))
    
    standard_calculator = StandardCalculator(parent=window, theme=ACTIVE_THEME,
                                             history_manager = history_manager,
                                             image_manager = Iamge_manager)
    
    scientific_calculater = ScientificCalculater(parent=window, theme=ACTIVE_THEME,
                                             history_manager = history_manager,
                                             image_manager = Iamge_manager)
    
    scientific_calculater.show()
    
    window.mainloop()

if __name__ == "__main__":
    main()