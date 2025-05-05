t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    for _ in range(y):
        if (x + 1000) > (2 * x):
            x = x + 1000
        else:
            x = x * 2
    print(x)
