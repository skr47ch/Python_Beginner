
def prime(num):
    for x in range (2, int(num/2)+1):
        if num % x == 0:
            return "Not Prime"
    else:
        return "Prime"


print(prime(int(input("Enter a number to check if it's prime : "))))
