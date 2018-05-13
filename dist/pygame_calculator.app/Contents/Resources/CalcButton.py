from globals import *
from Button import Button

# See Button.py for info

class CalcButton(Button):
    number = int
    x = int
    y = int

    def __init__(self, value, x, y):
        self.text = str(value)
        self.x = x
        self.y = y
        self.width = button_width
        self.height = button_height
        self.inactive_color = calc_button_inactive_color
        self.active_color = calc_button_active_color
        self = Button(self.text, self.x, self.y, self.width, self.height, self.inactive_color, self.active_color)

