import sys

import util
import core
import settings


def play() -> None:
    """Run the main game loop for the number guessing game.

    The number guessing game, version A.
    Handles player input, game logic, and output.
    """

    # sanity check of game settings. game quits if not OK.
    try:
        sanity_check()
    except Exception as e:
        util.print_fatal(str(e))
        sys.exit(1)

    # collect player data
    player_name = get_valid_player_name()
    validate_player_age(settings.MINIMUM_AGE_YEARS)

    # play game until player wants to quit
    while do_guessing_game(player_name):
        util.print_info("Another round of the guessing game coming up...")

    util.print_info(f"Goodbye, {player_name}!")


def get_valid_player_name() -> str:
    """Prompt the user for their full name and validate the input.

    This function repeatedly asks the user for their name (first and last)
    until a valid input is provided.

    Returns:
        str: A valid player name.

    """
    while True:
        try:
            return core.read_player_name()
        except core.InvalidInputError as e:
            util.print_error(str(e))


def validate_player_age(minimum_age_years: int) -> int:
    """Validate player's age against the minimum requirement.

    This function repeatedly prompts the user for their birthdate until a valid input
    that meets the age requirement is provided.

    Args:
        minimum_age_years (int): The minimum age required to proceed.

    Returns:
        int: The player's age in years, once a valid age meeting the minimum requirement is provided.

    """
    while True:
        try:
            player_birthdate = core.read_birthdate()
            player_age = core.calculate_age(player_birthdate)
            if player_age >= minimum_age_years:
                return player_age
            util.print_error(f"Age limit is {minimum_age_years} years.")
        except core.InvalidInputError as e:
            util.print_error(str(e))


def do_guessing_game(player_name: str) -> bool:
    """Execute a round of the number guessing game.

    This function handles the main game logic, including generating the lucky number,
    managing the guessing phases, and displaying the game results.

    Args:
        player_name (str): The name of the current player.

    Returns:
        bool: True if the player wants to play again, False otherwise.

    """

    lucky_list, lucky_number = core.create_numbers(
        list_size=settings.LIST_SIZE,
        lower_bound=settings.LIST_NUMBERS_LOWER_BOUND,
        upper_bound=settings.LIST_NUMBERS_UPPER_BOUND,
    )

    # Welcome message
    print_welcome_message(player_name, secret_number=lucky_number)

    # guessing, phase 1
    success, attempts_count, guessed_number = core.player_guess_phase1(
        lucky_list, lucky_number
    )

    # guessing, phase 2
    if not success:
        success, attempts_count = core.player_guess_phase2(
            lucky_list,
            secret_number=lucky_number,
            attempts_count=attempts_count,
            guessed_number=guessed_number,
            list_min_size=settings.MIN_LIST_SIZE,
            range_threshold=settings.RANGE_THRESHOLD,
        )

    # game end
    print_results(success, attempts_count)

    return core.play_again()


def print_welcome_message(player_name: str, secret_number: int) -> None:
    """Display a welcome message and optional debug information.

    Args:
        player_name: The name of the player.
        secret_number: The secret number to be guessed.
    """
    print("")
    util.print_info(f"<<<*= Welcome to the number guessing game, {player_name}! =*>>>")
    if settings.DEBUG:
        util.print_info(f"Psst! The secret number is {secret_number}.")


def print_results(success: bool, attempts_count: int) -> None:
    """Display the final game results to the player.

    Args:
        success: Whether the player found the lucky number.
        attempts_count: Number of attempts made by the player.
    """
    print("")
    attempts_word = "attempt" if attempts_count == 1 else "attempts"
    if success:
        util.print_info(
            f"Congrats, game is over! You found the lucky number in {attempts_count} {attempts_word}."
        )
    else:
        util.print_info(
            f"Game is over. You got to use {attempts_count} {attempts_word}, but did not find the lucky number."
        )


def sanity_check() -> None:
    """Perform sanity checks of game settings.

    Raises:
        Exception: If the numbers range is less than 1 or smaller than the list size.

    This function checks if:
    1. The range of numbers (upper bound - lower bound) is at least 1.
    2. The range of numbers is not smaller than the specified list size.
    """
    numbers_range = (
        settings.LIST_NUMBERS_UPPER_BOUND - settings.LIST_NUMBERS_LOWER_BOUND + 1
    )
    if numbers_range < 1:
        raise Exception(
            f"The numbers range ({settings.LIST_NUMBERS_LOWER_BOUND} -> {settings.LIST_NUMBERS_UPPER_BOUND}) is too small for the game to work!"
        )
    elif numbers_range < settings.LIST_SIZE:
        raise Exception(
            f"The game will not work if numbers range ({numbers_range}) is smaller than the list size ({settings.LIST_SIZE})."
        )
