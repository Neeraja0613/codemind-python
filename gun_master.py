t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    curr = 0
    switches = 0
    for value in a:
        if value <= d:
            if curr == 1:
                switches += 1
                curr = 0
        else:
            if curr == 0:
                switches += 1
                curr = 1
    print(switches)
