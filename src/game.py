from datetime import datetime

import regex

from settings import Settings
from player import Player
from number_list import NumberList
import util


class InvalidInputError(Exception):
    """Exception raised for invalid user input.

    This exception is used when the user provides input that doesn't meet
    the required criteria or format in various input functions.
    """

    pass


class Game:
    """Manages the main game logic for the number guessing game."""

    def __init__(self, settings: Settings):
        """Initialize a new game instance.

        Args:
            settings: Configuration settings for the game.
        """

        self.settings: Settings = settings
        self.player: Player = None
        self.number_list: NumberList = None
        self.secret_number: int = None
        self.attempts_count: int = 0
        self.recent_guess: int = None

    def create_player(self):
        """Set up a new player for the game."""
        player_name = self.get_player_name()
        player_age = self.get_player_age()
        self.player = Player(player_name, player_age)

    def play(self):
        """Start and manage the main game loop."""
        util.print_info("The number guessing game starts...")
        self.create_player()
        while self.game_loop():
            util.print_info("Another round of the guessing game coming up...")
        util.print_info(f"Goodbye, {self.player.name}!")
        print(self.player)

    def game_loop(self) -> bool:
        """Run a single round of the game.

        Returns:
            bool: True if the player wants to play again, False otherwise.
        """

        self.create_list()
        print("")
        util.print_info(
            f"<<<*= Welcome to the number guessing game, {self.player.name}! =*>>>"
        )
        if self.settings.DEBUG:
            util.print_info(f"Psst! The secret number is {self.secret_number}.")

        won = self.game_phase1()

        # if not won, guessing, phase 2
        if not won:
            won = self.game_phase2()

        # game end
        self.player.register_game_played(won)
        self.print_results(won)

        return self.play_again()

    def play_again(self) -> bool:
        """Ask the player if they want to play another round.

        Returns:
            bool: True if the player wants to play again, False otherwise.
        """

        return util.prompt_input_boolean("Would you like to play again?")

    def game_phase2(self) -> bool:
        """Run the second phase of the game.

        The list is clamped before each round.

        Returns:
            bool: True if the player guessed correctly, False otherwise.
        """

        self.number_list.clamp(self.secret_number, self.settings.RANGE_THRESHOLD)

        while True:
            self.number_list.remove(self.recent_guess)

            if self.number_list.size() < self.settings.MIN_LIST_SIZE:
                util.print_warning(
                    f"The list is now too short for game to continue: {self.number_list}"
                )
                return False

            self.attempts_count += 1
            self.print_list(
                f"This is attempt #{self.attempts_count}. The new list is",
                self.number_list,
            )

            guess = util.prompt_input_int("Enter your guess for the lucky number")
            if guess == self.secret_number:
                util.print_ok("Correct!")
                return True
            if not self.number_list.contains(guess):
                util.print_error(f"Wrong. {guess} is not even in the list.")
            else:
                util.print_error("Wrong.")
                self.number_list.remove(guess)

    def print_results(self, success: bool) -> None:
        """Display the final game results to the player.

        Args:
            success: Whether the player found the lucky number.
        """

        print("")
        attempts_word = "attempt" if self.attempts_count == 1 else "attempts"
        if success:
            util.print_info(
                f"Congrats, game is over! You found the lucky number in {self.attempts_count} {attempts_word}."
            )
        else:
            util.print_info(
                f"Game is over. You got to use {self.attempts_count} {attempts_word}, but did not find the lucky number."
            )

    def create_list(self) -> None:
        """Initialize the number list and select a secret number."""
        # create list of numbers to guess from
        self.number_list = NumberList(
            self.settings.LIST_SIZE,
            self.settings.LIST_NUMBERS_LOWER_BOUND,
            self.settings.LIST_NUMBERS_UPPER_BOUND,
        )
        # select one the numbers as the "lucky number"
        self.secret_number = self.number_list.random_choice()

    def game_phase1(self) -> bool:
        """Run the first phase of the game with the initial guess.

        Returns:
            bool: True if the player guessed correctly, False otherwise.
        """

        self.print_list("Here is the lucky list", self.number_list)
        print()

        self.recent_guess = util.prompt_input_int(
            "Enter your guess for the lucky number"
        )
        self.attempts_count = 1

        if self.recent_guess == self.secret_number:
            util.print_ok("Correct!")
            return True

        if not self.number_list.contains(self.recent_guess):
            util.print_error(f"Wrong. {self.recent_guess} is not even in the list.")
        else:
            util.print_error("Wrong.")

        return False

    def print_list(self, message: str, numbers: list[int]) -> None:
        """Print a message followed by a list of numbers.

        Args:
            message: The message to print before the list.
            numbers: The list of numbers to print.
        """

        print(f"\n{message}:\n{numbers}")

    def get_player_name(self) -> str:
        """Prompt for and validate the player's name.

        Returns:
            str: The validated player name.

        Raises:
            InvalidInputError: If the input doesn't meet the name criteria.
        """

        while True:
            try:
                name = util.prompt_input("Full name (first, last)")
                if not regex.match(r"^\p{L}+[\s\t]\p{L}+$", name, regex.UNICODE):
                    raise InvalidInputError(
                        "Enter a first- and a lastname, separated by exactly one (1) white space character."
                    )
                names = name.split()
                first_name, last_name = names
                if not all(name.isalpha() for name in names):
                    raise InvalidInputError("The names shall only contain letters.")
                break
            except InvalidInputError as e:
                util.print_error(str(e))
        return f"{first_name} {last_name}"

    def get_player_age(self) -> int:
        """Prompt for and validate the player's age based on birth date.

        Returns:
            int: The calculated age of the player.

        Raises:
            ValueError: If the input date is invalid or doesn't meet age criteria.
        """

        while True:
            now = datetime.now()
            try:
                birth_date_str = util.prompt_input("Enter your birth date [yyyyMMdd]")
                birth_date = datetime.strptime(birth_date_str, "%Y%m%d")
                player_age = now.year - birth_date.year
                if now < birth_date.replace(year=now.year):
                    player_age -= 1

                if now < birth_date or birth_date.year <= self.settings.MINIMUM_YEAR:
                    util.print_error(
                        f"The year must be in the past (but after {self.settings.MINIMUM_YEAR}) to be believable!"
                    )
                elif player_age < self.settings.MINIMUM_AGE_YEARS:
                    util.print_error(
                        f"Age limit is {self.settings.MINIMUM_AGE_YEARS} years."
                    )
                else:
                    return player_age
            except ValueError:
                util.print_error("Invalid date - use the format yyyyMMdd!")
