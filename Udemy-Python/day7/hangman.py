import random
from replit import clear
from day7.logo import stages
from day7.logo import title
from day7.logo import word_list

def play_game():
    print(title)
    chosen_word = random.choice(word_list)
    display = []
    lives = 6
    end_game = False
    
    for letter in chosen_word:
        display.append('_')

    while not end_game:
        user_guess = input("Guess a letter: ").lower()
        if user_guess in display:
                print(f"You have already guessed letter {user_guess}. Please choose another one.\n")
        for position in range(0,len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_guess:
                display[position] = letter
        print(f"{' '.join(display)}")
        print(stages[lives])
        
        if user_guess not in chosen_word:
            print(f"You guessed {user_guess}. It is not in the word. You lost a life.\n")
            lives -= 1
            if lives == 0:
                end_game = True
                print("You Lose!")
        if '_' not in display:
            end_game = True
            print("You Win!")

    # user_choice = input("\nWould you like to play again?\nType'yes/y' to play again. Type 'no/n' to exit: ").lower()
    # if user_choice == 'y' or user_choice == 'yes':
    #     end_game = False
    # elif user_choice == 'n' or user_choice == 'no':
    #     end_game = True
    #     print("Thank you for playing.\n")


while input("Would you like to play Hangman?\nType 'y' to play. Type 'n' to exit: ").lower() == 'y':
    clear()
    play_game()

print("\nThank you. See you!")

