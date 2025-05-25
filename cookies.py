t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if m < n:
        print(n - m)
    else:
        r = m % n
        add = n - r
        rem = r
        min_ops = min(add, rem)
        print(min_ops)
