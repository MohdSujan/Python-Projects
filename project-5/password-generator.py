# code challenge 1: print average height from list of heights given
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)


# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# number_of_student = 0
# for student in student_heights:
#     number_of_student += 1
# print(number_of_student) 

# average_height = round(total_height/number_of_student)
# print(average_height)

# code challenge 2: print highest score
# student_scores = input("Input a list of student score ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score is {highest_score}")


# code challenge 3: Adding evens using range
# total = 0

# for number in range(2, 101, 2):  #here  3rd digit i.e.2 is the step size means in this range only it will consider every other number giving only even ones.
#     total += number
# print(total)

# code challenge 4: Fizz buzz exercise

# number = input("Enter the fizzbuzz number: ")

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for char in range(1, nr_letters + 1): #the + 1 is adding inside range to take number between 1-5 into consideration and not consider 5 numbers rather 4
#     password += random.choice(letters) #remember += means there is concatenation going on and it will be saved inside as a variable i.e. password = password + random.choice(letters)
    
# for char in range(1, nr_symbols + 1): #lets say my input for nr_symbols will be 2 so not consider symbols between 1-3 digits + 1 was added
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters)) # this and the above method both works fine and does the same think but this append method will not work if the variable we are contatenating is not LIST i.e. password_list = []
    
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols) #keeping it same as above easy method to show that append and old method works with list.

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
random.shuffle(password_list) #using shuffle function to mix up the list

#Now the above print will return us list and below code will turn list to string using concatenation method 1
# password = ""

# for char in password_list:
#     password += char
# print(f"Your password is {password})

#Now the above print will return us list and below code will turn list to string methon 2 using join operator. This I found form Stackoverflow
password = ''.join(password_list)
print(f"Your password is {password}")
