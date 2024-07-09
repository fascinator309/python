import random

choices={
    -1 : "snake",
    0 : "water",
    1 : "gun"
    }

print("choices:",choices)

player=int(input("enter choice:"))

computer=random.choice([-1,0,1])

print("you choosen:",choices.get(player))

print("computer choosen:",choices.get(computer))

#                                ALGORITHM 

#                         L     W     W      L     W     L                           
        # player          -1    0     1      0     -1     1
        # computer         1    1     -1    -1     0      0
#         C-P              2    1     -2     -1    1      -1   

# so here player win on when result is -2 and 1                    

if(computer==player):
    print("draw!⚪")
elif((computer-player)==-2 or (computer-player)==1):
    print("you won!🟢😊")
else:
    print("computer won!🔴😢")

