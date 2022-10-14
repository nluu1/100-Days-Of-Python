#-- ASCII Art from ASCII Generator


# Import Sources
print('''
 __          __  _                            _          _   _ _     _ _          
 \ \        / / | |                          | |        | \ | | |   (_| )         
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   |  \| | |__  _|/ ___      
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | . ` | '_ \| | / __|     
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |\  | | | | | \__ \     
   __\/_ \/ \___|_|\___\___/|_| |_| |_|\___|__\__\___/  |_| \_|_| |_|_| |___/     
  / ____|    | |          (_)              / ____|               (_)              
 | |     __ _| |_ ___ _ __ _ _ __   __ _  | (___   ___ _ ____   ___  ___ ___  ___ 
 | |    / _` | __/ _ \ '__| | '_ \ / _` |  \___ \ / _ \ '__\ \ / / |/ __/ _ \/ __|
 | |___| (_| | ||  __/ |  | | | | | (_| |  ____) |  __/ |   \ V /| | (_|  __/\__ \
 
  \_____\__,_|\__\___|_|  |_|_| |_|\__, | |_____/ \___|_|    \_/ |_|\___\___||___/
                                    __/ |                                         
                                   |___/                                          
''')


cost = {'Burger': 20, 'Meat': 10, 'Bun': 6, 'Salad': 3, 'Chips': 12, 'Fries': 11, 'Soda': 6 } # 'food choice': cost of item
pack = {'Burger': 10, 'Meat': 4, 'Bun': 12, 'Salad': 3, 'Chips': 24, 'Fries': 24, 'Soda': 12} # 'food choice': item_per_pack


# Calculate minimum food require
def calculate(food_per_customer, item_per_pack):
    """This function calculates the packages of food needed, with minimum leftovers"""
    total_food = total_guest * food_per_customer
    food_pack = total_food / item_per_pack 
    food_remainder = total_food % item_per_pack
    if food_remainder > 0:
        min_food_required = int(food_pack + 1)
    else:
        min_food_required = int(food_pack)
    return min_food_required

def item_cost(food_item_key,food_per_customer):
    """This function calculates the cost of food quantities and add to out of pocket cost"""
    min_food_require = calculate(food_per_customer, pack[food_item_key])
    food_cost = min_food_require * cost[food_item_key]
    require_food.append(food_item_key)
    require_pack.append(min_food_require)
    return food_cost

user_cont = True
while user_cont:
    require_food = []
    require_pack = []
    out_of_pocket = 0

    occasion = input('\nWhat is the occasion for the catering? ')

    print("\nHere are the list of food choices that we have for this week!"
      "\n-- Burger \U0001F354"
      "\n-- Chicken Sandwich"
      "\n-- Mixed Green Salad")

    while True:
        total_guest = input('\nEnter the number of attending guests: ')
        try:
            if int(total_guest) >0:
                total_guest = int(total_guest)
            else:
                print('Please enter a valid guest number: ')
                continue
        except ValueError:
            print('Error: Please enter number only')
            continue
        else:
            break

    #Burger options
    burger_op = input('\nDo you want to serve burgers? (Y/N) ').lower()
    if burger_op == 'y':
        try:
            burger_per_customer = int(input('How many burger per guest? ').lower())
            out_of_pocket += item_cost('Burger',burger_per_customer)
        except ValueError:
            print('Invalid input. Not adding item')
    else:
        print('Not adding item.')

    #Sandwich options
    sandwich_op = input('\nDo you want to serve chicken sandwiches? (Y/N)  ').lower()
    if sandwich_op.startwith('y').lower(): #check if it works
        try:
            sandwich_per_customer = int(input('How many chicken sandwiches per guest? ').lower())
            sandwich_cost = item_cost('Meat',sandwich_per_customer) + item_cost('Bun',sandwich_per_customer)
            out_of_pocket += sandwich_cost
        except ValueError:
            print('Invalid input. Not adding item')
    else:
        print('Not adding item.')

	#Salad options
    salad_op = input('\nDo you want to serve salad? (Y/N) ').lower()
    if salad_op == 'y':
        try:
            salad_per_customer = int(input('How many salad per guest? ').lower())
            out_of_pocket += item_cost('Salad',salad_per_customer)
        except ValueError:
            print('Invalid input. Not adding item')
    else:
        print('Not adding item.')

    #Add-on options
    addon = input('\nDo you want to choose some add-ons? (Y/N) ').lower()
    if addon == 'y':
        
        #Chips
        chips_op = input('\nDo you want to provide some chips? (Y/N) ').lower()
        if chips_op == 'y':
            try:
                chips_per_customer = int(input('How many chips for each guest? '))
                out_of_pocket += item_cost('Chips',chips_per_customer)
            except ValueError:
                print('Invalid input. Not adding item')
        else:
            print('Not adding item.')

        #Fries
        fries_op = input('\nDo you want to add Fries? (Y/N) ').lower()
        if fries_op == 'y':
            try:
                fries_per_customer = int(input('How many Fries each guest? '))
                out_of_pocket += item_cost('Fries',fries_per_customer)
            except ValueError:
                print('Invalid input. Not adding item.')
        else:
            print('Not adding item.')

        #Drinks    
        drink_op = input('\nDo you want any Soda? (Y/N) ').lower()
        if drink_op == 'y':
            try:
                drink_per_customer = int(input('How many Soda for each guest? '))
                out_of_pocket += item_cost('Soda',drink_per_customer)
            except ValueError:
                print('Invalid input. Not adding item')
        else:
            print('Not adding item.')
    else:
        print('Alright! No add on!')

    while True:  #Loop to make sure user enter valid hours with minimum 4
        try:
            hour = int(input('\nHow many hour (min 4 hours) for the event? '))
            if hour >= 4:
                break
        except:    
            pass
        print ('\nMinimum of 4, please try again: ')

    #Listing of food required and sub-total cost for the event
    print(f"\nHere is the list of food items require for the {occasion}\n")
    for x in range(len(require_food)):
        print(f"-- {require_pack[x]} pack(s) of {require_food[x]}")

    print(f"\n---------------\nOut of pocket cost: ${round(out_of_pocket,2)}\n")

    catering_cost = (out_of_pocket * 1.25) + (hour * 25)
    print(f"\n---------------\nCatering cost (sub-total): ${round(catering_cost,2)}\n")

    # Asking user for coupon
    coupon = input('Do you have any coupon code? (Y/N) ').lower()  
    discount = 0
    if coupon == 'y':
        coupon_code = input('Please enter your coupon code: ').lower()
        if coupon_code == '362food':
            discount = catering_cost * 0.1
            print(f"\nGreat! Here's your 10% off coupon!\nYou saved ${round(discount,2)}!") # format .50 
        else:
            print("\nSorry, that's not a valid coupon.")
    else:
        print('No coupon applied.')

    #Total final catering cost
    print(f"\n---------------\n Total catering cost for the {occasion}: ${round(catering_cost-discount,2)}\n---------------\n")

    #Let user do as many estimation as they wish if they choose 'y'
    user_option = input("\nDo you want to do another estimate? (Y/N) ").lower()
    if user_option == 'y':
        print("\nAlright! Let's do another estimate!")
        user_cont = True
    elif user_option == 'n':
        print("\nBye! Thank you for using our catering estimator!")
        user_cont = False
    else:
        print("\nThat's not a valid answer.\nThank you for using our catering estimator!")
        user_cont = False
