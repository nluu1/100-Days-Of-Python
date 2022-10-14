import random
from art import logo, vs
from game_data import data
from replit import clear

current_score = 0
account_b = random.choice(data)
should_continue = True

print(logo)

# My functions:
def account_info(account):
    """Format account data into printable format"""
    account_name = account["name"]
    account_follower = account['follower_count']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_follower, b_follower):
    """Use the if statement to see if the user is correct"""
    if a_follower > b_follower:
        return guess == "a"
    else: 
        a_follower < b_follower
        return guess == "b"


while should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b == random.choice(data)
    #Format account data into printable format
    print(f"Compare A: {account_info(account_a)}")
    print(vs)
    print(f"Compare B: {account_info(account_b)}")
    #ask user for a guess
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower() 
    #Check if user is correct
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    clear()
    print(logo)
    is_correct = check_answer(guess, a_follower, b_follower)
    if is_correct:
        current_score += 1
        print(f"That's right!\nCurrent score: {current_score}")
    else:
        should_continue = False
        print(f"Sorry. That's wrong. \nFinal score: {current_score}.")

    