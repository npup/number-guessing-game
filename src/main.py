"""Main entry point for the number guessing game.

This module initializes the game settings, creates a game instance,
and handles the main game execution.
"""

from settings import Settings
import util
from game import Game


def main():
    """Initialize and run the number guessing game.

    This function sets up the game environment, creates a Game instance
    with the appropriate settings, and starts the game.
    It catches and handles any ValueError exceptions that might occur
    during the game setup or execution, printing a fatal error message
    if one occurs.
    """

    try:
        settings = Settings()
        game = Game(settings)
        game.play()
    except ValueError as e:
        util.print_fatal(f"Fatal error: {e}")


if __name__ == "__main__":
    main()
