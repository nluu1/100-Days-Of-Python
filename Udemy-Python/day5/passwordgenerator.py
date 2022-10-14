letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

print("Welcome to the Pypassword generator!")
x_letter = int(input("How many letters wold you like in your password? \nPlease indicate a number:  "))
x_symbol= int(input("How many symbols would you like in your password? \nPlease indicate a number: "))
x_number = int(input("How many numbers would you like in your password? \nPlease indicate a number: "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for x in range(0, x_letter):
    x = random.choice(letters)
    password += x
for x in range(0,x_symbol):
    x = random.choice(symbols)
    password += x
for x in range(0,x_number):
    x = random.choice(numbers)
    password += x   
print(password)   



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# list_password = list(password)
# random.shuffle(list_password)
# final = ''.join(list_password)
# print(final)

