# Closest to n and Divisible by m
# Given two integers n and m (m != 0). 

def closest_number(n, m):
    # find the quotient
    closest = 0
    min_difference = float('inf')

    # Check numbers around n
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n - i)

            if difference < min_difference or \
            			(difference == min_difference and abs(i) > abs(closest)):
                closest = i
                min_difference = difference
    return closest

  
if __name__ == "__main__":
  n = 78
  m = 90
  print(closest_number(n, m))
