import os
import json
from tkinter import PhotoImage

class ImageManager:
    def __init__(self, data_dir:str, theme_dir: str, availabe_themes):
        self.Image_galary = {}
        self.IMAGE_FILE_PATHS = self.__get_image_paths(data_dir)
        self.theme_dir = theme_dir
        self.availabe_themes = availabe_themes
        
    def __get_image_paths(self,data_dir:str):
        file_path = os.path.join(data_dir, 'image_data.json')
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    
    def get(self,dir:str,image:str) -> PhotoImage:
        return self.Image_galary[dir][image]
    
    def load(self, theme:str):
        if theme in self.availabe_themes:
            self.__load_images(Theme_dependent=True, Theme_independent=True, current_theme=theme)
            
    def refresh(self,theme:str):
        if theme in self.availabe_themes:
            self.__load_images(Theme_dependent=True, Theme_independent=False, current_theme=theme)
    
    def __load_images(self, Theme_dependent: bool, Theme_independent: bool, current_theme:str):
        Folders = list(self.IMAGE_FILE_PATHS.keys())
        if Theme_independent:
            for folder in Folders[:5]:
                collection = {}
                for image,path in self.IMAGE_FILE_PATHS[folder].items():
                    collection[image] = PhotoImage(file=path)
                self.Image_galary[folder] = collection               
        
            theme_icons = []
            for theme in self.availabe_themes:
                path = os.path.join(self.theme_dir,theme,'thm.png')
                image = PhotoImage(file=path)
                theme_icons.append(image)                
            self.Image_galary['Theme']['icons'] = theme_icons
            
        if Theme_dependent:
            for folder in Folders[5:]:
                collection = {}
                for image,path in self.IMAGE_FILE_PATHS[folder].items():
                    path = os.path.join(self.theme_dir,current_theme,path)
                    collection[image] = PhotoImage(file=path)
                self.Image_galary[folder] = collection