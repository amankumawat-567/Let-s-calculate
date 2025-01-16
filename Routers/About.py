from Routers import Baseframe

class About(Baseframe):
    def __init__(self, parent, theme, image_manager):
        super().__init__('About', parent, theme, image_manager)
        self.height = 550
        self.width = 340
        self._ui_setup()