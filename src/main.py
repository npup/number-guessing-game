from settings import Settings
import util 
from game import Game

def main():
    try:
        settings = Settings()
        game = Game(settings)
        game.play()
    except ValueError as e:
         util.print_fatal(f"Fatal error: {e}")


if __name__ == "__main__":
    main()