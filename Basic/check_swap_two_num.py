# Swap Two Numbers
# Method 1 :
def function_swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = 50
y = 67
swapped_x, swapped_y = function_swap(x, y)
print("Swapped Method 1:", swapped_x, swapped_y)  

# Method 2 :
def function_swap2(x,y):
    x = x + y
    y = x - y
    x = x - y

a = 90
b = 45
swapped_a , swapped_b = function_swap(a,b)
print("Swapped Method 2:",swapped_a,swapped_b)

def function_swap3(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

x = 45 
y = 56

swapped_x , swapped_y = function_swap(x,y)
print("Swapped Method 3:",swapped_x,swapped_y)