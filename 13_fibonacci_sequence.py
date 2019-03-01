# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate


def fibonacci(count):
    x = 0
    y = 1
    for i in range(count):
        print(x)
        x, y = y, x+y


fibonacci(int(input("Enter the number of sequence items you'd like to see : ")))
