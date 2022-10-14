from replit import clear
from art import logo
print(logo)

#Calculator
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
#Dictionary

formulas = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculation():
    #Ask for input
    num1 = float(input("What is your first number?: "))
    
    #print out options for input
    for symbol in formulas:
        print(symbol)
    
    continue_calc = True
    while continue_calc:
        formulas_symbol = input("Pick an operation : ")
        next_num = float(input("What is your next number?: "))
        #generate formula
        function = formulas[formulas_symbol]
        answer = function(num1,next_num)
        

        print(f"{num1} {formulas_symbol} {next_num} = {answer}")
        user_choice = input(f"Type y to continue calculating with {answer}. Type n to start a new calculation. Otherwise type exit: ").lower()
        if user_choice == "y":
            num1 = answer
        elif user_choice == "n":
            continue_calc = False
            clear()
            print(logo)
            calculation()
        else:
            continue_calc = False
calculation()

