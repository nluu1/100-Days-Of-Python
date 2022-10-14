print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

choice1 = input("You're at a crossroad. Where do you want to go? Type left or right. " ).lower()
if choice1 == "left":  
    choice2 = input('You\'ve come to a lake, there is an island in the middle of the lake. \nType "wait" to wait for a boat. \nType "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. \nOne red, one yellow, and one blue. Which color do you choose? ").lower()
        if choice3 == "red":
            print("You entered a room full of fire! \nGame Over!")
        elif choice3 == "yellow":
            print("You entered a room with the treasure chest! \nYou win!")
        elif choice3 == "blue":
            print("You entered a room full of beasts!\nGame Over!")
        else:
            print("You chose a door that doesn't exist.\nGame Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")