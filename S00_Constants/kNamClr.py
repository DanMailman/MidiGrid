"""
kNamClr.py

This module defines constants and dictionaries for color names and RGB values.
It provides mappings between color names and their corresponding RGB values, and vice versa.

Constants:
    - RED: The RGB value for the color red.
    - GREEN: The RGB value for the color green.
    - BLUE: The RGB value for the color blue.
    - (Additional constants...)

Dictionaries:
    - COLOR_NAMES: A dictionary mapping color names to their RGB values.
    - COLOR_RGBS: A dictionary mapping RGB values to color names.
"""
# RGB color constants
RED,    GREEN,     BLUE,     YELLOW   = (255,   0,   0), (  0, 255,   0), (  0,   0, 255), (255, 255,   0)
ORANGE, PURPLE,    CYAN,     MAGENTA  = (255, 165,   0), (128,   0, 128), (  0, 255, 255), (255,   0, 255)
LIME,   PINK,      TEAL,     LAVENDER = (191, 255,   0), (255, 192, 203), (  0, 128, 128), (230, 230, 250)
BROWN,  BEIGE,     MAROON,   MINT     = (165,  42,  42), (245, 245, 220), (128,   0,   0), (189, 252, 201)
OLIVE,  CORAL,     NAVY,     GREY     = (128, 128,   0), (255, 127,  80), (  0,   0, 128), (128, 128, 128)
PEACH,  TURQUOISE, SKY_BLUE, PLUM     = (255, 229, 180), ( 64, 224, 208), (135, 206, 235), (221, 160, 221)
GOLD,   SILVER,    BRONZE,   COPPER   = (255, 215,   0), (192, 192, 192), (205, 127,  50), (184, 115,  51)
SALMON, KHAKI,     IVORY,    SCARLET  = (250, 128, 114), (240, 230, 140), (255, 255, 240), (255,  36,   0)

# Dictionary mapping RGB triplets to color names
COLOR_NAMES = {
    RED:    'Red',    GREEN: 'Green',         BLUE:     'Blue',     YELLOW:   'Yellow',
    ORANGE: 'Orange', PURPLE: 'Purple',       CYAN:     'Cyan',     MAGENTA:  'Magenta',
    LIME:   'Lime',   PINK: 'Pink',           TEAL:     'Teal',     LAVENDER: 'Lavender',
    BROWN:  'Brown',  BEIGE: 'Beige',         MAROON:   'Maroon',   MINT:     'Mint',
    OLIVE:  'Olive',  CORAL: 'Coral',         NAVY:     'Navy',     GREY:     'Grey',
    PEACH:  'Peach',  TURQUOISE: 'Turquoise', SKY_BLUE: 'Sky Blue', PLUM:     'Plum',
    GOLD:   'Gold',   SILVER: 'Silver',       BRONZE:   'Bronze',   COPPER:   'Copper',
    SALMON: 'Salmon', KHAKI: 'Khaki',         IVORY:    'Ivory',    SCARLET:  'Scarlet'
}
# Dictionary mapping color names to RGB triplets
COLOR_RGBS = {v: k for k, v in COLOR_NAMES.items()}
