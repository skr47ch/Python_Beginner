
def fibonacci(count):
    x = 0
    y = 1
    for i in range(count):
        print(x)
        x, y = y, x+y


fibonacci(int(input("Enter the number of sequence items you'd like to see : ")))
