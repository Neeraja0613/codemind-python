t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    it = 10
    d = 100
    dist = x * it
    min_needed = y * 10 - dist
    n = 100 - y
    res = (min_needed + n - 1) // n
    print(res)
