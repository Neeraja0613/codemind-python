t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=a[0]
    r=sum(1 for i in a if i>=x)
    print(r)
