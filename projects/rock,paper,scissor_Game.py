import random
import sys

print("\t\t\t\t\tWELCOME\n\t\t\t\tRock,Paper,Scissor Game\n")
# choices
choices=["rock","paper","scissor"]

# initial score
player_score=0
computer_score=0

while(1):
    # genrating computer's choice
    computer=random.choice(choices)

    # taking player's choice
    print("choices:",choices,"\t\t\t\tenter 'quit' to exit")
    player=input("enter your choice:")

    # making lower case to player for making no comflit of case letter problem
    player= player.lower()
    print(f"your choice:{player}\ncomputer choice:{computer}")

    # program terminate by entering 'exit'
    if(player=="quit"):
        sys.exit("thanks for playing the game!")
        break
    else:
        # all cases
        if(player==computer):
            print("draw!⚪")
            print(f"Scores:     You:{player_score}    Computer:{computer_score}")
        elif(player=="rock" and computer=="scissor"):
            print("you won!🟢😊")
            player_score+=1
            print(f"Scores:     You:{player_score}    Computer:{computer_score}")

        elif(player=="rock" and computer=="paper"):
            print("computer won!🔴😢")
            computer_score+=1
            print(f"Scores:     You:{player_score}    Computer:{computer_score}")

        elif(player=="paper" and computer=="scissor"):
            print("computer won!🔴😢")
            computer_score+=1
            print(f"Scores:     You:{player_score}    Computer:{computer_score}")

        elif(player=="paper" and computer=="rock"):
            print("you won!🟢😊")
            player_score+=1
            print(f"Scores:     You:{player_score}    Computer:{computer_score}")

        elif(player=="scissor" and computer=="paper"):
            print("you won!🟢😊")
            player_score+=1
            print(f"Scores:     You:{player_score}    Computer:{computer_score}")

        elif(player=="scissor" and computer=="rock"):
            print("computer won!🔴😢")
            computer_score+=1
            print(f"Scores:     You:{player_score}    Computer:{computer_score}")
        else:
            print("invalid choice")


