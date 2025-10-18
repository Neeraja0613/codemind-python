# cook your dish here
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    S = input().strip()
    flipped = ""
    for ch in S:
        if ch == '0':
            flipped += '1'
        else:
            flipped += '0'
    results.append(flipped)
for res in results:
    print(res)
