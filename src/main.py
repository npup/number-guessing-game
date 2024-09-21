from settings import Settings
from game import Game

def main():
    settings = Settings()
    game = Game(settings)
    try:
        game.play()
    except ValueError as e:
         print(f"Error: {e}")


if __name__ == "__main__":
    main()