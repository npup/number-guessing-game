import regex
from datetime import datetime
import random

import util


class InvalidInputError(Exception):
    """Exception raised for invalid user input.

    This exception is used when the user provides input that doesn't meet
    the required criteria or format in various input functions.
    """

    pass


def read_player_name() -> str:
    """Get and validate the player's full name.

    Returns:
        str: A valid full name in the format 'First Last'.

    Raises:
        InvalidInputError: If the input is not a valid full name or doesn't meet the criteria.
    """
    attempt = util.prompt_input("Full name (first, last)")

    if not regex.match(r"^\p{L}+[\s\t]\p{L}+$", attempt, regex.UNICODE):
        raise InvalidInputError(
            "Enter a first- and a lastname, separated by exactly one (1) white space character."
        )

    names = attempt.split()

    first_name, last_name = names
    if not all(name.isalpha() for name in names):
        raise InvalidInputError("The names shall only contain letters.")

    return f"{first_name} {last_name}"


def read_birthdate() -> str:
    """Get and validate the player's birthdate.

    Returns:
        str: A valid birthdate in the format 'YYYYMMDD'.

    Raises:
        InvalidInputError: If the input is not a valid date or doesn't meet the criteria.
    """
    MINIMUM_YEAR = 1900
    now = datetime.now()
    attempt = util.prompt_input("Enter your birth date [yyyyMMdd]")
    try:
        date = datetime.strptime(attempt, "%Y%m%d")
        if now < date or date.year <= MINIMUM_YEAR:
            raise InvalidInputError(
                f"The year must be in the past (but after {MINIMUM_YEAR}) to be believable!"
            )
        return date.strftime("%Y%m%d")
    except ValueError:
        raise InvalidInputError("Invalid date - use the format yyyyMMdd!")


def calculate_age(birthdate: str) -> int:
    """Calculate age in years from a birthdate string.

    Args:
        birthdate (str): date string with format yyyymmdd

    Returns:
        int: Age in years

    Raises:
        ValueError: If the birthdate string is not in the correct format.
    """
    birth = datetime.strptime(birthdate, "%Y%m%d")
    now = datetime.now()
    age = now.year - birth.year
    if now < birth.replace(year=now.year):
        age -= 1
    return age


def create_numbers(
    list_size: int, lower_bound: int, upper_bound: int
) -> tuple[list[int], int]:
    """Create a list of unique numbers and a lucky number within a specified range.

    This function generates a list of unique random numbers and a separate lucky
    number. It ensures that the list contains no duplicates and includes the
    lucky number, then sorts the list.

    Args:
        list_size (int): The desired size of the final list.
        lower_bound (int): The minimum value for the numbers (inclusive).
        upper_bound (int): The maximum value for the numbers (inclusive).

    Returns:
        tuple[list[int], int]: A tuple containing:
            - A sorted list of integers, unique within the list, within the specified range.
            - A randomly selected lucky number from the same range.
    """
    # create list of numbers to guess from
    numbers = generate_lucky_list(
        size=list_size, lower_bound=lower_bound, upper_bound=upper_bound
    )

    # select one the numbers as the "lucky number"
    secret_number = random.choice(numbers)

    return numbers, secret_number


def generate_lucky_list(size: int, lower_bound: int, upper_bound: int) -> list[int]:
    """Generate list of random numbers within a specified range.

    The numbers are unique within the list.  The list is sorted in ascending order.

    Args:
        size (int): The number of lucky numbers to generate.
        lower_bound (int): The minimum value for the random numbers (inclusive).
        upper_bound (int): The maximum value for the random numbers (inclusive).

    Returns:
        list[int]: A sorted list of 'size' random integers between lower_bound and upper_bound, inclusive.
    """
    numbers = random.sample(range(lower_bound, upper_bound + 1), size)
    return sorted(numbers)


def generate_random_number(lower_bound: int, upper_bound: int) -> int:
    """Generate a random integer within the specified range.

    Args:
        lower_bound (int): The lower bound of the range (inclusive).
        upper_bound (int): The upper bound of the range (inclusive).

    Returns:
        int: A random integer between lower_bound and upper_bound, inclusive.
    """
    return random.randint(lower_bound, upper_bound)


def print_list(message: str, numbers: list[int]) -> None:
    """Print a message followed by a list of numbers.

    Args:
        message (str): The message to print before the list.
        numbers (list[int]): The list of numbers to print.
    """
    print(f"\n{message}:\n{numbers}")


