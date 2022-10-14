rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
list = [rock, paper, scissors]

end_game = True

while end_game:
    choice = int(input("Type 0 for Rock \nType 1 for Paper \nType 2 for Scissors\nWhat do you choose? "))
    if choice < 0 or choice >= 3:
        print("You chose an invalid number. Please try again!")
        end_game = True
    else:
        print(list[choice])
        print("Computer chose:")
        computer = random.randint(0,2)
        print(list[computer])
            
        if choice == 0 and computer == 2:
            print("You Won!")
        elif choice > computer:
            print("You Won!")
        elif choice < computer:
            print("You Lose!")
        elif choice == computer:
            print("It's a Draw!")
        else:
            print("You Lose!")
        
    answer = input("Do you want to play again?\nType yes to play again. Otherwise type no: ").lower()
    
    if answer == "yes":
        end_game = True
    else:
        end_game = False

print("Thank you for playing.")

