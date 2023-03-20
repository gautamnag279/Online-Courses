import random
#The Input Code
print("What is your name")
name = input()
print("Welcome" , name  , ", I am thinking of a number between 1 and 20")

#The Game Code
secretNumber = random.randint(1,20)
for guessTaken in range(1,7):
    print("Take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is to low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break

if guess == secretNumber:
    print("Correct! I was thinking of" , secretNumber)
else:
    print("Nope! I was thinking of" , secretNumber)
