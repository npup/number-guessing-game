"""
Configuration settings for the number guessing game.
This module contains constants used throughout the game.
"""
from typing import Final

###########################
# debug settings
###########################
# some extra info may be printed with debug = True
DEBUG: Final[bool] = True

###########################
# player settings
###########################
# age restriction to play the game
MINIMUM_AGE_YEARS: Final[int] = 18

###########################
# game settings
###########################
# size of list and range of numbers to guess from
LIST_SIZE: Final[int] = 10
LIST_NUMBERS_LOWER_BOUND: Final[int] = 0
LIST_NUMBERS_UPPER_BOUND: Final[int] = 100
# if list size is smaller than this, game is over
MIN_LIST_SIZE: Final[int] = 3
# when clamping the list, this is the range used
RANGE_THRESHOLD: Final[int] = 10
