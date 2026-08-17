# Check for Prime Number
def check_Prime_num(n):
    if n <=1:
        return False
    for i in range(2 , int(n / 2)+ 1):
        if n % i == 0:
            return False
    return True
print(f"check the prime number :{check_Prime_num(10)}")