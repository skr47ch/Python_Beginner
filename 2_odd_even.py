number = int(input("Please input a number : "))

if number % 4 == 0:
    print("The number is even and a multiple of 4")
elif number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


divisor = int(input("Input another smaller number : "))

if number % divisor == 0:
    print("The number " + str(number) + " is divisible by " + str(divisor))
else:
    print("The number " + str(number) + " is not divisible by " + str(divisor))
