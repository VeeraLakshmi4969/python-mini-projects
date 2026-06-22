# Lets play Rock, Paper, Scissor
import random

options = ("rock","paper","scissors")

play = ("True","Yes","y","Y","yes","YES","play")

while True:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors) : ")
    print(f"player choice   : {player}")
    print(f"computer choice : {computer}")
    if player == computer:
        print("It's Tie!")
    elif player == "rock" and computer == "scissors":
        print("You won this game!")
    elif player == "paper" and computer == "rock":
        print("You won this game!")
    elif player == "scissors" and computer == "paper":
        print("You won this game!")
    else:
        print("You lose this match!")


    again = input("Do you want to play again? :")
    if  again not in play:
       break

print("Thanks for playing .")