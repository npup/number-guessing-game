"""
Configuration settings for the number guessing game.
This module contains settings used throughout the game.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Settings:
    ###########################
    # debug settings
    ###########################
    # some extra info may be printed with debug = True
    DEBUG: bool = field(default=True)

    ###########################
    # player settings
    ###########################
    # age restriction to play the game
    MINIMUM_AGE_YEARS: int = field(default=18)

    ###########################
    # game settings
    ###########################
    # size of list and range of numbers to guess from
    MINIMUM_YEAR: int = field(default=1900)
    LIST_SIZE: int = field(default=10)
    LIST_NUMBERS_LOWER_BOUND: int = field(default=0)
    LIST_NUMBERS_UPPER_BOUND: int = field(default=100)

    # if list size is smaller than this, game is over
    MIN_LIST_SIZE: int = field(default=3)

    # when clamping the list for phase 2, this is the range used
    RANGE_THRESHOLD: int = field(default=10)

    def __init__(self, **kwargs: Any):
        # Use default values for fields not specified in kwargs
        for field in self.__dataclass_fields__:
            if field not in kwargs:
                kwargs[field] = self.__dataclass_fields__[field].default

        # Initialize fields using object.__setattr__ to bypass frozen=True
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

        self.__post_init__()

    def __post_init__(self):
        self.validate()

    def validate(self) -> None:
        # Validate settings
        if self.LIST_NUMBERS_LOWER_BOUND >= self.LIST_NUMBERS_UPPER_BOUND:
            raise ValueError(f"Lower bound {self.LIST_NUMBERS_LOWER_BOUND} must be \
less than upper bound {self.LIST_NUMBERS_UPPER_BOUND}.")
        if self.MIN_LIST_SIZE > self.LIST_SIZE:
            raise ValueError(f"Minimum list size {self.MIN_LIST_SIZE} cannot be greater \
than list size {self.LIST_SIZE}.")
        range = self.LIST_NUMBERS_UPPER_BOUND + 1 - self.LIST_NUMBERS_LOWER_BOUND
        if range < self.LIST_SIZE:
            raise ValueError(f"There are not enough unique values in the numbers \
range {self.LIST_NUMBERS_LOWER_BOUND} - {self.LIST_NUMBERS_UPPER_BOUND} to fill \
a list of size {self.LIST_SIZE}.")
