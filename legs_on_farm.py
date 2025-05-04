t = int(input())
for _ in range(t):
    n = int(input())
    x = n // 4
    y = (n - (x * 4)) // 2
    z = x + y
    print(z)