def player_guess_phase1(
    numbers: list[int], secret_number: int
) -> tuple[bool, int, int]:
    """Conduct phase 1 of the player guessing game with a single guess attempt.

    Args:
        numbers (list[int]): The list of numbers to guess from.
        secret_number (int): The number the player needs to guess.

    Returns:
        tuple[bool, int, int]: A tuple containing:
            - A boolean indicating whether the player guessed correctly
            - The number of attempts used in this phase
            - The number guessed by the player
    """
    print_list("Here is the lucky list", numbers)
    print()

    guessed_number = util.prompt_input_int("Enter your guess for the lucky number")
    attempts_count = 1

    if guessed_number == secret_number:
        util.print_ok("Correct!")
        return True, attempts_count, guessed_number

    if guessed_number not in numbers:
        util.print_error(f"Wrong. {guessed_number} is not even in the list.")
    else:
        util.print_error("Wrong.")

    return False, attempts_count, guessed_number


def player_guess_phase2(
    numbers: list[int],
    secret_number: int,
    attempts_count: int,
    guessed_number: int,
    list_min_size: int,
    range_threshold: int,
) -> tuple[bool, int]:
    """Conduct phase 2 of the player guessing game with a shrinking list of numbers.

    Phase 2 continues until either of these events occur:
        - Player guesses the secret number correctly
        - The list of numbers is deemed "too short" for the game to continue

    Args:
        numbers (list[int]): The initial list of numbers.
        secret_number (int): The number the player needs to guess.
        attempts_count (int): The number of attempts made so far.
        guessed_number (int): The number guessed by the player.
        list_min_size: The minimum size the list can shrink to before ending the game.
        range_threshold: The range around the secret number to clamp the list.

    Returns:
        tuple[bool, int]: A tuple containing a boolean indicating if the player
                          guessed correctly, and the total number of attempts after
                          this phase.
    """
    lower_bound = secret_number - range_threshold
    upper_bound = secret_number + range_threshold
    clamped_list = clamp_list(
        numbers=numbers, lower_bound=lower_bound, upper_bound=upper_bound
    )

    while True:
        # remove should always succeed here, but a safe guard is ok
        if guessed_number in clamped_list:
            clamped_list.remove(guessed_number)
        if list_too_short(clamped_list, list_min_size):
            break
        attempts_count += 1
        print_list(f"This is attempt #{attempts_count}. The new list is", clamped_list)
        guessed_number = util.prompt_input_int("Enter your guess for the lucky number")
        if guessed_number == secret_number:
            util.print_ok("Correct!")
            return True, attempts_count
        if guessed_number not in clamped_list:
            util.print_error(f"Wrong. {guessed_number} is not even in the list.")
        else:
            util.print_error("Wrong.")

    return False, attempts_count


def clamp_list(numbers: list[int], lower_bound: int, upper_bound: int) -> list[int]:
    """Create a new list containing only numbers within the specified range.

    Note: The resulting list will not necessarily be shorter than the
    original, as the items in it were randomized from the beginning.

    Args:
        numbers (list[int]): The original list of numbers.
        lower_bound (int): The minimum value to include (inclusive).
        upper_bound (int): The maximum value to include (inclusive).

    Returns:
        list[int]: A new list containing only numbers within the specified range.
    """
    return [number for number in numbers if lower_bound <= number <= upper_bound]


def list_too_short(numbers: list[int], min_size: int) -> bool:
    """Checks if the list is too short and prints a warning if it is.

    Args:
        numbers (list[int]): The list of numbers to check.
        min_size (int): The minimum acceptable length of the list.

    Returns:
        bool: True if the list length is less than min_length, False otherwise.
    """
    if len(numbers) < min_size:
        util.print_warning(f"The list is now too short for game to continue: {numbers}")
        return True
    return False


def play_again() -> bool:
    """Prompts the user to decide whether to play again and returns their decision.

    This function repeatedly prompts the user with the question "Would you like to play again? (y/n)".
    It converts the user's input to lowercase and matches it against "y" for yes and "n" for no.
    If the input is anything else, it prints an error message and prompts the user again.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    while True:
        play_again = util.prompt_input("Would you like to play again? (y/n)")
        match play_again.lower():
            case "y":
                return True
            case "n":
                return False
            case _:
                util.print_error('Enter "y" or "n" for yes and no, respectively.')
