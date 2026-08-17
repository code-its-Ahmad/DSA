# Program to find LCM of two numbers
def computegcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def computeLcm(x, y):
    lcm = (x * y) // computegcd(x, y)
    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1, "and", num2, "is:", computeLcm(num1, num2))
