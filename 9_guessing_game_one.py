import random

number = random.randint(1, 9)
userInput = input("Guess the selected number (1-9) : ")
guessCount = 1

while userInput != "Exit":
    if number == int(userInput):
        print("That's correct!! It took you " + str(guessCount) + " tries.")
    elif int(userInput) > number:
        if int(userInput) > 9:
            print("Way too big. Select between 1-9")
        else:
            print("Too big. Go smaller")
    else:
        if int(userInput) < 1:
            print("Way too small. Select between 1-9")
        else:
            print("Too small. Go bigger")
    userInput = input("Guess the selected number (1-9) : ")
    guessCount += 1

