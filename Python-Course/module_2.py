#Function 1: Repeatedly accept input numbers until a user enters the word "done"
def sum_avg_max_min():
  user_cont = True
  list = []

  while user_cont:
      try:
          user = input('Enter a number: ')
          if user == 'done':
              #return sum, avg, max, and min 
              print(f"\nThe entered numbers are: {list}\nTotal: {sum(list)}\nAverage: {sum(list)/len(list)}\nMax: {max(list)}\nMin: {min(list)}")
              break
          else:
              user = int(user)
              list.append(user)
      except ValueError:#if user enters anything other than a number, ask them to try again
          print('Invalid number, please try again.')
          
def foo(*arg):
    print (f"The function was provided with {len(arg)} values: {arg}\n")
    total = 0
    stop = False
    for number in arg:#loop through each argument
      if type(number) == str: #if any of the arguments is string, stop the function
        stop = True
        break
      else:
        total+=int(number) #else calculate the total
    if stop:# if total caculation is stopped, there is a str in it
      print("Not all arguments are numbers")#print error
    else:#else print result
      print(f"Total: {total}\nAverage: {round(total/len(arg),2)}\nMax: {max(arg)}\nMin: {min(arg)}")
     
#print * triangles    
def right_triangle():
    for star in range(rows//2):      
        for j in range(star):        
            print("**", end = '')    
        print("\n")

def right_down_triangle():
    for star in range(rows//2):       
        for j in range(star, rows//2):        
            print("**", end = '')        
        print("\n")

def left_pascal_triangle():
    right_triangle()
    right_down_triangle()

rows = int(input("Enter the max number of '*' for the center of the pyramid: "))
left_pascal_triangle()
