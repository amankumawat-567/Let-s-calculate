class PackTemplate:
    def __init__(self,display,max_length=None):
        self.display = display
        self.max_length = max_length

    def update_display(self, text):
        """
        Update the display text, ensuring it doesn't exceed the max length.
        """
        current = self.display.get()
        if self.max_length and len(current) >= self.max_length:
            self.display.set(current[:self.max_length - 1])
        self.display.set(current + text)