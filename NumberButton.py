from setup import *
from Button import Button

# See Button.py for info

class NumberButton(Button):
    number = int
    x = int
    y = int

    def __init__(self, number, x, y):
        self.text = str(number)
        self.x = x
        self.y = y
        self.width = button_width
        self.height = button_height
        self.inactive_color = number_button_inactive_color
        self.active_color = number_button_active_color
        self = Button(self.text, self.x, self.y, self.width, self.height, self.inactive_color, self.active_color)

