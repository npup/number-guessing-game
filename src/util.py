from __future__ import annotations
from enum import Enum, auto


def prompt_input(label: str) -> str:
    """
    Prompt the user for string input with a given label.

    Args:
        label (str): The prompt label to display.
    """
    return input(f"{Indicators.QUESTION} {label}: ")


def prompt_input_int(label: str) -> int:
    """
    Prompt for an integer input with the given label.

    Repeatedly asks until a valid integer is provided.

    Args:
        label (str): The prompt label to display.

    Returns:
        int: The valid integer input.
    """
    while True:
        attempt = input(f"{Indicators.QUESTION} {label}: ")
        if attempt.isnumeric():
            return int(attempt)
        print_error("Not an integer. Try again!")


def prompt_input_boolean(label: str) -> bool:
    while True:
        answer = prompt_input(f"{label} ({Choice.YES}/{Choice.NO})")
        choice = Choice.from_string(answer)
        print("answer", answer, choice)
        match choice:
            case Choice.YES | Choice.NO:
                return choice == Choice.YES
            case _:
                print_error(
                    f'Enter "{Choice.YES}" or "{Choice.NO}" for yes and no, respectively.'
                )


def print_error(message: str) -> None:
    """
    Print a message with the ERROR indicator.

    Args:
        message (str): The message to be printed.
    """
    __print_message(message, Indicators.ERROR)


def print_fatal(message: str) -> None:
    """
    Print a message with the FATAL indicator.

    Args:
        message (str): The message to be printed.
    """
    __print_message(message, Indicators.FATAL)


def print_warning(message: str) -> None:
    """
    Print a message with the WARNING indicator.

    Args:
        message (str): The message to be printed.
    """
    __print_message(message, Indicators.WARNING)


def print_ok(message: str) -> None:
    """
    Print a message with the OK indicator.

    Args:
        message (str): The message to be printed.
    """
    __print_message(message, Indicators.OK)


def print_info(message: str) -> None:
    """
    Print a message with the INFO indicator.

    Args:
        message (str): The message to be printed.
    """
    __print_message(message, Indicators.INFO)


def __print_message(message: str, indicator: str) -> None:
    """
    Print a formatted message with an indicator.

    Args:
        message (str): The message to be printed.
        indicator (str): The indicator to be prepended to the message.
    """
    print(f"{indicator} {message}")


class Indicators:
    """Predefined colored indicators for various message types."""

    class __Codes:
        """ANSI escape codes for text formatting and colors."""

        # bold
        BOLD = "\033[1m"
        # colors
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        BLUE = "\033[34m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        WHITE = "\033[37m"
        # reset
        RESET = "\033[0m"

    INFO = f"{__Codes.BOLD}{__Codes.MAGENTA}[ i ]{__Codes.RESET}"
    QUESTION = f"{__Codes.BOLD}{__Codes.BLUE}[ ? ]{__Codes.RESET}"
    OK = f"{__Codes.BOLD}{__Codes.GREEN}[ ✓ ]{__Codes.RESET}"
    WARNING = f"{__Codes.BOLD}{__Codes.YELLOW}[ ! ]{__Codes.RESET}"
    ERROR = f"{__Codes.BOLD}{__Codes.RED}[ × ]{__Codes.RESET}"
    FATAL = f"{__Codes.BOLD}{__Codes.RED}[×××]{__Codes.RESET}"


class Choice(Enum):
    """Represents a binary choice (Yes/No) in the game."""

    YES = auto()
    NO = auto()

    @classmethod
    def from_string(cls, s: str) -> "Choice" | None:
        """Convert a string input to a Choice enum value.

        Args:
            s: The input string to convert.

        Returns:
            The corresponding Choice enum value if the input is valid,
            or None if the input doesn't match any valid choice.
        """
        match s.lower():
            case "y":
                return Choice.YES
            case "n":
                return Choice.NO
            case _:
                return None

    def __str__(self) -> str:
        match self:
            case Choice.YES:
                return "y"
            case Choice.NO:
                return "n"
            case _:
                return None
