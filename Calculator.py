from setup import *
from Button import Button
from CalcButton import CalcButton
from NumberButton import NumberButton

class Calculator:
    row_x_margin = 80
    row_x1 = 100
    row_x2 = row_x1 + row_x_margin
    row_x3 = row_x2 + row_x_margin
    row_x4 = row_x3 + row_x_margin
    row_x5 = row_x4 + row_x_margin

    row_y_margin = 60
    row_1_y = 200
    row_2_y = row_1_y + row_y_margin
    row_3_y = row_2_y + row_y_margin
    row_4_y = row_3_y + row_y_margin
    row_5_y = row_4_y + row_y_margin

    buttons = []

    # Buttons as they appear visualy from left to right, each block is one row
    button_left_parenthese = CalcButton('(', row_x1, row_1_y)
    button_right_parenthese = CalcButton(')', row_x2, row_1_y)
    button_percent = CalcButton('%', row_x3, row_1_y)
    button_clear = CalcButton('AC', row_x4, row_1_y)
    button_factorial = CalcButton('!', row_x5, row_1_y)

    button_7 = NumberButton(7, row_x1, row_2_y)
    button_8 = NumberButton(8, row_x2, row_2_y)
    button_9 = NumberButton(9, row_x3, row_2_y)
    button_division = CalcButton('/', row_x4, row_2_y)
    button_power = CalcButton('^', row_x5, row_2_y)

    button_4 = NumberButton(4, row_x1, row_3_y)
    button_5 = NumberButton(5, row_x2, row_3_y)
    button_6 = NumberButton(6, row_x3, row_3_y)
    button_multiplication = CalcButton('*', row_x4, row_3_y)
    button_tan = CalcButton('tan', row_x5, row_3_y)


    button_1 = NumberButton(1, row_x1, row_4_y)
    button_2 = NumberButton(2, row_x2, row_4_y)
    button_3 = NumberButton(3, row_x3, row_4_y)
    button_substraction = CalcButton('-', row_x4, row_4_y)
    button_sin = CalcButton('sin', row_x5, row_4_y)

    button_0 = NumberButton(0, row_x1, row_5_y)
    button_dot = CalcButton('.', row_x2, row_5_y)
    button_equal = Button('=', row_x3, row_5_y, button_width, button_height, color['medium_dark_blue'], color['darkish_blue'])
    button_addition = CalcButton('+', row_x4, row_5_y)
    button_cos = CalcButton('cos', row_x5, row_5_y)


    def __init__(self):
        self.buttons.append(self.button_7)
        self.buttons.append(self.button_8)
        self.buttons.append(self.button_9)
        self.buttons.append(self.button_4)
        self.buttons.append(self.button_5)
        self.buttons.append(self.button_6)
        self.buttons.append(self.button_1)
        self.buttons.append(self.button_2)
        self.buttons.append(self.button_3)
        self.buttons.append(self.button_0)
        self.buttons.append(self.button_dot)
        self.buttons.append(self.button_equal)
        self.buttons.append(self.button_addition)
        self.buttons.append(self.button_left_parenthese)
        self.buttons.append(self.button_right_parenthese)
        self.buttons.append(self.button_percent)
        self.buttons.append(self.button_clear)
        self.buttons.append(self.button_division)
        self.buttons.append(self.button_multiplication)
        self.buttons.append(self.button_substraction)
        self.buttons.append(self.button_power)
        self.buttons.append(self.button_tan)
        self.buttons.append(self.button_sin)
        self.buttons.append(self.button_cos)
        self.buttons.append(self.button_factorial)

    def draw_buttons(self):
        for button in self.buttons:
            button.draw_button()

    def get_button_value(self):
        for button in self.buttons:
            if button.is_clicked():
                return button.text

