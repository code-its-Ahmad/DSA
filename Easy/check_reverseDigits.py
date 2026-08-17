# Reverse Digits of a Number
def ReverseDigit(num):
    rev_num = 0
    while ( num > 0):
        rev_num = rev_num * 10 + num % 10
        num = int(num / 10)
    return rev_num
print(ReverseDigit(4562))