import pygame
import string
import math
from Calculator import Calculator
from setup import *

class Screen:
    init_text = '0'
    error = False

    def __init__(self):
        self.text = '0'
        self.x = 100
        self.y = 80
        self.width = 390
        self.height = 80
        self.calc = Calculator()

    def draw_screen(self):
        pygame.draw.rect(window, screen_color, (self.x, self.y, self.width, self.height))
        smallText = pygame.font.Font(font_style, font_size)
        textSurf, textRect = text_objects(self.text, smallText)
        textRect.center = ( (self.x+(self.width/2)), (self.y+(self.height/2)) )
        window.blit(textSurf, textRect)

    # def get_value(self):
    #     return self.text

    def update_value(self):
        if self.calc.get_button_value() == 'AC':
            self.text = self.init_text
            return
        elif self.text == '0' and self.calc.get_button_value() != None or self.error and self.calc.get_button_value() != None:
            if self.error:
                self.error = False
            self.text = ''
        
        if self.calc.get_button_value() != '=':
            if self.calc.get_button_value() != None:
                self.text += self.calc.get_button_value()

    # need factorial math.factorial
    def print_result(self):
        if self.calc.get_button_value() != '=':
            return

        if 'tan' in self.text:
            self.text = self.text.replace('tan', '')
            self.text = self.text.replace('(', '')
            self.text = self.text.replace(')', '')
            try:
                self.text = math.tan(eval(self.text))
            except TypeError as err:
                print(err)
                self.text = self.init_text

        elif 'cos' in self.text:
            self.text = self.text.replace('cos', '')
            self.text = self.text.replace('(', '')
            self.text = self.text.replace(')', '')
            try:
                self.text = math.cos(eval(self.text))
            except TypeError as err:
                print (err)
                self.text = self.init_text
        
        elif 'sin' in self.text:
            self.text = self.text.replace('sin', '')
            self.text = self.text.replace('(', '')
            self.text = self.text.replace(')', '')
            try:
                self.text = math.sin(eval(self.text))
            except TypeError as err:
                print(err)
                self.text = self.init_text

        elif '^' in self.text:
            try:
                integers = self.text.split('^')
                self.text = str(math.pow(int(integers[0]), int(integers[1])))
            except ValueError as err:
                print(err)
                self.text = self.init_text

        elif '!' in self.text:
            try:
                if self.text[0] == '!':
                    self.text = self.text.replace('!', '')
                    self.text = self.text.replace('(', '')
                    self.text = self.text.replace(')', '')
                    self.text = str(math.factorial(int(self.text)))
                else:
                    self.error = True
                    self.text = 'Use factorial as follows: !(x)'
            except ValueError as err:
                print(err)
                self.text = self.init_text
            
        else:
            try:
                self.text = eval(self.text)
            except ZeroDivisionError as ze:
                self.error = True
                self.text = 'You cannot divide a number by 0'
            except SyntaxError as sy:
                self.error = True
                self.text = 'There was a syntax error'
        
        self.text = str(self.text)
        