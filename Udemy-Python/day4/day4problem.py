import random

#Exercise 1:
# number = random.randint(0,1)
# if number == 1:
#     print("Heads")
# else:
#     print("Tails")

#Exercie 2:
# name_input = input("Give me everybody\'s name, seperated by a comma: ")
# name = name_input.split(", ")
# person = random.choice(name)
# print(f"{person} is going to buy the meal today!")

#Exercise 3:
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \nPlease insert the column, then row with no space: ")
x = int(position[0]) -1
y = int(position[1]) -1
map [y][x] = 'X'
print(f"{row1}\n{row2}\n{row3}")