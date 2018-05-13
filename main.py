#!/usr/bin/env python3
import pygame
from setup import *
from Screen import Screen
from Calculator import Calculator

pygame.init()

screen = Screen()
calc = Calculator()

def main():
    user_quit = False

    while not user_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                screen.update_value()
                screen.print_result()
                
            window.fill(window_fill_color)
            screen.draw_screen()
            calc.draw_buttons()

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()
