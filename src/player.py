class Player:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.games_played = 0
        self.wins_count = 0


    def register_game_played(self, win: bool) -> None:
        self.games_played += 1
        if win:
            self.wins_count += 1


    def __str__(self) -> str:
        return f"""
       Player : {self.name}, {self.age} years old.
 Games played : {self.games_played}
         Wins : {self.wins_count}
       Losses : {self.games_played - self.wins_count}
"""
