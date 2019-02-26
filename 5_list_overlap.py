import random

listA = []
listB = []
listC = []

lenA = random.randint(1, 50)
lenB = random.randint(1, 50)

for x in range(1, lenA):
    listA.append(random.randint(1, 100))

for x in range(1, lenB):
    listB.append(random.randint(1, 100))

print(listA)
print(listB)

for element in listA:
    if element in listB:
        if element not in listC:
            listC.append(element)

print(listC)
