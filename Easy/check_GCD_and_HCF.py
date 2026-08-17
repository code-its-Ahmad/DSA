# Program to Find GCD or HCF of Two Numbers

def find_gcd(x, y):
    """
    This function returns the Greatest Common Divisor (GCD)
    of two numbers x and y using the Euclidean algorithm.
    """
    while(y):
        x, y = y, x % y
    return x

def find_hcf(x, y):
    """
    This function returns the Highest Common Factor (HCF)
    of two numbers x and y using the Euclidean algorithm.
    Note: HCF is the same as GCD.
    """
    while(y):
        x, y = y, x % y
    return x

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD and HCF
GCD = find_gcd(num1, num2)
HCF = find_hcf(num1, num2)

# Display the result
print(f"The GCD of {num1} and {num2} is: {GCD}")
print(f"The HCF of {num1} and {num2} is: {HCF}")