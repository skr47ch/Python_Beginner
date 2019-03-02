# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.


def string_reverse(string):
    return " ".join(string.split()[::-1])


print(string_reverse(str(input("Enter a string : "))))
