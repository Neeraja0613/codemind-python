T = int(input())
for _ in range(T):
    A1, A2, B1, B2 = map(int, input().split())
    if A2 + B2 > A1 + B1:
        print("YES")
    else:
        print("NO")
