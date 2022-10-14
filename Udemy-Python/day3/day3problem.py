#Exercise 1:
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#Exercise 2:
# weight = int(input("What is your weight? "))
# height = float(input("What is your height? "))
# bmi_not_int = weight / height ** 2
# bmi = round(bmi_not_int)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}. You are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}. You have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}. You are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}. You are obese.")
# else:
#     print(f"Your BMI is {bmi}. You are clinically obese.")

#Execise 3:
# year = int(input("Which year do yo want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year!")
#         else:
#             print("Not Leap Year!")
#     else:
#         print("Leap Year!")
# else:
#     print("Not Leap Year!")

#Exercise 4:
# print("Welcome to Python Pizza Order Delivery!" )
# size = input("What size of pizza do you want? \nPlease indicate S, M, or L: ").lower()
# add_pep = input("Do you want to add pepperoni on it? \nPlease indicate Y or N: ").lower()
# add_cheese = input("Do you want to add extra cheese? \nPlease indicate Y or N: ").lower()
# total = 0
# if size == "s":
#     total += 15
# elif size == "m":
#     total += 20
# else:
#     total += 25

# if add_pep == "y":
#     if size == "s":
#         total += 2
#     else:
#         total += 3
# else:
#     total += 0

# if add_cheese == "y":
#     total += 1
# else: total+= 0

# print(f"Your total is: {total}")

# coupon = input("Do you have any coupons that you want to use? \nPlease indicate Y or N: ").lower()
# if coupon == "y":
#     discount = int(input("If so, how much is the coupon? \nPlease insert the number without %: ").lower())
#     total *= ((100-discount)/100)
# else:
#     total += 0

# print(f"Thank you for ordering! Your total with discount is: ${total}!")

#Exercise 5:
print("Welcome to the Love Calculator!")
name1 = input("What is the name of the first person? ").lower()
name2 = input("What is the name of the second person? ").lower()
combine_x = name1 + name2
combine = combine_x.lower()
t = combine.count("t")
r = combine.count("r")
u = combine.count("u")
e = combine.count("e")
true = t + r + u + e
l = combine.count("l")
o = combine.count("o")
v = combine.count("v")
e = combine.count("e")
love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}. You two go together like mentos and coke!")
elif 40 <= score <= 50:
    print(f"Your score is {score}. You guys are alright together!")
else:
    print(f"Your score is {score}")