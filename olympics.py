g, s, b = map(int, input().split())

total = g + s + b
if total < 15:
    print(15 - total)
else:
    print(0)
