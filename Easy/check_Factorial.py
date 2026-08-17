def check_Factorial(n):
    if n == 0:
        return 1
    else:
        return n * check_Factorial(n -1)
print(f"Factorial Number : {check_Factorial(5)}")