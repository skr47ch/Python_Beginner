inputList = []
resultList = []
elementCount = int(input("How many elements do you wish to enter : "))
for x in range(0, elementCount):
    newElement = input("Input item " + str(x+1) + " : ")
    inputList.append(newElement)

compare = int(input("Enter number tp compare with : "))

for element in inputList:
    if int(element) < compare:
        resultList.append(element)

print(resultList)
