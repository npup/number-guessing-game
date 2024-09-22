import random


class NumberList:
    """A class representing a list of unique random numbers within a specified range.

    The numbers will be sorted in ascending order, left to right.
    """

    def __init__(self, size: int, lower_bound: int, upper_bound: int):
        """Initialize the NumberList with random unique integers.

        Args:
            size: The number of integers to generate.
            lower_bound: The lower bound of the range (inclusive).
            upper_bound: The upper bound of the range (inclusive).
        """
        self.numbers: list[int] = sorted(
            random.sample(range(lower_bound, upper_bound + 1), size)
        )

    def contains(self, number: int) -> bool:
        """Check if the given number is in the list.

        Args:
            number: The number to check for.

        Returns:
            True if the number is in the list, False otherwise.
        """
        return number in self.numbers

    def remove(self, number: int) -> None:
        """Remove the given number from the list if it exists.

        Args:
            number: The number to remove.
        """
        if number in self.numbers:
            self.numbers.remove(number)

    def random_choice(self) -> int:
        """
        Select and return a random number from the list.

        Returns:
            A random integer from the list.
        """
        return random.choice(self.numbers)

    def clamp(self, pivot: int, range_threshold: int):
        """Filter the list to keep only numbers within a certain range of the pivot.

        Args:
            pivot: The central value for the range.
            range_threshold: The maximum allowed difference from the pivot.
        """
        self.numbers = [n for n in self.numbers if abs(n - pivot) <= range_threshold]

    def size(self) -> int:
        """Get the current size of the list.

        Returns:
            The number of integers currently in the list.
        """
        return len(self.numbers)

    def __str__(self) -> str:
        """Get a string representation of the list.

        Returns:
            A string representation of the numbers in the list.
        """
        return str(self.numbers)
