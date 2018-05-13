#!/usr/bin/env python3
# import pdb
import pygame
import sys
from globals import *
from Screen import Screen
from Calculator import Calculator

pygame.init()

screen = Screen()
calc = Calculator()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                screen.update_value()
                screen.print_result()

            window.fill(window_fill_color)
            screen.draw_screen()
            calc.draw_buttons()

            pygame.display.update()
            clock.tick(20)

main()
# pdb.set_trace()
