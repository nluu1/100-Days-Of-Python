def dec_to_hex(quo):
    """This function converts decimal(base 10) to hexadecimal(base 16)"""
    hex = ''
    hex_digits = "0123456789ABCDEF"
    while quo > 0:
        hex += hex_digits[quo % 16]
        quo = quo // 16
    return '0x' + hex[::-1]

def hex_to_dec(hex_num):
    """This function converts hexadecimal(base 16) to decimal(base 10)"""
    hex_strings = {  
        #dictionary to access the values between hex : dec
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15, 
    }
    dec_num = 0
    size = len(hex_num) -1
    for num in hex_num:
        dec_num = dec_num + hex_strings[num] * 16 ** size
        size = size -1
    return dec_num

def dec_to_oct(dec_num):
    """This function converts decimal(base 10) to octal(base 8)"""
    octal_num = 0
    count = 1
    while dec_num > 0:
        remainder = dec_num % 8
        octal_num += remainder * count
        count = count * 10
        dec_num = dec_num // 8
    return octal_num

def oct_to_dec(user_num):
    """This function converts octal(base 8) to decimal (base 10)"""
    temp_num = user_num 
    dec_num = 0
    base = 1
    while temp_num:
        last_digit = temp_num % 10
        temp_num = temp_num // 10
        dec_num += last_digit * base
        base = base * 8
    return dec_num

def dec_to_bin(bin_num):
    """This function converts decimal(base 10) to binary(base 2) using recursion"""
    if bin_num == 0:
        return ''
    else:
        result =  str(dec_to_bin(bin_num // 2)) + str(bin_num % 2)
        return result

def bin_to_dec(user_num):
    """This function converts binary(base 2) to decimal(base 10) using int()"""
    return int(user_num,2)
        
def tryblock(choice):
    """This function checks if the decimal input is valid and within range"""
    try:
        user_num = int(input("\nEnter a decimal number: "))
        while user_num not in range (0,2049):
            print("You entered a number that's out of range.")
            user_num = int(input("\nEnter a decimal number in range (0,2048): "))
        return user_num
    except ValueError as e:
        print(f"\nYou did not enter a valid decimal number.\nError: '{e}'")
        return -1 #some parameters from defined functions are Nonetype, it brings error with int; have to return a number and insert a condition if user_num != -1 

def is_hex(hex_char):
    """This function checks if the input is a valid character within the list for hexadecimal(base 16) """
    hex_digits = "0123456789ABCDEF"
    for char in hex_char:
        if not char in hex_digits:
            return False
    return True
    
def is_octal(octal_num):
    """This function checks if the input is a valid number within the list for octal(base 8) """
    octal_digits = '01234567'
    for char in octal_num:
        if not char in octal_digits:
            return False
    return True

def is_bin(bin_num):
    """This function checks if the input is a valid number within the list for binary(base 2) """
    bin_digits = "01"
    for char in bin_num:
        if not char in bin_digits:
            return False
    return True
    
def conversion(choice):
    """This function performs the conversion based on user's choices from 1 through 6 (with data validation) """
    if choice == 1:
        user_num = tryblock(choice)
        if user_num != -1:
            print(f"\nDecimal(Base 10): {user_num}, Hexadecimal(Base 16): {dec_to_hex(user_num)}")           
    elif choice == 2:
        user_num = input("\nEnter a hexadecimal number (starts with '0x'): ")
        if user_num[:2] == '0x':
            user_num = user_num.replace('0x','')
            if is_hex(user_num.upper()):
                print(f"\nHexadecimal(Base 16): 0x{user_num}, Decimal(Base 10): {hex_to_dec(user_num.upper())}")
            else:
                print("\nYou did not enter a valid hexadecimal number. Please review valid hexadecimal(Base16) numbers.")
        else:
            print("\nYou did not enter a trailing '0x', and/or valid hex strings")
    elif choice == 3:
        user_num = tryblock(choice)
        if user_num != -1:
            print(f"\nDecimal(Base 10): {user_num}, Octal(Base 8): {dec_to_oct(user_num)}")
    elif choice == 4:
        user_num = input("\nEnter an octal number: ")
        if user_num[:1] == '0':
            user_num = user_num.replace('0x','')
            if is_octal(user_num):
                user_num = int(user_num)
                print(f"\nOctal(Base 8): 0{user_num} to Decimal(Base10): {oct_to_dec(user_num)}")
            else:
                print("\nYou did not enter a valid octal number. Please review valid Octal(Base8) numbers.")
        else:
            print("\nYou did not enter a trailing '0' for octal number, and/or valid octal numbers")
    elif choice == 5:
        user_num = tryblock(choice)
        print(f"\nDecimal(Base 10): {user_num}, Binary(Base 2): {dec_to_bin(user_num)}")
    elif choice == 6:
        user_num = input("\nEnter a binary number: ")
        if is_bin(str(user_num)):
            print(f"\nBinary: {user_num} to Decimal(Base10): {bin_to_dec(user_num)}")
        else:
            print("\nYou did not enter a valid binary number. Please review valid Binary(base 2) numbers.")

#-- Start of Number Converter:

print("Number Converter -> convert a number from:\n\nEnter 1 -- Decimal to Hexadecimal\nEnter 2 -- Hexadecimal to Decimal\nEnter 3 -- Decimal to Octal\nEnter 4 -- Octal to Decimal\nEnter 5 -- Decimal to Binary\nEnter 6 -- Binary to Decimal\nEnter X -- Exit\n")
user_cont = True
while user_cont:
    choice = input("Enter your choice: ").lower()
    try:
        if choice == 'x':
            print("\nBye! Exiting the program.")
            break
        elif int(choice) in range (1,7):
            choice = int(choice)
            conversion(choice)
        else:
            print("\nInvalid choice. Please enter 1-6 or X to exit.")
    except ValueError:
        print("\nInvalid choice. Please enter 1-6 or X to exit.")
        
    user_option = input("\nDo you want to continue? (Y/N) ").lower()
    print("")
    if user_option == 'y':
        user_cont = True
    elif user_option == 'n'or user_option =='x':
        print("Bye!")
        user_cont = False
    else:
        print("That's not a valid answer, shutting down anyway.")
        user_cont = False
