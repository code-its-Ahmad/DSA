# Check if a number is a power of another

def Check_Prower(a,b):
    while b != 1:
        if a % b != 0:
            return False
        a = a // b
        b = b // b
    return True 
print(f"Check the number Power is : {Check_Prower(1,20)}")