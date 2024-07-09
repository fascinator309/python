from random import randint

computer = randint(1, 100)

print("The Perfect Guess game started......\nGuess the no. from 1 to 100")

count = 1
player = 0

while (player != computer):
    player = int(input("Enter your guess:"))

    if player > computer:
        print("Lower no. please!!")
        count += 1

    elif player < computer:
        print("higher no. please!!")
        count += 1

else:
    print(f"Congratulations!! You Guessed right in {count} chance")
