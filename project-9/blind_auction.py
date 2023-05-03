#code challenge 1 (grading program)
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student]
#     print(score)
#     if score > 90:
#         student_grades[student] = "outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

    

# # 🚨 Don't change the code below 👇
# print(student_grades)

#code challeng 2 (Dictionary in a list)
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     print(new_country)
#     travel_log.append(new_country)


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

from art import logo
import os
clear = lambda: os.system('clear')
clear()
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record): #bidding_record is a dictionary 
  highest_bid = 0
  winner = ""
  for bidder in bidding_record: #remember that bidder will loop though each of the keys in bidding_record
    bid_amount = bidding_record[bidder] #this will save the value for key[bidder] in bid_amount
    if bid_amount  > highest_bid:
      highest_bid = bid_amount
      winner = bidder #setting winner as the key i.e. current bidder  
  print(f"The winner is {winner} with a bid of {highest_bid}")
    

while not bidding_finished:  #this means when bidding is not yet finished i.e. bidding_finished = False
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $")) #added int data here because we dont want the number as string
  bids[name] = price #this will ensure that key and value are from name and price inputs are added to bids dict.
  should_continue = input("Are there any more bids? Type 'yes' or 'no' to continue:")
  if should_continue == 'no':
    bidding_finished = True #if the input for should_continue is yes then the while loop will continue
    find_highest_bidder(bids) #passing bids here that we have been saving in line 86 to keep track of bids
  elif should_continue == 'yes':
    clear()
    



  


