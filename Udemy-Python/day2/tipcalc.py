#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator!")
total = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_each = (total / people)
with_tip = total_each * (1+tip/100)
final_amount = "{:.2f}".format(with_tip)
print(f"${final_amount}")                              