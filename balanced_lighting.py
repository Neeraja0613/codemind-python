def bal(n,c):
    r=c.count(1)
    b=c.count(2)
    x=c.count(0)
    diff=abs(r-b)
    if diff<=x and (x-diff)%2==0:
        return "YES"
    else:
        return "NO"

t=int(input())
for i in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    print(bal(n,c))
