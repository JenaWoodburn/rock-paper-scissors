import sys
import random
from enum import Enum

class RPS(Enum):
    #define constants
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# while loop for continuous play
play_again = True

while play_again:

    #get player choice
    player = int(input("Enter...\n1 for Rock\n2 for Paper, or\n3 for Scissors\n\n"))

    #player can only choose from 1, 2 or 3 - if not, exit
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3")

    #get computer choice
    computer = int(random.choice("123"))

    #display player and computer choice
    print("You chose " + str(RPS(player)).replace('RPS.', '').title())
    print("Computer chose " + str(RPS(computer)).replace('RPS.', '').title())
    print("")

    #logic for determining winner
    if player == 1 and computer == 3:
        print("You win 🎉")
    elif player == 2 and computer == 1:
        print("You win 🎉")
    elif player == 3 and computer == 2:
        print("You win 🎉")
    elif player == computer:
        print("It's a tie")
    else:
        print("Computer wins") 
    print("")

    #ask player to play again or quit
    play_again = input("Play again?\nY for Yes or \nQ to Quit \n\n")

    if play_again.lower() == 'y':
        continue
    else:
        print("Thanks for playing!")
        play_again = False

sys.exit()

