t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    slices = 0
    while a != b:
        if a > b:
            eat = (a + 1) // 2
            a -= eat
            slices += eat
        else:
            eat = (b + 1) // 2
            b -= eat
            slices += eat
    print(slices)
