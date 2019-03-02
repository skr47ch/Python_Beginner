# Write a password generator in Python. # Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

import random
password = []

user_input = int(input("Enter password length (4-12 digit): "))

PASSWORD_LENGTH = user_input

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
special_char = "!`@#$%^&*()_+"

password.append(random.choice(lower))
password.append(random.choice(upper))
password.append(random.choice(number))
password.append(random.choice(special_char))

LETTER_COUNT = 4

while LETTER_COUNT < PASSWORD_LENGTH:
    choice = random.randint(0, 3)

    if choice == 0:
        password.append(random.choice(lower))
    elif choice == 1:
        password.append(random.choice(upper))
    elif choice == 2:
        password.append(random.choice(number))
    else:
        password.append(random.choice(special_char))

    LETTER_COUNT += 1


random.shuffle(password)
print("".join(password))
print("Password length : " + str(len(password)))
