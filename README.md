# 14 Higher Lower Game

## Overivew

A fun CLI-based game where you compare two Instagram accounts and guess which one has more followers. This project was completed as part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.


## Table of Contents
1. [About the Game](#about-the-game)
2. [Features](#features)
3. [How to Play](#how-to-play)
4. [Code Walkthrough](#code-walkthrough)
    - [Modules and Imports](#modules-and-imports)
    - [Core Functions](#core-functions)
    - [Game Logic](#game-logic)
5. [How to Run](#how-to-run)


## About the Game

The **Higher Lower Game** challenges you to determine which of two Instagram accounts has more followers. You continue guessing until you get one wrong, and your score is displayed at the end.


## Features

- **Randomized Account Selection**: Dynamically chooses two different accounts to compare.
- **Formatted Display**: Neatly displays account details such as name, description, and country.
- **Interactive Gameplay**: Prompts the user to guess and gives immediate feedback.
- **Score Tracking**: Keeps track of your streak until you make a wrong guess.
- **Replayable**: Play as many times as you like by rerunning the script.


## How to Play

1. The game presents two Instagram accounts.
2. You choose which account has more followers by typing `A` or `B`.
3. If you guess correctly, your score increases, and you move to the next round.
4. If you guess incorrectly, the game ends, and your final score is displayed.


## Code Walkthrough

### Modules and Imports

- `random`: Used to randomly select accounts from the dataset.
- `art.py`: Contains ASCII art for the game's logo and "vs" separator.
- `game_data.py`: Includes a list of dictionaries, each representing an Instagram account with its details.

### Core Functions

#### `select_account(list_of_dicts)`
Randomly selects an account from the `data` list:
```python
def select_account(list_of_dicts):
    return random.choice(data)
```

#### `format_data(account)`
Formats the account's details into a user-friendly string:
```python
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, from {account_country}."
```

#### `check_answer(user_guess, a_followers, b_followers)`
Validates the user's guess:
```python
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
```

### Game Logic

1. **Setup**: The game initializes with `score = 0` and `game_should_continue = True`.
2. **Account Selection**:
   - `account_a` and `account_b` are chosen randomly.
   - Ensures `account_b` is different from `account_a`.
3. **Display Accounts**:
   - Accounts are displayed using the `format_data()` function.
   - The `vs` separator from `art.py` is shown.
4. **User Guess**:
   - The player inputs their guess (`A` or `B`), converted to lowercase.
   - Clears the screen and displays the logo again.
5. **Answer Check**:
   - `check_answer()` verifies the guess.
   - If correct, `score` increases, and the game continues.
   - If incorrect, the final score is displayed, and the game ends.


## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/coderbri/14_higher_lower_game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 14_higher_lower_game
   ```
3. Run the script:
   ```bash
   python main.py
   ```

---
<section align="center">
  <code>coderBri © 2024</code>
</section>
