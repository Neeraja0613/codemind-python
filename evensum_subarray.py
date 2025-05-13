t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    max_len = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s % 2 == 0:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
    print(max_len)
