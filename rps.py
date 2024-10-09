import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    #variables to track game statistics
    game_count = 0
    computer_wins = 0
    ties = 0

    def play_rps():
        nonlocal name
        nonlocal game_count
        nonlocal computer_wins
        nonlocal ties

        class RPS(Enum):
            #define constants
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        #get player choice
        while True:
            player = input(f"\n{name}, enter:\n1 for Rock\n2 for Paper, or\n3 for Scissors\n\n")
            #player can only choose from 1, 2 or 3 - if not, ask again
            if player not in ["1", "2", "3"]:
                print("\nYou must enter 1, 2 or 3")
                continue
            else:
                player = int(player)
                break

        #get computer choice
        computer = int(random.choice("123"))

        #display player and computer choice
        print("You chose " + str(RPS(player)).replace('RPS.', '').title())
        print("Computer chose " + str(RPS(computer)).replace('RPS.', '').title())
        print("")

        #logic for determining winner
        #tracks number of times computer wins or game is tied
        def decide_winner(player, computer):
            if player == 1 and computer == 3:
                return(f"{name}, you win 🎉")
            elif player == 2 and computer == 1:
                return(f"{name}, you win 🎉")
            elif player == 3 and computer == 2:
                return(f"{name}, you win 🎉")
            elif player == computer:
                nonlocal ties
                ties += 1
                return("It's a tie 👔")
            else:
                nonlocal computer_wins
                computer_wins += 1
                return(f"Computer wins. Sorry, {name} 😪") 
            
        #play game and print results
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count:  {game_count}")
        print(f"{name}'s wins: {game_count - computer_wins - ties}")
        print(f"Computer wins: {computer_wins}")
        print(f"Ties: {ties}")

        #ask player to play again or quit
        while True:
            play_again = input(f"\n{name}, do you want to play again?\nY for Yes or \nQ to Quit \n\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == 'y':
                return play_rps()
        else:
                print(f"Thanks for playing, {name}!")
                sys.exit()
    return play_rps

rock_paper_scissors = rps()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalised game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()