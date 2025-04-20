t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    max_val = max(a, b, c)
    total = a + b + c - max_val
    if max_val <= total + 1:
        print("YES")
    else:
        print("NO")
