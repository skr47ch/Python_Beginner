import random

number = random.randint(1000, 9999)

user_input = 0

while user_input != number:
    cow, bull = 0, 0
    user_input = input("Enter a four digit number : ")

    if int(user_input) == number:
        print("4 Cows! You're a dairy farmer!")
        break

    elif len(str(user_input)) != 4:
        print("DO YOU EVEN READ!!")
        break

    for i in range(len(str(number))):
        if user_input[i] == str(number)[i]:
            cow += 1
        elif user_input[i] in str(number):
            bull += 1

    print(str(cow) + " Cows and " + str(bull) + " Bulls")
