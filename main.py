import random
from art import logo, vs
from game_data import data

def select_account(list_of_dicts):
    return random.choice(data)


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, from {account_country}."


def check_answer(user_guess, a_followers, b_followers):
    """Takes the user's guess as well as the follower counts and returns if the user got it right."""
    if a_followers > b_followers:
        return user_guess == "a" # if valid, return True
    else:
        return user_guess == "b" # if invalid, return False


print(logo)

score = 0
game_should_continue = True
account_b = select_account(data)


while game_should_continue:
    
    account_a = account_b
    account_b = select_account(data)
    
    if account_a == account_b:
        account_b = select_account(data)
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    print("\n" * 20)
    print(logo)
    
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You're Right! Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_should_continue = False
