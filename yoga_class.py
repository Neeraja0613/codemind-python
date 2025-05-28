t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    if y > 2 * x:
        r = (n // 2) * y + (n % 2) * x
    else:
        r = n * x
    print(r)
