from art import logo, vs
import random
from game_data import data
import os

clear = lambda: os.system('clear') #this is useful for restarting the game at the bottom to clear the screen 
print(logo)
score = 0
game_should_continue = True #this is created so that we can make the game repeatable
account_b = random.choice(data)
# Format account data into printable format.
def format_data(account): 
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_description} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """takes the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a" #this means return true
    else:
        return guess == "b"

# Make game repeatable. So that new accounts are repeated when user is correct
while game_should_continue:

    # Generate a random account from the game data.
    # Make account at position B become the next A.
    account_a = account_b #so when the game continues previous account b will become new a
    account_b = random.choice(data)

    while account_a == account_b: #so that the account is no longer equal
        account_b = random.choice(data)

    print(f"Compare A = {format_data(account_a)}")
    print(vs)
    print(f"Against B = {format_data(account_b)}")


    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B: ").lower()

    # Check if user is correct.
    ## Get follower count of each count.

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    #creating a var here with the check_answer function created above 
    is_correct = check_answer(guess, a_follower_count, b_follower_count) 
    ## If Statement to check if user is correct (created function above)

    # give user Feedback on their guess.
    # Clear screen between rounds.
    clear()
    print(logo)
    if is_correct:
        score += 1 ## Score Keeping. so that everytime the user is correct the score is updated
        print(f"You are right!! Current Score: {score}")
    else:
        game_should_continue = False
        print(f"You are wrong. Final Score: {score}")






