t = int(input())
for _ in range(t):
    x = int(input())
    r = x % 10
    if r == 0:
        print(100 - ((x // 10) * 10))
    else:
        print(100 - (((x // 10) + 1) * 10))
