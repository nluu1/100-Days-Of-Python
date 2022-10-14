#Generate interger
user_input_again = True

while user_input_again:
    count = 0
    num_list = []
    for n in range(4):
        while count < 4:
            try:
                num = int(input("Enter a number: "))
                print(" ")
                count += 1
                num_list.append(num)
            except ValueError:
                print(f"\nThe input was not a valid integer. Please enter again. {4 - count} more integers required.\n")
                
    print(f'\nHighest number is: {max(num_list)}\n')
    print(f'Smallest number is: {min(num_list)}\n')
    print(f'The total of these numbers are: {sum(num_list)}\n')

    user_choice = input("Do you want to enter some numbers again? (Y/N): ").lower()
    if user_choice == 'y':
        user_input_again = True
        print(" ")
    elif user_choice == 'n':
        user_input_again = False
        print("\nBye bye!")
    else: 
        print("\nYou entered something I could not understand.")
        input("\nDo you want to enter some numbers again? (Y/N): ").lower()
        print(" ")
     
#Grade point calculator
def grade_calc(point):
  """Function to retun which letter grade the student will receive"""
  if point >= 0.9:
      return 'A'
  elif point >= 0.8:
      return 'B'
  elif point >= 0.7:
      return 'C'
  elif point >= 0.6:
      return 'D'
  else:
      return 'F'

user_continue = True 

while user_continue:
  try:
    point = float(input("Please enter a value between 0.0 and 1.0: "))  
    if point < 0.0 or point > 1.0:
      print("\nThe value you entered is out of range")
    else:
      print(f"\nYour grade is: {grade_calc(point)}")
  except ValueError:
      print("\nYou entered an invalid number.")
  user_choice = input("\nInput another value? (y/n): ").lower()
  print(" ")
  if user_choice == 'y' or user_choice == 'yes':
    user_continue = True
  elif user_choice == 'n' or user_choice == 'no':
    user_continue = False
    print("Bye bye!")
  else:
    print("Please enter y/yes or n/no.")
    input("\nInput another value? (y/n): ").lower()
    print(" ")

