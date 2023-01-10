#data cleaning for the 2 text files
with open("/content/BoyNames.txt", "r") as f:
  boynames = [line.rstrip() for line in f]

with open("/content/GirlNames.txt", "r") as f2:
  girlnames = [line.rstrip() for line in f2]  
  
allnames =  boynames + [i for i in girlnames if i not in boynames]
#Function find_match() find exact name in boynames list or girlnames list or both using list comprehension
#Parameter 1: name -> the exact name to be searched
#Parameter 2: gender -> gender option 'boy', 'girl', or 'all'

def find_match(name, gender):
    """Function finds name in the master list of boynames or girlnames or both and return the gender of the name entered by user"""
  #Boolean check to see the exact name is in which list
    isInBoyList = False
    isInGirlList = False
    isInAllList = False
    result_boy_name = []
    result_girl_name = []
    result_all_name = [] 
 
  # result_all_name = [for all element 's' in both list, if exact name = 's', then s is added to the result_all_name ] 
    result_all_name = [s for s in (boynames+girlnames) if name == s]
    if len(result_all_name) > 1:
        isInAllList = True

  # result_boy_name = [for all element 's' in boynames list, if exact name = 's', then s is added to the result_boy_name ] 
    result_boy_name = [s for s in boynames if name == s]
    if len(result_boy_name) > 0:
        isInBoyList = True

  # result_girl_name = [for all element 's' in girlnames list, if exact name = 's', then s is added to the result_girl_name ] 
    result_girl_name = [s for s in girlnames if name == s]
    if len(result_girl_name) > 0:
        isInGirlList = True

    if gender == "boy":
        if isInBoyList == True:
            print(f'We found {name} in our list')
            print(f'\n{name} is in the list of boy names')
            if isInAllList == True:
                print(f'But hey! {name} is actually both boy and girl names')
        else:
            if isInGirlList == True:
                print(f'\n{name} is not a boy name')
                print(f'\nBut, {name} is in the list of girl names')
            else:
                print(f'\n{name} is not in the list of boy names')
                print('\nSee some suggestion:')
                find_close_match(name,boynames)

    elif gender == "girl":
        if isInGirlList == True:
            print(f'We found {name} in our list')
            print(f'\n{name} is in the list of girl names')
            if isInAllList == True:
                print(f'But hey! {name} is actually both boy and girl names')
        else:
            if isInBoyList == True:
                print(f'\n{name} is not in the list of girl names')
                print(f'\nBut, {name} is in the list of boy names')
            else:
                print(f'\n{name} is not in the list')
                print('\nSee some suggestion:')
                find_close_match(name,girlnames)
    else:
        if isInAllList == True:
            print(f'We found {name} in our list')
            print(f'\n{name} is in the list of both boy and girl names')
        else:
            if isInBoyList == True:
                print(f'\n{name} is in the list of boy names')
            elif isInGirlList == True:
                print(f'\n{name} is in the list of girl names')
            else:
                print(f'\n{name} is not in the list')
                print('\nSee some suggestion:')
                find_close_match(name,allnames)

def find_close_match(name,genderlist):
    """This function returns the closest match to letter(s) entered by the user"""
    similar_name = difflib.get_close_matches(name,genderlist,n=5,cutoff = 0.3)
    if similar_name == []:
        result = [s for s in genderlist if s.startswith(name)]
        print(*result, sep='\n')
    else:
        print(*similar_name, sep = '\n')
        
        
#-- Import module:
import difflib

#-- Start of program
user_cont = True
while user_cont:
    search_option = input('Do you want to search by Gender or by Name? ').lower()
    if search_option.startswith('g'):
        print("Proceed with option: Gender\n")
        while True:
            gender_option = input("Please enter gender (boy/girl/all): ").lower()
            if gender_option.startswith('b'):
                gender_option = 'boy'
            elif gender_option.startswith('g'):
                gender_option = 'girl'
            elif gender_option.startswith('a'):
                gender_option = 'all'
            else:
                print('Please enter a valid gender option.')
                continue
            break
        print(f'Searching in {gender_option} list\n')
        name_to_search =  input("Enter the name you want to search: ").title()
        while True:
            if name_to_search.isdigit():
                print('Invalid Input! Enter valid letter(s)')
                continue
            else:
                break
        find_match(name_to_search, gender_option)
    elif search_option.startswith('n'):
        print("Proceed with option: Name\n")
        name_input = input('Enter the name you want to search: ').title()
        while True:
            if name_input.isdigit():
                print('Invalid Input! Enter valid letter(s)')
                continue
            else:
                break
        find_match(name_input, allnames)
    else:
        print("Please enter a valid search mode, either 'gender' or 'name'.")
        continue

    user_option = input("\nDo you want to do another search? (Y/N) ").lower()
    if user_option.startswith('y'):
        if user_option == 'y':
            print('Continuing!\n')
            pass
        else:
            print("You probably entered 'Yes'.Continuing!\n")
        user_cont = True
    elif user_option.startswith('n'):
        if user_option == 'n':
            print('Bye!\n')
            pass
        else:
            print("You probably entered 'No'.Exiting!\n")
        user_cont = False
    else:
        print("That's not a valid answer, shutting down anyway.")
        user_cont = False
