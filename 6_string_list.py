inputString = str(input("Please enter a string : "))
reverse = inputString[::-1]

print(reverse)
if inputString == reverse:
    print("Palindrome")
else:
    print("Not palindrome")
