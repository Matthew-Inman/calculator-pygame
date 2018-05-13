import pygame

# Colors
color = {
    'black': (0,0,0),
    'white': (255,255,255),
    'white_smoke': (240, 240, 240),
    'gainsboro': (220, 220, 220),
    'dark_grey': (64, 64, 64),
    'medium_dark_grey': (75, 75, 75),
    'medium_grey': (104, 104, 104),
    'grey': (135, 135, 135),
    'classic_grey': (151, 151, 151),
    'light_grey': (211, 211, 211),
    'light_blue': (179, 209, 255),
    'medium_blue': (102, 163, 255),
    'medium_dark_blue': (26, 117, 255),
    'darkish_blue': (0, 92, 230),
    'dark_blue': (0, 61, 153)
}

# Text Fonts
font_color = color['white']
font_style = "freesansbold.ttf"
font_size = 20

# Button configs
button_width = 70
button_height = 50
number_button_active_color = color['grey']
number_button_inactive_color = color['classic_grey']
calc_button_active_color = color['dark_grey']
calc_button_inactive_color = color['medium_grey']

# Main window setup
window_width = 600
window_height = 600
window_fill_color = color['light_grey']
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('My Calculator')

# Screen setup
screen_color = color['classic_grey']

# Time setup
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, font_color)
    return textSurface, textSurface.get_rect()
