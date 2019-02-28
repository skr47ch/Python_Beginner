# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

import random

a = []

for x in range(1, random.randint(10, 25)):
    a.append(random.randint(1, 100))

print(a)
print([a[0], (a[len(a)-1])])

