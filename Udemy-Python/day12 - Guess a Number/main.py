from random import randint
from logo import title
from replit import clear
EASY_LEVEL = 10
HARD_LEVEL = 5


def difficulty():
    user_option = input("First, please choose a difficulty.\nType 'Easy' or 'Hard'? ").lower()
    if user_option == 'easy':
        return EASY_LEVEL
    if user_option == 'hard':
        return HARD_LEVEL
        

def check_answer(user_choice,correct_num,attempts):
    if user_choice < correct_num:
        print("Too low.")
        return attempts -1
    elif user_choice > correct_num:
        print("Too high.")
        return attempts -1
    elif user_choice == correct_num:
        print(f"You got it! The answer was {correct_num}") 
        return


def game():
    print(title)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 to 100. Guess the number!\n")
    correct_num = randint(1,100)
    print(f"Pss, the correct number is {correct_num}\n")
    user_choice = 0
    attempts = difficulty()
    while user_choice != correct_num:
        print(f"You have {attempts} remaining attempts to guess a number.")
        user_choice = int(input("Make a guess: "))
        attempts = check_answer(user_choice,correct_num,attempts)
        if attempts == 0:
            print("You have run out of guesses. You Lose.")
            return
        elif user_choice != correct_num:
            print("Guess again.")
            

game()
while input("Would you like to play again?\nType 'y' to play. Type 'n' to exit: ") == 'y':
    clear()
    game()
print("Thank you. See you!")