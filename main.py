# ✓ Import required modules: art, random and game data
import random
from art import logo, vs
from game_data import data

# print(logo)

# ✓ Randomly select an account from the game data.
def select_account(list_of_dicts):
    return random.choice(data)

account_a = select_account(data)
account_b = select_account(data)

if account_a == account_b:
    select_account(data)

# ✓ Format the account data into a printable format.
def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, from {account_country}."

print(f"Compare A: {format_data(account_a)}")
# print(vs)
print(f"Against B: {format_data(account_b)}")



# TODO 4: Ask user for guess and assign to choices 'A' or 'B'.

# TODO 5: Check if user is correct.
#   1. Get follower count of each account
#   2. Use if statement to check if user is correct.
#   3. Give user feedback on their guess. End game if user is right, otherwise continue game.
#   4. Score Keeping.
#   5. Make the game repeatable.
#   6. Reassign account in position 'B' to position 'A'.
