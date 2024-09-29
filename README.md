# Number Guessing Game

A simple, interactive number guessing game implemented in Python.

There are two branches:

1. `master` - contains version A of the game (procedural programming)
2. `game-b` - containes version B of the game (object oriented programming)

## Description

This project is a command-line implementation of a number guessing game. The game generates a list of random numbers and asks the player to guess a secret number from this list.

## Features

-   Age verification for players
-   Two-phase guessing system
-   Dynamic list shrinking based on player guesses
-   Configurable game settings
-   Colored console output for better user experience

## Installation

1. Ensure you have Python 3.7 or higher installed on your system.
2. Clone this repository:
    ```bash
    git clone https://github.com/npup/number-guessing-game.git
    ```
3. Navigate to the project directory:
    ```bash
    cd number-guessing-game
    ```
4. Create a virtual env and install the requirements:
    ```bash
    python -m venv venv
    source venv/bin/activate # linux/mac
    # .\venv\Scripts\activate # Windows
    pip install -r requirements.txt
    ```

## Version selection

Select version of the game by checking out branch `master` for "game A" and branch `game-b` for "game B".

```bash
git checkout master
git checkout game-b
```

## Usage

Run the game using Python:

```bash
    python src/main.py
```
