#just practice
# import random

# random_digit = random.randint(1,20)
# random_float = random.random() * 5
# print(random_digit)
# print(random_float)

#code challenge
# import random

# random_coin_flip = random.randint(0,1)

# if random_coin_flip == 0:
#     print("Tails")
# else:
#     print("Heads")

#practice stuffs
# states_of_uae = ["Dubai", "Sharjah", "UmmalQuwain", "Fujairah", "RasalKhaima", "Abudhabi", "Ajman"]

# print(f"Habibi come to {states_of_uae[-2]}")
# #appending with 1 item only
# states_of_uae.append("Poznan")
# print(states_of_uae)
# #extending with list
# states_of_uae.extend(["Dhaka", "Warsaw", "Berlin"])
# print(states_of_uae)
# #using insert function with list
# states_of_uae.insert(0, "Lisbon")
# print(states_of_uae)


#code challenge
# name_string = input("Give me everybodys names, separated by a comma: ")
# names = name_string.split(", ")

# import random

# num_items = (len(names))

# random_payment = random.randint(0, num_items)
# person_who_will_pay = names[random_payment]
# print(f"Aaj ka treat {person_who_will_pay} dene wala hai. GANDAY!!")

#code challenge
# row1 = ["🥰", "🥰", "🥰"]
# row2 = ["🥰", "🥰", "🥰"]
# row3 = ["🥰", "🥰", "🥰"]

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position= input("Where do you want to put your treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])

# map [vertical - 1][horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
if my_choice >= 3 or  my_choice < 0:  #This if statement was moved here to catch this condition earlier
    print("You typed an invalid number SUCKERRR")
else:
    print (game_images[my_choice])

    computers_choice = random.randint(0, 2)

    print("Computer chose: ")
    print(game_images[computers_choice])


    if my_choice == 0 and computers_choice == 2:
        print("You win")
    elif computers_choice > my_choice:
        print("You lose")
    elif my_choice == 2 and computers_choice == 0:
        print("You lost lol")
    elif my_choice > computers_choice:
        print("Nice one you won")
    elif computers_choice == my_choice:
        print("Its a tie bruvv!!!")
