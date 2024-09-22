class Player:
    """Represents a player in the number guessing game.

    This class keeps track of the player's name, age, games played,
    and wins, providing methods to update game statistics and display
    player information.

    Attributes:
        name (str): The player's name.
        age (int): The player's age.
        games_played (int): The number of games played by the player.
        wins_count (int): The number of games won by the player.
    """

    def __init__(self, name: str, age: int):
        """Initialize a new Player instance."""
        self.name = name
        self.age = age
        self.games_played = 0
        self.wins_count = 0


    def register_game_played(self, win: bool) -> None:
        """Record the result of a game played by the player."""
        self.games_played += 1
        if win:
            self.wins_count += 1


    def __str__(self) -> str:
        """Return a string representation of the Player."""
        return f"""
       Player : {self.name}, {self.age} years old.
 Games played : {self.games_played}
         Wins : {self.wins_count}
       Losses : {self.games_played - self.wins_count}
"""
