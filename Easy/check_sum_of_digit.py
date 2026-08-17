# Sum of Digits of a Number
def check_sum_digit(n):
    sum_digit = 0
    while n > 0:
        digit = n % 10
        sum_digit += digit
        n //= 10
    return sum_digit
def main():
    n = int(input("Enter a number ="))
    s=check_sum_digit(n)
    print(f"The sum of the {n} is {s}")
    if n % s == 0:
        print(f"{n} is divisible by {s} times")
    else:
        print(f"{n} is not divisible by {s} times")
if __name__=="__main__":
    main()

