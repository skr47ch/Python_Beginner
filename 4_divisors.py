number = int(input("Input a number : "))

result = []

for x in range(2, int(number/2)+1):
    if number % x == 0:
        result.append(x)

print(result)
