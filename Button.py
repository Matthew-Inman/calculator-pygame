import pygame
from setup import *

# Parent class of CalcButton and NumberButton
# No instances should be created from this class
# 
# CalcButton and NumberButton are instanciated with only three arguments: 
# (output (value or number), x position, y position)
# Their respective sizes and colors can be changed in setup.py

class Button:
    text = str
    x = int
    y = int
    width = int
    height = int
    inactive_color = tuple
    active_color = tuple

    def __init__(self, text, x, y, width, height, inactive_color, active_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
    
    def draw_button(self):
        mouse = pygame.mouse.get_pos()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(window, self.active_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(window, self.inactive_color, (self.x, self.y, self.width, self.height))

        smallText = pygame.font.Font(font_style, font_size)
        textSurf, textRect = text_objects(self.text, smallText)
        textRect.center = ( (self.x+(self.width/2)), (self.y+(self.height/2)) )
        window.blit(textSurf, textRect)

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            return True
        else:
            return False
