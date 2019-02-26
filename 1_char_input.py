import datetime

name = input("Please enter your name : ")
age = int(input("Please enter your age : "))

time = datetime.datetime.now()
centennial_year = time.year + 100 - age

# main solution
result = name + ", your age is " + str(age) + " and you will turn 100 in the year " + str(centennial_year)
print(result)

# extra - 1
repeat = int(input("Input another number between 1 to 50 : "))
if repeat < 1 or repeat > 50:
    print("Invalid number")
else:
    for x in range(0, repeat):
        print(result)

