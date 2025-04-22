t = int(input())
for _ in range(t):
    a, b, c, m = map(int, input().split())
    flag = False
    for x in range(m + 1):
        for y in range(m - x + 1):
            z = m - x - y
            if (a + x == b + y) or (a + x == c + z) or (b + y == c + z):
                flag = True
                break
        if flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")
