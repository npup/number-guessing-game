import random

class NumberList:
    
    def __init__(self, size: int, lower_bound: int, upper_bound: int):
        self.numbers: list[int] = sorted(random.sample(range(lower_bound, upper_bound + 1), size))

    def contains(self, number: int) -> bool:
        return number in self.numbers
        
    def remove(self, number: int) -> None:
        if number in self.numbers:
            self.numbers.remove(number)
        
    def random_choice(self) -> int:
        return random.choice(self.numbers)

    def clamp(self, pivot: int, range_threshold: int):
        self.numbers = [n for n in self.numbers if abs(n - pivot) <= range_threshold]

    def size(self) -> int:
        return len(self.numbers)

    def __str__(self) -> str:
        return str(self.numbers)
