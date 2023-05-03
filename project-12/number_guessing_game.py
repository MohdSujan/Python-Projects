#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """
 _______               ___.                                                      .__                                               
 \      \  __ __  _____\_ |__   ___________     ____  __ __   ____   ______ _____|__| ____    ____      _________    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \   / ___\|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\    / ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/  / /_/  >  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >  / /_/  > __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \___  /|____/  \___  >____  >____  >__|___|  /\___  /   \___  (____  /__|_|  /\___  >
        \/            \/    \/     \/        /_____/             \/     \/     \/        \//_____/   /_____/     \/      \/     \/
Welcome to the Number guessing game!
I am thinking of a number between 1 and 100"
"""

print(logo)

import random

easy_attempts_turns = 10
hard_attempts_turns = 5
    
answer = random.choice(range(1, 100)) #computer guess and save it to gloabl variable
print(answer)


def check_answer(guessed_number, answer, turns):     
    """checks answer against guess and returns remaining"""   
    if guessed_number > answer:
        print(f"Too high.")
        return turns - 1 #so that the number of turns reduces
    elif guessed_number < answer:
        print(f"Too low.")
        return turns - 1
    else:
        print(f"You got it.. the answer was {answer}")

    
def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level ==  "easy":
        return easy_attempts_turns #returning the values as an output of this function so we can call this func later and the output will save actual number of turns below
    else:
        return hard_attempts_turns

def game():
    turns = set_difficulty() #call this func here so the output from this func will save actual number of turns and save it to global var i.e. turns
    guessed_number = 0 #setting an empty local var so this is appended later when we input the guess
    while guessed_number != answer: #this while loop is to make sure the game keeps continuing until the attempts are over/guessed the right answer
        print(f"You have {turns} attempts remaining")
        guessed_number = int(input("Make a guess: "))
        turns = check_answer(guessed_number, answer, turns)
        if turns == 0:
            print("You have ran out of guesses you lose")
            return #this return will help the function to exit
game()