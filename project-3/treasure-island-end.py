#code challenge
# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")


# code challenge if,else,elif
# height = float(input("enter your height in m: "))
# weight = float(input("enter yoru weight in kg: "))

# bmi = round(weight/height ** 2)

# if bmi < 18.5:
#     print("You are underweight")
# elif bmi < 25:
#     print("normal weight")
# elif bmi < 30:
#     print("overweight")
# elif bmi < 35:
#     print("Fucking obese")
# else:
#     print("Dude you need to visit clinic or some shit!!")

#code challenge nested condition
# year = int(input("Which year do you want to check??"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Its definitely a leap year")
#         else:
#             print("No goddamnn")
#     else:
#         print("Leap year")
# else:
#     print("Its not leap year")

# code chllenge multiple same conditions
# print("Welcome to Python Pizza Deliveries")
# size = input("What size pizza do you want? S,M or L ?")
# add_pepperoni = input("Do you want pepperoni? ")
# extra_chese = input("Wanna extra cheese bruv? ")

# bill = 0

# if size == "S":
#     bill +=15       #in example while learning 15 was given already for small pizza 20 for medium and 25 for large
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == 'Y':
#     if size == "S":
#         bill += 2       #the rate 2 for pepperoni was alreadt added in question for small and $3 for nedium and large
#     else:
#         bill += 3

# if extra_chese == 'Y':
#     bill += 1

# print(f"Your final bill is ${bill}")

#code challenge using logical operators like and, or ,not
# print("Welcome to Love Calculator")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_string = name1 + name2
# lower_case_string =  combined_string.lower()

# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true = t + r + u + e

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love))


# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score},you go together like coke and mentios")
# elif (love_score >= 40 and love_score <=50):
#     print(f"Your score is {love_score}, you are alright together")
# else:
#     print(f"Your score is {love_score}")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure!!")

direction_choice = input('Where do you wanna go? "left" or "right"?').lower()

if direction_choice == "left":
    direction_choice2 = input('You have come to a lake. Type "wait" to wait for a boat. Type "swim" to swimm across. ').lower()
    if direction_choice2 == "wait":
        door_choice = input('You arrived at Island unharmed luckily. Now choose door "red", "yellow" or "blue". Which one? ').lower()
        if door_choice == "red":
            print("Its room full of fire/ Game Over")
        elif door_choice == "yellow":
            print("You found the treasure! You Win")
        elif door_choice == "blue":
            print("You fell down mate. GAME OVER")
        else:
            print("You chose the door that doesnt exist")
    else:
        print("You got attached by crocodile. Game Over!!!")
else:
    print("Lol bruv GAME OVER because you fell into a hole")





