x = int(input())
for i in range(x):
    a = int(input())
    s = input().strip()
    l = list(map(int,s))
    c = []
    if 0 in l:
        ind = l.index(0)
        c = l[ind+1:]
        print(c.count(1))
    else:
        print("0")
