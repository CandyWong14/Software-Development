#Import python library
import random

while True:
    #Generate a random value (1, 2) to simulate the coin flip
    answer = random.randint(1, 2)

    #Prompt to enter the user guess
    guess = int(input("Enter your guess as 1 for head, 2 for tail, or 0 to exit: "))

    if guess == 0:
        print("Thank you for playing the game!")
        break
    elif guess == 1 or guess == 2:
        if guess == answer:
            print("You guess is correct!")
        else:
            print("You guess is incorrect!")
    else:
        print("Please enter either 0, 1 or 2. \n")