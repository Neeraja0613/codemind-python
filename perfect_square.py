import math

n = int(input("Enter a number: "))

# Calculate the square root
sqrt_n = int(math.sqrt(n))

# Check if the square of the square root equals the number
if sqrt_n * sqrt_n == n:
    print("YES, it's a perfect square")
else:
    print("NO, it's not a perfect square")
